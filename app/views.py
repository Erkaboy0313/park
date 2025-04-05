from rest_framework.viewsets import ViewSet,ModelViewSet
from .serializers import RegisterParkingSerialzier,ParkingShortSeraizer,ParkingDetailSeraizer,BookingSerializer,BookingDetailSerializer
from .models import Parking
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Count,Q

from user.permission import IsOwner

class RegisterParkingViewSet(ModelViewSet):

    serializer_class = RegisterParkingSerialzier
    http_method_names = ['get','post']
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Parking.objects.filter(owner = self.request.user)

    def perform_create(self, serializer):
        data = serializer.save(owner = self.request.user)
        return data

class ParkingViewSet(ViewSet):
    
    def list(self,request):
        parkings = Parking.objects.all()
        serializer = ParkingShortSeraizer(parkings,many = True)
        return Response(serializer.data)

    @action(methods=['POST'],detail=False)
    def parking_detail(self,request,*args,**kwargs):
        parking_id = request.data.get('parking_id',None)
        parking = Parking.objects.annotate(floor_count = Count('floors',distinct=True),free_slot = Count("floors__slot", filter=Q(floors__slot__status=False))).get(id = parking_id)
        serializer = ParkingDetailSeraizer(parking)
        return Response(serializer.data)
    
class BookingSlot(ViewSet):

    @action(methods=['POST'],detail=False)
    def book(self,request,*args,**kwargs):
        serializer = BookingSerializer(data = request.data,context = {"request":request})
        serializer.is_valid(raise_exception=True)
        data = serializer.save(action = 'book')
        ss = BookingDetailSerializer(data)
        return Response(ss.data)

    @action(methods=['POST'],detail=False)
    def arrive(self,request,*args,**kwargs):
        pass

    @action(methods=['POST'],detail=False)
    def left(self,request,*args,**kwargs):
        pass

    @action(methods=['POST'],detail=False)
    def reject(self,request,*args,**kwargs):
        pass
