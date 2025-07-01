from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CategoryViewset, ProductViewset

router = DefaultRouter()
router.register(r'categories', CategoryViewset)
router.register(r'products', ProductViewset)


urlpatterns = [
    path('', include)(router.urls)
]