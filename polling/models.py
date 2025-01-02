from django.db import models
from django.contrib import admin

class Poll(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
# class PollAdmin(admin.ModelAdmin):
#     fields= ('title','score')