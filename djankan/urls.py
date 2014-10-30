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
checklist = cards+idof('board')+'checklist/'

urlpatterns = patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

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
    url(lanes+idof('lane')+'$',boardLaneIDView),
    url(lanes+idof('lane')+'cards/$',boardLaneCardView),
    url(cards+'$',views.boardCardAPIView),
    url(card+'$',views.cardAPIView),
)
