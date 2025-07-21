from django.urls import path
from .views import ProdutoAPI

urlpatterns = [
    path('api/produtos', ProdutoAPI.as_view(), name='api_produtos'),
]
