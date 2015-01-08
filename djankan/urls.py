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

from django.conf.urls import patterns, include, url
from kanban import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

def idof(objectName):
    return r'(?P<'+objectName+r'_id>[0-9]+)/'

v1Prefix = r'^api/v1/'

users = v1Prefix+'users/'
boards = v1Prefix+'boards/'
milestones = boards+idof('board')+'milestones/'
buckets = boards+idof('board')+'buckets/'
lanes = boards+idof('board')+'lanes/'
cards = boards+idof('board')+'cards/'
card = v1Prefix+'card/'+idof('card')
checklists = card+'checklists/'
assignees = card+'assignees/'
assignee = v1Prefix+'assignee/'+idof('assignee')
lane = v1Prefix+'lane/'+idof('lane')
bucket = v1Prefix+'bucket/'+idof('bucket')
milestone = v1Prefix+'milestone/'+idof('milestone')

urlpatterns = patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(users+'$',views.userAPIView),
    url(users+'profile/$',views.userProfileAPIView),
    url(boards+'$',views.boardAPIView),
    url(boards+idof('board')+'$',views.boardIDView),
    url(boards+idof('board')+'roles/$',views.boardRolesView),
    url(boards+idof('board')+'roles/'+idof('role')+'$',views.boardRolesIDView),
    url(milestones+'$',views.boardMilestonesView),
    url(milestones+idof('milestone')+'$',views.boardMilestoneIDView),
    url(milestones+idof('milestone')+'cards/$',views.boardMilestoneCardView),
    url(buckets+'$',views.boardBucketsView),
    url(buckets+idof('bucket')+'$',views.boardBucketIDView),
    url(buckets+idof('bucket')+'cards/$',views.boardBucketCardView),
    url(lanes+'$',views.boardLanesView),
    url(lanes+idof('lane')+'$',views.boardLaneIDView),
    url(lanes+idof('lane')+'cards/$',views.boardLaneCardView),
    url(checklists+'$',views.cardChecklistsView),
    url(assignees+'$',views.cardAssigneesView),
    url(cards+'$',views.boardCardAPIView),
    url(card+'$',views.cardAPIView),
    url(assignee+'$',views.assigneeView),
    url(lane+'$',views.laneView),
    url(bucket+'$',views.bucketView),
    url(milestone+'$',views.milestoneView),
)
