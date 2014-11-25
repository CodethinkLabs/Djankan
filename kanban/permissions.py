#The MIT License (MIT)

#Copyright (c) 2014 Codethink

#Permission is hereby granted, free of charge, to any person obtaining a copy of
#this software and associated documentation files (the "Software"), to deal in
#the Software without restriction, including without limitation the rights to
#use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
#the Software, and to permit persons to whom the Software is furnished to do so,
#subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
#FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
#COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
#IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
#CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

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
