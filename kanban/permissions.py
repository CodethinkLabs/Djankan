from rest_framework import permissions
import re

class defaultPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        path = request.path
        # if in the user/ subpath any user can GET but for any other
        # method the request user must be an admin or the user who's
        # data is being edited
        if re.match(r'^user/', path):
            if request.method = 'GET':
                return True
            userPath = re.search(r'^users/(.+?)/',path)
            if user == userPath:
                return True
            return False
        # if in the kanban/ subpath anybody with any role on the kanban
        # can GET but for any other method the request user must be an
        # Editor
        try:
            findKanbanID = re.search(r'^kanban/(.+?)/', path)
            kanbanID = findKanbanID.group(1)
        except:
            return False
        if request.method = 'GET':
            return Permissions.objects.filter(
                user=user,
                kanban=kanbanID
                ).exists()
   
        return Permissions.objects.filter(
            user=user,
            kanban=kanbanID,
            USER_ROLE='EDIT'
            ).exists()
