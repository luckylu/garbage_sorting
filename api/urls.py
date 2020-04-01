from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('garbages/<garbage>/', views.garbages),
    path('exact_garbages/<garbage>/', views.exact_garbages),
]
