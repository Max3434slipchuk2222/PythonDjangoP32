import random
from rest_framework import viewsets, parsers, status
from rest_framework.decorators import action
from django.shortcuts import render
from .serializers import CustomTokenObtainPairSerializer, UserSerializer
from .models import CustomUser
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

# from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth.tokens import default_token_generator


# Create your views here.
FIRST_NAMES = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"] # список імен для генерації
LAST_NAMES = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Lee"] # список прізвищ для генерації
DOMAINS = ["example.com", "test.com", "mail.com"] # список доменів для email


def generate_random_users(n=5): # приймає кількість користувачів, для їхньої генерації
    created_users = []

    for _ in range(n):
        while True:
            username = f"user{random.randint(1000, 9999)}" # генерує username типу "userxxxx"
            if not CustomUser.objects.filter(username=username).exists(): # перевіряє чи не існує вже такий username
                break

        first_name = random.choice(FIRST_NAMES) # генерує випадкове ім'я
        last_name = random.choice(LAST_NAMES) # генерує випадкове прізвище
        email = f"{first_name.lower()}.{last_name.lower()}@{random.choice(DOMAINS)}" # генерує email

        user = CustomUser.objects.create( # створює користувача в БД
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        created_users.append(user) # додає до списку

    return created_users # повертає список створених користувачів


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all() # всі користувачі з БД
    serializer_class = UserSerializer # серіалізатор для перетворення в JSON
    parser_classes = [parsers.MultiPartParser, parsers.FormParser] # підтримка form-data (для файлів)

    @action(detail=False, methods=["post"])
    def generate(self, request):
        users = generate_random_users(5)  # генерує 5 користувачів
        serializer = self.get_serializer(users, many=True) # серіалізує список
        return Response(serializer.data)  # повертає JSON


class LoginView(TokenObtainPairView): # наслідує стандартний JWT логін
    serializer_class = CustomTokenObtainPairSerializer  # використовує кастомний серіалізатор

    def post(self, request, *args, **kwargs):
        # print('-------working login--------')
        serializer = self.get_serializer(data=request.data) # передає дані запиту в серіалізатор
        # print("-----data server------", serializer)
        try:
            serializer.is_valid(raise_exception=True) # валідує дані, якщо невалідні - кидає помилку
        except Exception as e:
            return Response({"detail": "Invalid credentials"}, status=401) # повертає 401 якщо невірні дані

        return Response(serializer.validated_data, status=status.HTTP_200_OK) # повертає токени якщо успішно