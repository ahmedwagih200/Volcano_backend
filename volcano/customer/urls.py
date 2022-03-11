from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.get_reviews, name='get'),
    path('add/', views.add_review, name='add_review'),
]
