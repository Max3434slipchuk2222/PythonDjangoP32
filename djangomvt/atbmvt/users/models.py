from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
#Клас успадковується від AbstractUser - дозволяє використовувати вбудовані механізми Django
class CustomUser(AbstractUser):
    #три поля для зображень різних розмірів
    #models.ImageField - створює спеціальне поле для зберігання файлів зображень
    #Вказуємо в яку папку зберігати а також ставимо завантаження фото не обов'язковою
    image_small = models.ImageField(upload_to='avatar/', null=True, blank=True)
    image_medium = models.ImageField(upload_to='avatar/', null=True, blank=True)
    image_large = models.ImageField(upload_to='avatar/', null=True, blank=True)

    #метод який визначає як об'єкт користувача буде відображатися в текстовому вигляді
    def __str__(self):
        return self.email
