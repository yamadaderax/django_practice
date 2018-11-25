from django.contrib import admin

from .models import Memo
# Register your models here.
class MemoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_datetime', 'update_datetime')
    list_display_link = ('id', 'title')


admin.site.register(Memo, MemoAdmin)
