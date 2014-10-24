from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from kanban.models import *
from kanban.serializers import *
from django.http import Http404

@api_view(['POST', 'GET'])
def cardAPIView(request, board_id):
    if request.method == 'GET':
        board = Board.objects.get(id=board_id)
        lanes = board.lane_set.all()
        cards = Card.objects.filter(lane_id=lanes)
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = CardSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
