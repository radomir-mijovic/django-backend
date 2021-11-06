from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView
from .serializers import TodosSerializer
from .models import Todos


def get_todos():
    todos = Todos.objects.all()
    serializer = TodosSerializer(todos, many=True)
    return serializer.data


class TodosView(ListCreateAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer

    def get(self, request, **kwargs):
        return Response(get_todos(), status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = TodosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(get_todos(), status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer

    def put(self, request, *args, **kwargs):
        task = Todos.objects.get(pk=kwargs['pk'])
        serializer = TodosSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(get_todos(), status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        task = Todos.objects.get(pk=kwargs['pk'])
        task.delete()
        return Response(get_todos(), status=status.HTTP_200_OK)


class DeleteCompletedView(DestroyAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer

    def delete(self, request, *args, **kwargs):
        todo = Todos.objects.filter(completed=True).all()
        todo.delete()
        return Response(get_todos(), status=status.HTTP_200_OK)
