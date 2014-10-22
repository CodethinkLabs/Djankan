from django.contrib import admin

from kanban.models import *

admin.site.register(UserProfile)
admin.site.register(Board)
admin.site.register(Lane)
admin.site.register(Milestone)
admin.site.register(Bucket)
admin.site.register(Card)
admin.site.register(Checklist)
admin.site.register(TickEvent)
admin.site.register(Assignees)
admin.site.register(Permissions)

# Register your models here.
