from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Dish, Table, Reservation


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class DishSerializer(serializers.ModelSerializer):
    category_detail = CategorySerializer(source='category', read_only=True)

    class Meta:
        model = Dish
        fields = ['id', 'name', 'description', 'price', 'category', 'category_detail', 'is_available']


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'number', 'seats', 'is_available']


class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    table_detail = TableSerializer(source='table', read_only=True)

    class Meta:
        model = Reservation
        fields = ['id', 'user', 'table', 'table_detail', 'date', 'time', 'guests_count', 'status', 'created_at']
        read_only_fields = ['status', 'user']


class ReservationStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['status']