from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

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

class CardSerializer(serializers.ModelSerializer):
    class Meta:
            model = Card

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
