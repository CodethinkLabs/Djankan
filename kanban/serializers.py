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

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from kanban.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email')

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board

class LaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lane

class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone

class BucketSerializer(serializers.ModelSerializer):
    class Meta:
            model = Bucket

class CardHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardHeader
        fields = ('cardNumber', 'createDate', 'creator')

# serializer adds board field when client gets card
class CardOutSerializer(serializers.ModelSerializer):
    header = CardHeaderSerializer(source='header')
    board = serializers.SerializerMethodField('getBoard')

    class Meta:
        model = Card
        fields = ('id','header','board','lane', 'milestone',
        'bucket', 'title', 'description', 'dueDate',
        'timeEstimate', 'result', 'modifiedDate', 'archived',
        'position', 'lastUser', 'supersededBy')

    def getBoard(self,obj):
        return obj.lane.board.id;

# remove the board field when client puts or posts card - this should
# not be in the model because it leaves it open in inconsitency if the
# lane does not belong to the board the card belongs to
class CardInSerializer(serializers.ModelSerializer):
    header = CardHeaderSerializer(source='header')

    class Meta:
        model = Card
        fields = ('id','header','lane', 'milestone',
        'bucket', 'title', 'description', 'dueDate',
        'timeEstimate', 'result', 'modifiedDate', 'archived',
        'position', 'lastUser', 'supersededBy')

class ChecklistSerializer(serializers.ModelSerializer):
    class Meta:
            model = Checklist

class TickEventSerializer(serializers.ModelSerializer):
    class Meta:
            model = TickEvent

class AssigneesSerializer(serializers.ModelSerializer):
    class Meta:
            model = Assignees

class PermissionsSerializer(serializers.ModelSerializer):
    class Meta:
            model = Permissions
