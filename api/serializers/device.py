from rest_framework import serializers
from api.models import Device

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Device
        fields = ('id', 'status', 'device_uid', 'user')

    def create(self, validated_data):
        return Device.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.device_uid = validated_data.get('device_uid', instance.device_uid)

        # TODO: Verify that the UID of device is correct by making calls to appropriate APIs, and update status
        instance.save()

        return instance
