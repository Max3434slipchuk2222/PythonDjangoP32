from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet, basename='department')

urlpatterns = [
    path('', include(router.urls)),
]