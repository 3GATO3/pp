from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Todo
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import TodoSerializer, UserSerializer, GroupSerializer, CalificacionSerializer
from .models import Calificacion
import gspread
import pandas as pd

class TodoListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        todos = Todo.objects.filter(user = request.user.id)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


    def post(self, request, *args, **kwargs):
        data = {
            'task': request.data.get('task'),
            'completed': request.data.get('completed'),
            'user': request.user.id
        }

        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TodoDetailApiView(APIView):


    def get_object(self, todo_id, user_id):
        try:
            return Todo.objects.get(id=todo_id, user = user_id)
        except Todo.DoesNotExist:
            return None
        
    def get(self, request, todo_id, *args, **kwargs):
        todo_instance = self.get_object(todo_id,request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status = status.HTTP_400_BAD_REQUEST
            )
        serializer = TodoSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, todo_id, *args, **kargs):
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 

                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'task':request.data.get('task'),
            'completed': request.data.get('completed'),
            'user': request.user.id
        }

        serializer =TodoSerializer(instance= todo_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, todo_id, *args, **kwargs):
        todo_instance = self.get_object(todo_id,request.user.id)
        if not todo_instance:
            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )
        todo_instance.delete()
        return Response(
             {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
    



class CalificacionListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    """ def get(self, request, *args, **kwargs):
        calificaciones = Calificacion.objects.filter(user = request.user.id)
        serializer = TodoSerializer(calificaciones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
     """
    def get(self, request, *args, **kargs):
        spreadsheetName = 'Copia de Control 2020 Test'
        gc = gspread.oauth()
        sh = gc.open(spreadsheetName)
        calificaciones= sh.worksheet('Calificación')
        calificaciones = calificaciones.get_all_values()
        calificaciones= pd.DataFrame(calificaciones[1:], columns=calificaciones[0])
        serialized_data = calificaciones.to_json(orient='table')
        f = open("data.txt", "w")
        f.write(serialized_data)
        f.close()
        return Response(serialized_data)
    


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer
    permission_classes = [permissions.IsAuthenticated]



# Create your views here.
