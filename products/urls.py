from django.urls import path, include
from .views import ProductViewSet, CategoryViewSet
from rest_framework import routers


app_name = "products"

router = routers.DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"", ProductViewSet)


urlpatterns = [
    path("", include(router.urls))
]