import json
import jwt

from django.contrib.auth.models import User
from django.conf import settings
from rest_framework import authentication
from rest_framework import exceptions

class JwtAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('Authorization')
        payload = json.loads(
            jwt.decode(
                token,
                settings.JWT_SECRET,
                algorithm=[settings.JST_ALGORITHM]
            )
        )

        user_id = payload.get('user_id')
        if not user_id:
            return None

        try:
            user = User.object.get(pk=user_id)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)
