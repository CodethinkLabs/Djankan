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
        try:
            board = Board.objects.get(id=board_id)
            lanes = board.lane_set.all()
            cards = Card.objects.filter(lane_id=lanes)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        return post_method(request, Card)


@api_view(['GET', 'PUT'])
def cardAPIView(request, card_id):
    if request.method == 'GET':
        return get_one_method(request, Card, card_id)
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
