from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username


class Board(models.Model):
    title = models.CharField(max_length=200)
    createDate = models.DateTimeField(auto_now_add=True, default=datetime.now())
    archived = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return self.title


class Lane(models.Model):
    board = models.ForeignKey(Board)
    title = models.CharField(max_length=200)
    cardLimit = models.IntegerField(blank=True, null=True)
    colour = models.CharField(max_length=7)

    # define lane_role options
    LANE_OPTIONS = (
        ('NORM', 'Normal'),
        ('REVI', 'Review'),
        ('DONE', 'Done'),
    )

    lane_role = models.CharField(max_length=4,
                                 choices=LANE_OPTIONS,
                                 default='NORM')

    position = models.PositiveIntegerField()
    inTriageView = models.BooleanField(default=True)
    inKanbanView = models.BooleanField(default=True)
    deletedDate = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title


class Milestone(models.Model):
    board = models.ForeignKey(Board)
    title = models.CharField(max_length=200)
    dueDate = models.DateTimeField('date due')
    colour = models.CharField(max_length=7)
    description = models.TextField()

    def __str__(self):
        return self.title


class Bucket(models.Model):
    board = models.ForeignKey(Board)
    title = models.CharField(max_length=200)
    colour = models.CharField(max_length=7)
    description = models.TextField()

    def __str__(self):
        return self.title

class CardHeader(models.Model):
    cardNumber = models.IntegerField(default=1)
    createDate = models.DateTimeField(auto_now_add=True, default=datetime.now())
    creator = models.ForeignKey(UserProfile)

    def __str__(self):
        return "Card Number: " + str(self.cardNumber)

class Card(models.Model):
    # Foreign key links
    lane = models.ForeignKey(Lane)
    milestone = models.ForeignKey(Milestone, blank=True, null=True)
    bucket = models.ForeignKey(Bucket, blank=True, null=True)
    lastUser = models.ForeignKey(UserProfile, related_name='last_user')
    header = models.ForeignKey(CardHeader)

    title = models.CharField(max_length=200)
    description = models.TextField()
    dueDate = models.DateTimeField('date due')
    timeEstimate = models.IntegerField()
    result = models.TextField(blank=True, null=True)
    modifiedDate = models.DateTimeField(auto_now=True, default=datetime.now())
    archived = models.BooleanField(default=False)
    position = models.PositiveIntegerField()
    supersededBy = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title


class Checklist(models.Model):
    card = models.ForeignKey(Card)
    #cardNumber = models.IntegerField()
    description = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True, default=datetime.now())
    position = models.PositiveIntegerField()
    deletedDate = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class TickEvent(models.Model):
    checklist = models.ForeignKey(Checklist)
    ticked = models.BooleanField(default=False)
    timeStamp = models.DateTimeField('date (un)ticked')
    ticker = models.ForeignKey(UserProfile)


class Assignees(models.Model):
    card = models.ForeignKey(Card)
    person = models.ForeignKey(UserProfile)
    timeAssigned = models.DateTimeField('assignment time')

    ASSIGNEE_ROLE = (
        ('NORM', 'Normal'),
        ('REVI', 'Reviewer'),
    )
    assignee_role = models.CharField(max_length=4,
                                     choices=ASSIGNEE_ROLE,
                                     default='NORM')

    def __str__(self):
        return self.person


class Permissions(models.Model):
    board = models.ForeignKey(Board)
    user = models.ForeignKey(UserProfile)

    USER_ROLE = (
        ('VIEW', 'Viewer'),
        ('EDIT', 'Editor'),
    )

    user_role = models.CharField(max_length=4,
                                 choices=USER_ROLE,
                                 default='VIEW')

    def __str__(self):
        return self.user
