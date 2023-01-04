from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from utils.pagination import Page
from App.models import Colors
from App.serializers import ColorSerializer, UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class ColorViewSet(ModelViewSet):
    queryset = Colors.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ColorSerializer
    pagination_class = Page

    def get_queryset(self):
        return self.queryset.filter(is_delete=False).order_by('id')

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.soft_delete()
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    pagination_class = Page
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(is_delete=False).order_by('id')

    def create(self, request, *args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = User.objects.last()
        user.set_password(user.password)
        user.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.soft_delete()
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
