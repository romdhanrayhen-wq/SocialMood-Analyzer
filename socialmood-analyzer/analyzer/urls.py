from django.urls import path
from . import views

urlpatterns = [
    path('',            views.home,       name='home'),
    path('analyze/',    views.analyze,    name='analyze'),
    path('historique/', views.historique, name='historique'),
    path('dashboard/',  views.dashboard,  name='dashboard'),
]
