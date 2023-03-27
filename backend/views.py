from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Todo
from .serializers import TodoSerializer

# Create your views here.
# list all todo
@api_view(['GET'])
def todoList(request):
    todo = Todo.objects.all().order_by('-updated_at')
    serializer = TodoSerializer(todo, many=True)
    return Response(serializer.data)
# detail of one object
@api_view(['GET'])
def todoDetail(request, pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todo, many=False)
    return Response(serializer.data)
# create todo
@api_view(['POST'])
def todoCreate(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save();
    return Response(serializer.data)

@api_view(['PUT'])
def todoUpdate(request, pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance=todo, data=request.data)
    if serializer.is_valid():
        serializer.save();
    return Response(serializer.data)

@api_view(['DELETE'])
def todoDelete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()

    return Response("Successfully deleted")






# class TodoList(APIView):
#     def get(self, request):
#         todo = Todo.objects.all()
#         serializer = TodoSerializer(todo, many=True)
#         return Response(serializer.data)

#     def post(self):
#         pass
