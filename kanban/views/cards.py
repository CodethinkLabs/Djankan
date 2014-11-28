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
from django.core.exceptions import ObjectDoesNotExist
from methods import *


def get_by_card(request, Class, card_id):
    return get_filter_method(request, Class, 'card', card_id)


@api_view(['POST', 'GET'])
def boardCardAPIView(request, board_id):
    if request.method == 'GET':
        milestone = request.QUERY_PARAMS.get('milestone', None)
        bucket = request.QUERY_PARAMS.get('bucket', None)
        archived_flag = request.QUERY_PARAMS.get('archived', None)
        try:
            board = Board.objects.get(id=board_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        lanes = board.lane_set.all()
        if milestone is not None:
            try:
                cards = Card.objects.filter(lane_id=lanes, milestone_id=milestone)
            except ValueError:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            if not cards:
                return Response(status=status.HTTP_404_NOT_FOUND)
        elif bucket is not None:
            try:
                cards = Card.objects.filter(lane_id=lanes, bucket_id=bucket)
            except ValueError:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            if not cards:
                return Response(status=status.HTTP_404_NOT_FOUND)
        elif archived_flag is not None:
            archived_flag = archived_flag.upper()
            if archived_flag == "FALSE":
                cards = Card.objects.filter(lane_id=lanes, archived=False)
            elif archived_flag == "TRUE":
                cards = Card.objects.filter(lane_id=lanes, archived=True)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            cards = Card.objects.filter(lane_id=lanes)
        serializer = CardOutSerializer(cards, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        return post_method(request, Card)


@api_view(['GET', 'PUT'])
def cardAPIView(request, card_id):
    if request.method == 'GET':
        try:
            instance = Card.objects.get(id=card_id)
        except ObjectDoesNotExist:
            content = {'error': 'No matching data'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        serializer = CardOutSerializer(instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        return put_method(request, Card, card_id)


@api_view(['GET', 'POST'])
def cardAssigneesView(request, card_id):
    if request.method == 'GET':
        return get_by_card(request, Assignees, card_id)
    elif request.method == 'POST':
        return post_method(request, Assignees)


@api_view(['GET', 'POST'])
def cardChecklistsView(request, card_id):
    if request.method == 'GET':
        return get_by_card(request, Checklist, card_id)
    elif request.method == 'POST':
        return post_method(request, Checklist)
