from django.conf.urls import url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'universities', views.UniversityViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'faculties', views.FacultyViewSet)
router.register(r'emergency', views.EmergencyViewSet)
router.register(r'departements', views.DepartementViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]