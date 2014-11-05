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

class CardSerializer(serializers.ModelSerializer):
    header = CardHeaderSerializer(source='header')

    class Meta:
        model = Card
        fields = ('id','header', 'lane', 'milestone',
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
