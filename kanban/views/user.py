from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from kanban.models import *
from kanban.serializers import *
from django.http import Http404
from methods import *

# WARNING:  this will return everything about the user including passwords
#           the serialiser needs changing so that this does not happen
@api_view(['GET'])
def userAPIView(request):
    if request.method == 'GET':
        return get_all_method(request, User)
