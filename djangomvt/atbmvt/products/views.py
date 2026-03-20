import os
import json
import uuid
from io import BytesIO

from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils.text import slugify

from PIL import Image
from django.core.files.base import ContentFile

from .models import Product, ProductImage
from .forms import ProductForm
# Create your views here.
def show_products(request):
    products = Product.objects.prefetch_related("images").all()
    return render(request, 'products.html', {'products': products})


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        images_ids = [i for i in request.POST.getlist('images') if i and i.isdigit()]
        if form.is_valid():
            product = form.save(commit=False)
            if not product.slug:
                product.slug = slugify(product.name, allow_unicode=False)
            product.save()
            for idx, img_id in enumerate(images_ids):
                img = ProductImage.objects.get(id=img_id)
                img.product = product
                img.priority = idx
                img.save()

            return redirect("products:show_products")  # назва URL на список товарів
    else:
        form = ProductForm()

    return render(request, "add_product.html", {"form": form})


def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    existing_images = list(product.images.order_by('priority'))

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        new_images_ids = [i for i in request.POST.getlist('new_images') if i and i.isdigit()]
        kept_images_ids = [i for i in request.POST.getlist('kept_images') if i and i.isdigit()]

        if form.is_valid():
            product = form.save(commit=False)
            if not product.slug:
                product.slug = slugify(product.name, allow_unicode=False)
            product.save()

            for img in existing_images:
                if str(img.id) not in kept_images_ids:
                    if img.image and os.path.isfile(img.image.path):
                        os.remove(img.image.path)
                    img.delete()

            for idx, img_id in enumerate(kept_images_ids):
                try:
                    img = ProductImage.objects.get(id=int(img_id), product=product)
                    img.priority = idx
                    img.save()
                except ProductImage.DoesNotExist:
                    pass

            offset = len(kept_images_ids)
            for idx, img_id in enumerate(new_images_ids):
                try:
                    img = ProductImage.objects.get(id=int(img_id), product__isnull=True)
                    img.product = product
                    img.priority = offset + idx
                    img.save()
                except ProductImage.DoesNotExist:
                    pass

            return redirect("products:show_products")
    else:
        form = ProductForm(instance=product)

    return render(request, "edit_product.html", {
        "form": form,
        "product": product,
        "existing_images": existing_images,
    })
@csrf_exempt
def upload_temp_image(request):
    if request.method == "POST":
        file_key = list(request.FILES.keys())[0]
        image_file = request.FILES[file_key]

        img = ProductImage()
        img_image = Image.open(image_file)
        if img_image.mode in ("RGBA", "P"):
            img_image = img_image.convert("RGB")

        filename = f"{uuid.uuid4().hex}.webp"
        buffer = BytesIO()
        img_image.save(buffer, format="WEBP")
        buffer.seek(0)
        img.image.save(filename, ContentFile(buffer.read()), save=True)

        return JsonResponse({"file_id": img.id})


@csrf_exempt
def delete_temp_image(request):
    if request.method == "DELETE":
        data = json.loads(request.body)
        file_id = data.get("file_id")
        if file_id:
            try:
                img = ProductImage.objects.get(id=file_id, product__isnull=True)
                if img.image:
                    if os.path.isfile(img.image.path):
                        os.remove(img.image.path)
                img.delete()
                return JsonResponse({"status": "ok"})
            except ProductImage.DoesNotExist:
                return JsonResponse({"error": "File not found"}, status=404)
        return JsonResponse({"error": "No file_id provided"}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)


def delete_product(_, product_id):
    try:
        product = Product.objects.get(id=product_id)

        for img in product.images.all():
            if img.image:
                img.image.delete(save=False)
            img.delete()

        product.delete()

    except Product.DoesNotExist:
        pass

    return redirect('products:show_products')
