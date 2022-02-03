from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('profile/', views.UserDetail.as_view(),
         name='profile_detail'),
    path('profile/influences/<int:pk>', views.InfluenceDetail.as_view(),
         name='influence_detail')
]
