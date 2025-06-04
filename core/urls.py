from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_ficha, name='criar_ficha'),
    path('ficha/<int:ficha_id>/', views.ver_ficha, name='ver_ficha'),
]
