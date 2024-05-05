from django.urls import path
from . import views
urlpatterns = [
    path('cab/', views.CabListCreate.as_view(),name='CabListCreate'),
    path('cab/delete/<int:pk>/', views.CabRetrieveUpdateDestroy.as_view(),name='Delete-cab'),
    path('booking/', views.BookingListCreate.as_view(),name='BookingListCreate'),
    path('booking/delete/<int:pk>/', views.BookingRetrieveUpdateDestroy.as_view(),name='Delete-booking'),
]