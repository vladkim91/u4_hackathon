from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('profile', views.ProfileDetail.as_view(),
         name='profile_detail'),
    path('profile/login', views.Login.as_view()),
    path('profile/create', views.CreateProfile.as_view()),
    path('profile/bills/create', views.CreateBill.as_view()),
    path('profile/bills/update', views.UpdateBill.as_view()),
    path('profile/bills/<int:pk>/delete', views.DeleteBill.as_view()),
    path('profile/transactions/create', views.CreateTransaction.as_view())
]
