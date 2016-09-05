from rest_framework import serializers

from api.models import UserCredential

class UserCredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCredential
        fields = ('facebook_token', 'user')
