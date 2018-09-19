from api import models
from api import serializers 
from rest_framework import viewsets
from rest_framework_swagger.views import get_swagger_view


api_swagger = get_swagger_view(title='Edubenin API')


class DistrictViewSet(viewsets.ModelViewSet):
    """
    /districts
    """
    queryset = models.District.objects.all()
    serializer_class = serializers.DistrictSerializer


class CityViewSet(viewsets.ModelViewSet):
    """
    /cities
    """
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer


class ProvinceViewSet(viewsets.ModelViewSet):
    """
    /provinces
    """
    queryset = models.Province.objects.all()
    serializer_class = serializers.ProvinceSerializer


class UniversityViewSet(viewsets.ModelViewSet):
    """
    /universities
    """
    queryset = models.University.objects.all()
    serializer_class = serializers.UniversitySerializer


class FacultyViewSet(viewsets.ModelViewSet):
    """
    /faculties
    """
    queryset = models.Faculty.objects.all()
    serializer_class = serializers.FacultySerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    /courses
    """
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer