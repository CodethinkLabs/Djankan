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
from rest_framework.decorators import api_view
from rest_framework.response import Response
from kanban.models import *
from kanban.serializers import *
from django.http import Http404
from methods import *


@api_view(['GET', 'PUT','DELETE'])
def laneView(request, lane_id):
    if request.method == 'GET':
        return get_one_method(request, Lane, lane_id)
    elif request.method == 'PUT':
        return put_method(request, Lane, lane_id)
    elif request.method == 'DELETE':
        try:
            lane = Lane.objects.get(id=lane_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # if can't find any cards in this lane delete else 400
        cards_in_lane = Card.objects.filter(lane=lane_id)
        if cards_in_lane:
            return Response(status=status.HTTP_403_FORBIDDEN)
        lane.delete()
        return Response(status=status.HTTP_200_OK)
