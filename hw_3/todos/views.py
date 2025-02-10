from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.decorators import action
from .forms import TodoForm

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @action(detail=True, methods=['delete'])
    def delete_todo(self, request, pk=None):
        todo = self.get_object()
        todo.delete()
        return Response({"message": "Todo deleted successfully"})

def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos_list')  # Перенаправляем на страницу с todos
    else:
        form = TodoForm()
    return render(request, 'todos/create_todo.html', {'form': form})

def home(request):
    return render(request, 'home.html')