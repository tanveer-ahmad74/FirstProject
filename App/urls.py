from django.urls import path, include
from rest_framework.routers import DefaultRouter
from App import views
from App.views import ColorViewSet, UserViewSet

router_master = DefaultRouter()
router_master.register('color', ColorViewSet, basename="color")
router_master.register('users', UserViewSet, basename="users")

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('', include(router_master.urls)),
]
