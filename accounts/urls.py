from rest_framework import routers
from accounts.views import (
    ProfileViewSet,
    UserViewSet,
    FollowingView,
    FollowersView,
    LoginView,
    activate_email,
)
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.SimpleRouter()
router.register("profiles", ProfileViewSet, basename="profiles")
router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("login/", LoginView.as_view(), name="login"),
    path("profiles/<str:account_id>/followings-list/", FollowingView.as_view(), name="followings-list"),
    path("profiles/<str:account_id>/followers-list/", FollowersView.as_view(), name="followers-list"),
    path("activate-email/<str:email_activate_code>/", activate_email, name="activate-email")
]

urlpatterns += router.urls
