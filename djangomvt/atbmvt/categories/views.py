from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Category
from .forms import CategoryForm
from users.utils import save_custom_image
from django.utils.text import slugify


def category_list(request):
    categories = Category.objects.all().order_by('name')
    return render(request, 'categories/category_list.html', {
        'categories': categories
    })


@login_required(login_url='/users/login/')
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                category = form.save(commit=False)
                if not category.slug:
                    category.slug = slugify(category.name, allow_unicode=False)
                if 'image' in request.FILES:
                    image = request.FILES['image']
                    image_name = save_custom_image(image, size=(600, 600), folder='categories')
                    category.image = image_name

                category.save()
                messages.success(request, f'Категорію "{category.name}" успішно створено!')
                return redirect('categories:list')

            except Exception as e:
                messages.error(request, f'Помилка при створенні: {str(e)}')
        else:
            messages.error(request, 'Виправте помилки у формі.')
    else:
        form = CategoryForm()

    return render(request, 'categories/category_create.html', {'form': form})


@login_required(login_url='/users/login/')
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        name = category.name
        category.delete()
        messages.success(request, f'Категорію "{name}" видалено.')
        return redirect('categories:list')

    return redirect('categories:list')