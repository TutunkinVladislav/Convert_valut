from django.template.defaulttags import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import convert_valut_usd_to_rub

app_name = 'api'

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('rates', convert_valut_usd_to_rub),
]

