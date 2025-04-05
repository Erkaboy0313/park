from rest_framework.routers import SimpleRouter,DefaultRouter
from django.urls import path,include
user = DefaultRouter()
from .views import RegisterView,ProfileVieset,CardViewSet

user.register(r'auth',RegisterView,basename='auth')
user.register(r'profile',ProfileVieset,basename='profile')
user.register(r'card',CardViewSet,basename='card')


urlpatterns = [
    path('', include(user.urls)),
]