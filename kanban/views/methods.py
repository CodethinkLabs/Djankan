from rest_framework import status
from rest_framework.response import Response
from kanban.models import *
from kanban.serializers import *
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist


def serializer_of(Class):
    serializer_tuples = [
        (User, UserSerializer),
        (Board, BoardSerializer),
        (Lane, LaneSerializer),
        (Milestone, MilestoneSerializer),
        (Bucket, BucketSerializer),
        (Card, CardInSerializer), #serializer for POST and PUT not GET
        (Checklist, ChecklistSerializer),
        (TickEvent, TickEventSerializer),
        (Assignees, AssigneesSerializer),
        (Permissions, PermissionsSerializer),
    ]

    serializer = [item[1] for item in serializer_tuples if Class in item]
    return serializer[0]


def post_method(request, Class):
    serializer_name = serializer_of(Class)
    serializer = serializer_name(data=request.DATA)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_all_method(request, Class):
    serializer_name = serializer_of(Class)
    try:
        instances = Class.objects.all()
    except ObjectDoesNotExist:
        content = {'error': 'No matching data'}
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    serializer = serializer_name(instances, many=True)
    return Response(serializer.data)


def get_one_method(request, Class, id):
    serializer_name = serializer_of(Class)
    try:
        instance = Class.objects.get(id=id)
    except ObjectDoesNotExist:
        content = {'error': 'No matching data'}
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    serializer = serializer_name(instance)
    return Response(serializer.data)


def get_filter_method(request, Class, field, filterby):
    serializer_name = serializer_of(Class)
    filter_dict = {field: filterby}
    try:
        instances = Class.objects.filter(**filter_dict)
    except ObjectDoesNotExist:
        content = {'error': 'No matching data'}
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    serializer = serializer_name(instances, many=True)
    return Response(serializer.data)


def put_method(request, Class, id):
    serializer_name = serializer_of(Class)
    try:
        instance = Class.objects.get(id=id)
    except ObjectDoesNotExist:
        content = {'error': 'No matching data'}
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    serializer = serializer_name(instance, data=request.DATA)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
