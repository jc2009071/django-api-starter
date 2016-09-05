from rest_framework import serializers
from django.contrib.auth.models import User

from api.models import Device
from api.models import UserCredential
from api.serializers.user_credential import UserCredentialSerializer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    devices = serializers.HyperlinkedRelatedField(view_name='device-detail', many=True, queryset=Device.objects.all())
    facebook_token = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = ('id', 'username', 'devices', 'facebook_token',)
