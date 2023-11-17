from django.urls import include, path
from rest_framework import routers
from .views import StudentViewSet, CollegeViewSet, CourseViewSet

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'colleges', CollegeViewSet)
router.register(r'courses', CourseViewSet)
urlpatterns = [
    path('api/', include(router.urls)),
    # Other URL patterns in your project
]
