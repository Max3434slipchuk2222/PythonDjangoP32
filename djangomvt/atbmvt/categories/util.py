import uuid


def upload_image(instance, filename):
    return f"images/{uuid.uuid4()}.webp"