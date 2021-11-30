from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView
)
from .serializers import (
    ProductsFeedbackSerializer,
    ProductFeedbackUpVotesSerializer,
    CommentsFeedbackSerializer,
    CreateReplySerializer
)
from .models import *


def get_serialized_queryset():
    return ProductsFeedbackSerializer(ProductFeedback.objects.all(), many=True)


class ProductsFeedbackListView(ListCreateAPIView):

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]

    def get(self, request, *args, **kwargs):
        products = ProductFeedback.objects.all()
        serializer = ProductsFeedbackSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ProductsFeedbackSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetUpdateDeleteFeedbackView(RetrieveUpdateDestroyAPIView):

    def get_object(self, pk):
        try:
            return ProductFeedback.objects.get(id=pk)
        except ProductFeedback.DoesNotExist:
            raise Http404

    def get_permissions(self):
        if self.request.method == 'GET' or self.request.method == 'PATCH':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]

    def get(self, request, *args, **kwargs):
        serializer = ProductsFeedbackSerializer(self.get_object(kwargs['pk']))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        serializer = ProductsFeedbackSerializer(instance=self.get_object(kwargs['pk']), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        serializer = ProductFeedbackUpVotesSerializer(instance=self.get_object(kwargs['pk']), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        self.get_object(kwargs['pk']).delete()
        print(kwargs['pk'])
        return Response(data={'id': kwargs['pk']}, status=status.HTTP_200_OK)


class CreateCommentView(CreateAPIView):
    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request, *args, **kwargs):
        serializer = CommentsFeedbackSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreateReplyView(CreateAPIView):
    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request, *args, **kwargs):
        serializer = CreateReplySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
