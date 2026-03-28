from rest_framework import viewsets
from .serializers import CitySerializer
from .models import City
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.
class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    parser_classes = [MultiPartParser, FormParser]