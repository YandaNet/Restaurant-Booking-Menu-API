from rest_framework import generics
from .models import Category, Dish
from .serializers import CategorySerializer, DishSerializer


class CategoryListView(generics.ListAPIView):
    """список усіх категорій."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DishListCreateView(generics.ListCreateAPIView):
    """
    GET: список усіх страв.
    POST: Додати нову страву.
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class DishDetailView(generics.RetrieveAPIView):
    """список усіх страв."""
    queryset = Dish.objects.all()
    serializer_class = DishSerializer