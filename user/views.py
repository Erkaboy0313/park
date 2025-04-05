from rest_framework.viewsets import ViewSet,ModelViewSet
from .serializers import RegisterSerializer,VerifySerializer,UserProfileSerializer,CardSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser,Card


class RegisterView(ViewSet):
    
    @action(methods=['POST'],detail=False)
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"message":f"code was sent to {user.phone} number","user":user.id}, status=status.HTTP_200_OK)

    @action(methods=['POST'],detail=False)
    def verify_number(self,request):
        serializer = VerifySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(data)
        

class ProfileVieset(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    http_method_names = ['get','post']
    permission_classes = (IsAuthenticated,)
    
    def list(self, request, *args, **kwargs):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)
        
    def create(self, request, *args, **kwargs):
        serializer = UserProfileSerializer(data = request.data,instance = request.user,partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class CardViewSet(ModelViewSet):
    serializer_class = CardSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Card.objects.filter(user = self.request.user)
    
    def perform_create(self, serializer):
        data = serializer.save(user = self.request.user)
        return data
    