from django.urls import path
from . import views

urlpatterns = [
    path('library/', views.SongList.as_view()),
    path('library/<int:pk>/', views.SongDetail.as_view()),
]