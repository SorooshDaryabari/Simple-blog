from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from accounts.serializers import (
    ProfileSerializer,
    UserSerializer,
    UpdateUserSerializer,
    FollowingSerializer,
    FollowerSerializer,
    LoginSerializer
)
from accounts.permissions import IsCreatorOrIsStaffOrReadOnly
from accounts.models import Profile, Follower
from django.contrib.auth import get_user_model
from django.shortcuts import Http404
from rest_framework.response import Response
from rest_framework import status
from django.utils.crypto import get_random_string
from django.contrib.auth import authenticate, login


class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = (IsCreatorOrIsStaffOrReadOnly, IsAuthenticated)
    queryset = Profile.objects.all()
    lookup_field = "account_id"


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    lookup_field = "id"

    def get_serializer_class(self):
        serializer_class = UserSerializer
        if self.action in ("update", "retrieve"):
            serializer_class = UpdateUserSerializer
        return serializer_class


class FollowingView(ListCreateAPIView):
    serializer_class = FollowingSerializer

    def get_queryset(self):
        return Follower.objects.filter(profile__account_id__iexact=self.kwargs.get("account_id"))


class FollowersView(ListCreateAPIView):
    serializer_class = FollowerSerializer

    def get_queryset(self):
        return Follower.objects.filter(profile__account_id__iexact=self.kwargs.get("account_id"))


def activate_email(request, email_activate_code):
    user = get_user_model().objects.get(email_unique_code__iexact=email_activate_code)

    if user is not None:
        user.is_active = True
        user.email_unique_code = get_random_string(255)
        user.save()
        return Response(status=status.HTTP_200_OK)
    else:
        raise Http404


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
