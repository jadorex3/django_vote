from django.contrib import admin
from .models import Poll, Person, Vote


class VoteInline(admin.TabularInline):
    model = Vote
    extra = 1
    exclude = ('vote', )


class PollAdmin(admin.ModelAdmin):
    inlines = (VoteInline, )


class PersonAdmin(admin.ModelAdmin):
    inlines = (VoteInline, )


admin.site.register(Poll, PollAdmin)
admin.site.register(Person, PersonAdmin)

