# filepath: Tables/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.table_list, name='table_list'),
    path('<int:id>/', views.table_detail, name='table_detail'),
    path('create/', views.table_create, name='table_create'),
    path('<int:id>/update/', views.table_update, name='table_update'),
    path('<int:id>/delete/', views.table_delete, name='table_delete'),
]