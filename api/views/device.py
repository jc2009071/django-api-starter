from rest_framework import viewsets
from rest_framework import permissions

from api.models import Device
from api.serializers import DeviceSerializer
from api.permissions import IsOwnerOrReadOnly

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
