from rest_framework.routers import DefaultRouter
from .views import LoginView, UserViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('users/login/', LoginView.as_view(), name='login'), # логін, повертає JWT токени
    path('', include(router.urls)) # підключає всі URL згенеровані router
]