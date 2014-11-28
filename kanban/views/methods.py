#The MIT License (MIT)

#Copyright (c) 2014 Codethink Ltd.

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
