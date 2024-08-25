from django.contrib import admin
from .models import Todo
from .models import Schedule

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date')
# Register your models here.

admin.site.register(Todo, TodoAdmin)
admin.site.register(Schedule, ScheduleAdmin)