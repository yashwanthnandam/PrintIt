from rest_framework.routers import DefaultRouter
from PrintIt import views
from django.urls import include, path

router = DefaultRouter()
router.register(r'^printer', views.Printer, basename='printer')

urlpatterns = [
    path('', include(router.urls)),
]