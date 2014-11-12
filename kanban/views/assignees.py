from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from kanban.models import *
from kanban.serializers import *
from django.http import Http404
from methods import *


@api_view(['DELETE'])
def assigneeView(request, assignee_id):
    try:
        assignee = Assignees.objects.get(id=assignee_id)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    assignee.delete()
    return Response(status=status.HTTP_200_OK)
