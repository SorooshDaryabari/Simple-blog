from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsCreatorOrIsStaffOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        elif request.user == obj.user:
            return True

        return request.user.is_staff

