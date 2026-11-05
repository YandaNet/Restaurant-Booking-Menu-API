from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    RegisterView,
    CategoryListView,
    DishListCreateView,
    DishDetailView,
    TableListView,
    ReservationCreateView,
    UserReservationListView,
    ReservationDetailView,
    ReservationStatusUpdateView,
    ReservationCancelView,
)

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('dishes/', DishListCreateView.as_view(), name='dish-list-create'),
    path('dishes/<int:pk>/', DishDetailView.as_view(), name='dish-detail'),
    path('tables/', TableListView.as_view(), name='table-list'),
    path('reservations/create/', ReservationCreateView.as_view(), name='reservation-create'),
    path('reservations/my/', UserReservationListView.as_view(), name='user-reservations'),
    path('reservations/<int:pk>/', ReservationDetailView.as_view(), name='reservation-detail'),
    path('reservations/<int:pk>/status/', ReservationStatusUpdateView.as_view(), name='reservation-status-update'),
    path('reservations/<int:pk>/cancel/', ReservationCancelView.as_view(), name='reservation-cancel'),
]