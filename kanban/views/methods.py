from rest_framework import status
from rest_framework.response import Response
from kanban.models import *
from kanban.serializers import *
from django.http import Http404

# find which serializer to use
def serializer_of(Class):
    serializer_tuples = [ 
        (Board,BoardSerializer),
        (Lane,LaneSerializer),
        (Milestone,MilestoneSerializer),
        (Bucket,BucketSerializer),
        (Card,CardSerializer),
        (Checklist,ChecklistSerializer),
        (TickEvent,TickEventSerializer),
        (Assignees,AssigneesSerializer),
        (Permissions,PermissionsSerializer),
    ]
    
    a = [item[1] for item in serializer_tuples if Class in item]
    return a[0]

def post_method(request,Class): 
    serializer_name = serializer_of(Class)
    serializer = serializer_name(data=request.DATA)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_all_method(request,Class):
    serializer_name = serializer_of(Class)
    q = Class.objects.all()
    serializer = serializer_name(q,many=True)
    return Response(serializer.data)

def get_one_method(request,Class,id):
    serializer_name = serializer_of(Class)
    q = Class.objects.get(id=id)
    serializer = serializer_name(q)
    return Response(serializer.data)

def get_filter_method(request,Class,field,filterby):
    serializer_name = serializer_of(Class)
    filter_dict = {field: filterby}
    q = Class.objects.filter(**filter_dict)
    serializer = serializer_name(q,many=True)
    return Response(serializer.data)

def put_method(request,Class,id):
    serializer_name = serializer_of(Class)
    q = Class.objects.get(id=id)
    serializer = serializer_name(q,data=request.DATA)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
