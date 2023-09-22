from django.urls import path, include
from .views import(
    TodoListApiView,
    TodoDetailApiView,
    CalificacionListApiView
)

urlpatterns = [
    path('api', TodoListApiView.as_view()),
    path('api/<int:todo_id>/', TodoDetailApiView.as_view()),
    path('api/calificaciones', CalificacionListApiView.as_view())
]
