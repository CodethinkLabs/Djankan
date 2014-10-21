from rest_framework import permissions

class editPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        result = Permissions.objects.filter(
            kanban=request.kanban,
            user=request.user,
            USER_ROLE='EDIT'
            ).exists()
        return result

class viewPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        result = Permissions.objects.filter(
            kanban=request.kanban,
            user=request.user,
            USER_ROLE='VIEW'
            ).exists()
        return result 
