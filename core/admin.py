from django.contrib import admin
from core.models import Watch, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')

admin.site.register(Page, PageAdmin)

class WatchAdmin(admin.ModelAdmin):
    list_display = ('email', 'page')

admin.site.register(Watch, WatchAdmin)
