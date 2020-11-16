from django.urls import path, include
from rest_framework import routers
from data.views import TemperatureViewSet

router = routers.DefaultRouter()

router.register(
    r'temperature', 
    TemperatureViewSet,
    basename='temp'
)

urlpatterns = router.urls