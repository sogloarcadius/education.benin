from django.conf.urls import url, include
from rest_framework import routers
from api import views

class ApiReference(routers.APIRootView):
    """
    Edubenin API
    """
    pass


class APIRouter(routers.DefaultRouter):
    APIRootView = ApiReference


router = APIRouter()
router.register(r'districts', views.DistrictViewSet)
router.register(r'cities', views.CityViewSet)
router.register(r'provinces', views.ProvinceViewSet)
router.register(r'universities', views.UniversityViewSet)
router.register(r'faculties', views.FacultyViewSet)
router.register(r'courses', views.CourseViewSet)

urlpatterns = [
    url(r'^swagger$', views.api_swagger),
    url(r'^', include(router.urls))
]