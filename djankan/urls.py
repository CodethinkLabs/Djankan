from django.conf.urls import patterns, include, url
from kanban import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

def idof(objectName):
    return r'(?P<'+objectName+r'_id>.+?)/'

v1Prefix = r'^api/v1/'

users = v1Prefix+'users/'
boards = v1Prefix+'boards/'
milestones = boards+idof('board')+'milestones/'
buckets = boards+idof('board')+'buckets/'
lanes = boards+idof('board')+'lanes/'
cards = boards+idof('board')+'cards/'
checklist = cards+idof('board')+'checklist/'

urlpatterns = patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

"""    
    url(users+'$',)
    url(users+idof('user')+'$',),
    url(users+idof('user')+'kanbans/$',),
    url(users+idof('user')+'cards/$',),
"""
    url(boards+'$',views.boardAPIView),
"""
    url(boards+idof('board')+'$',),
    url(boards+idof('board')+'archive/$',),
    url(boards+idof('board')+'creationDate/$',),
    url(boards+idof('board')+'roles/$',),

    url(milestones+'$',),
    url(milestones+idof('milestone')+'$',),
    url(milestones+idof('milestone')+'cards/$',),

    url(buckets+'$',),
    url(buckets+idof('bucket')+'$',),
    url(buckets+idof('bucket')+'cards/$',),

    url(lanes+'$',),
    url(lanes+idof('lane')+'$',),
    url(lanes+idof('lane')+'position/$',),
    url(lanes+idof('lane')+'showInTriage/$',),
    url(lanes+idof('lane')+'showInKanban/$',),

    url(cards+'$',),
    url(cards+idof('card')+'$',),
    url(cards+idof('card')+'milestone/$',),
    url(cards+idof('card')+'bucket/$',),
    url(cards+idof('card')+'archive/$',),
    url(cards+idof('card')+'changeLane/$',),
    url(cards+idof('card')+'asignees/$',),
    url(cards+idof('card')+'asignees/'+idof('asignee')+'$',),

    url(checklist+'$',),
    url(checklist+idof('checklist')+'$',),
    url(checklist+idof('checklist')+'tick/$',),
"""
)
