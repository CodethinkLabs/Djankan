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


def get_by_board(request, Class, board_id):
    return get_filter_method(request, Class, 'board', board_id)


@api_view(['POST', 'GET'])
def boardAPIView(request):
    if request.method == 'POST':
        return post_method(request, Board)
    elif request.method == 'GET':
        return get_all_method(request, Board)


@api_view(['GET', 'PUT'])
def boardIDView(request, board_id):
    if request.method == 'GET':
        return get_one_method(request, Board, board_id)
    elif request.method == 'PUT':
        return put_method(request, Board)


@api_view(['GET', 'POST'])
def boardRolesView(request, board_id):
    if request.method == 'GET':
        return get_by_board(request, Permissions, board_id)
    elif request.method == 'POST':
        return post_method(request, Permissions)


@api_view(['GET', 'PUT'])
def boardRolesIDView(request, board_id, role_id):
    if request.method == 'GET':
        return get_by_board(request, Permissions, board_id)
    elif request.method == 'PUT':
        return put_method(request, Permissions, role_id)


@api_view(['GET', 'POST'])
def boardMilestonesView(request, board_id):
    if request.method == 'GET':
        return get_by_board(request, Milestone, board_id)
    elif request.method == 'POST':
        return post_method(request, Milestone)


@api_view(['GET', 'PUT'])
def boardMilestoneIDView(request, board_id, milestone_id):
    if request.method == 'GET':
        return get_one_method(request, Milestone, milestone_id)
    elif request.method == 'PUT':
        return put_method(request, Milestone, milestone_id)


@api_view(['GET'])
def boardMilestoneCardView(request, board_id, milestone_id):
    if request.method == 'GET':
        return get_filter_method(request, Card, 'milestone', milestone_id)


@api_view(['GET', 'POST'])
def boardBucketsView(request, board_id):
    if request.method == 'GET':
        return get_by_board(request, Bucket, board_id)
    elif request.method == 'POST':
        return post_method(request, Bucket)


@api_view(['GET', 'PUT'])
def boardBucketIDView(request, board_id, bucket_id):
    if request.method == 'GET':
        return get_one_method(request, Bucket, bucket_id)
    if request.method == 'PUT':
        return put_method(request, Bucket, bucket_id)


@api_view(['GET'])
def boardBucketCardView(request, board_id, bucket_id):
    if request.method == 'GET':
        return get_filter_method(request, Card, 'bucket', bucket_id)


@api_view(['GET', 'POST'])
def boardLanesView(request, board_id):
    if request.method == 'GET':
        return get_by_board(request, Lane, board_id)
    elif request.method == 'POST':
        return post_method(request, Lane)


@api_view(['GET', 'PUT'])
def boardLaneIDView(request, board_id, lane_id):
    if request.method == 'GET':
        return get_one_method(request, Lane, lane_id)
    elif request.method == 'PUT':
        return put_method(request, Lane, lane_id)


@api_view(['GET'])
def boardLaneCardView(request, board_id, lane_id):
    if request.method == 'GET':
        return get_filter_method(request, Card, 'lane', lane_id)
