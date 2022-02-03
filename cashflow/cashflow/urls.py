from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('profile/', views.ProfileDetail.as_view(),
         name='profile_detail'),
    path('profile/create', views.CreateProfile.as_view()),
    path('profile/bills/create', views.CreateBill.as_view())
]
