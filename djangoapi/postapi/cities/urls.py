from rest_framework.routers import DefaultRouter
from .views import CityViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'cities', CityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]