from .models import CustomUser
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer): # наслідує ModelSerializer - автоматично створює поля з моделі
    class Meta:
        model = CustomUser # вказує яку модель серіалізувати
        fields = [ # вказує які поля включити у відповідь
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'image_small',
            'image_medium',
            'image_large'
        ]

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer): # наслідує стандартний JWT серіалізатор
    @classmethod
    def get_token(cls, user):  # викликається при створенні токена
        token = super().get_token(user)  # створює стандартний токен (з id, exp тощо)

        # Додає власні дані всередину токена
        token['id'] = user.id
        token['username'] = user.username
        token['email'] = user.email
        # token['phone'] = user.phone if user.phone else None
        token['image'] = user.image_small.url if user.image_small else None  # якщо є фото - додає URL, інакше None
        token['date_joined'] = user.date_joined.strftime('%Y-%m-%d %H:%M:%S')

        return token  # повертає токен з додатковими даними