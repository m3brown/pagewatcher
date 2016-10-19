from __future__ import unicode_literals

from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=50, unique=True)
    url = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return self.title

class Watch(models.Model):
    email = models.CharField(max_length=120)
    page = models.ForeignKey(Page)
    triggered = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s - %s" % (self.email, self.page.title)
