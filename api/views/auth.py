import jwt
import facebook

from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import UserSerializer
from api.serializers import UserCredentialSerializer

class Auth(APIView):
    """
    Auth class with JWT was custom written because I needed some experience
    handling auth without packages.

    It was quite a pain. Don't do it.
    """

    def post(self, request, format=None):
        access_token = request.data.get('facebook_token')
        graph = facebook.GraphAPI(access_token=access_token)

        try:
            username = graph.get_object('me').get('id')
        except facebook.GraphAPIError:
            error = {'error': 'Invalid access token.'}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

        user_data = {
            'username': username,
            'devices': [],
        }

        user = User.objects.get(username=username)

        if not user:
            user_serializer = UserSerializer(data=user_data)
            if user_serializer.is_valid():
                user = user_serializer.save()
            else:
                error = {'error': user_serializer.errors}
                return Response(error, status=status.HTTP_400_BAD_REQUEST)

            user_credentials_serializer = UserCredentialSerializer(data={'facebook_token': access_token, 'user': user.id})
            if user_credentials_serializer.is_valid():
                user_credentials = user_credentials_serializer.save()
            else:
                error = {'error': user_credentials_serializer.errors}
                return Response(error, status=status.HTTP_400_BAD_REQUEST)

        jwt_payload = {
            'user_id': user.id
        }

        jwt_token = jwt.encode(jwt_payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)

        res = {
            'hash_token': jwt_token
        }

        return Response(res, status=status.HTTP_201_CREATED)
