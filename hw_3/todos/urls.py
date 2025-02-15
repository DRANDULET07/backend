from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet
from . import views

router = DefaultRouter()
router.register(r"todos", TodoViewSet)

urlpatterns = [
    path("todos/create/", views.create_todo, name="create_todo"),
    path(
        "todos/<int:pk>/delete/",
        views.TodoViewSet.as_view({"delete": "delete_todo"}),
        name="delete_todo",
    ),
]
