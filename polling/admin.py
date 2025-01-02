from django.contrib import admin
from polling.models import Poll,PollAdmin

admin.site.register(Poll,PollAdmin)