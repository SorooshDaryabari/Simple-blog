from rest_framework import serializers
from accounts.models import Profile, Follower
from django.contrib.auth import get_user_model
from accounts.tasks import send_email_activation_code_task
from django.utils.crypto import get_random_string
from django.shortcuts import reverse


class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ("user",)


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ("follower",)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            "account_id",
            "profile_image",
            "about",
            "resume",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
        )

    def create(self, validated_data):
        username = validated_data.get("username")
        first_name = validated_data.get("first_name")
        last_name = validated_data.get("last_name")
        email = validated_data.get("email")
        email_unique_code = get_random_string(255)

        user = get_user_model().objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            email_unique_code=email_unique_code,
            is_active=False,
        )
        user.set_password(validated_data.get("password"))
        full_name = f"{first_name} {last_name}"

        email_activate_url = reverse("activate-email", args=(email_unique_code,))

        send_email_activation_code_task.delay(full_name, email, email_activate_url)

        return user


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
        )


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("username", "password")
