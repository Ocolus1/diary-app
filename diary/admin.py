from django.contrib import admin

from .models import Diary

class DiaryAdmin(admin.ModelAdmin):
    model = Diary
    exclude = ['message']
    list_display = ["user"]


admin.site.register(Diary, DiaryAdmin)
