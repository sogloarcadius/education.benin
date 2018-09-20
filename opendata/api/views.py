from api import models
from api import serializers 
from rest_framework import viewsets
from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view

api_swagger = get_swagger_view(title='Edubenin API')
schema_view = get_schema_view(title='Edubenin API')


class DistrictViewSet(viewsets.ModelViewSet):
    """
    /districts
    """
    queryset = models.District.objects.all()
    serializer_class = serializers.DistrictSerializer
    http_method_names = ['get']



class CityViewSet(viewsets.ModelViewSet):
    """
    /cities
    """
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer
    http_method_names = ['get']



class ProvinceViewSet(viewsets.ModelViewSet):
    """
    /provinces
    """
    queryset = models.Province.objects.all()
    serializer_class = serializers.ProvinceSerializer
    http_method_names = ['get']



class UniversityViewSet(viewsets.ModelViewSet):
    """
    /universities
    """
    queryset = models.University.objects.all()
    serializer_class = serializers.UniversitySerializer
    http_method_names = ['get']


class FacultyViewSet(viewsets.ModelViewSet):
    """
    /faculties
    """
    queryset = models.Faculty.objects.all()
    serializer_class = serializers.FacultySerializer
    http_method_names = ['get']
    filter_fields = ('university', 'city',)



class CourseViewSet(viewsets.ModelViewSet):
    """
    /courses
    """
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    http_method_names = ['get']
