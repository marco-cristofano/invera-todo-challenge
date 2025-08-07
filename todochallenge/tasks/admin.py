from django.contrib import admin
from tasks.models import Task

from todochallenge.admin import admin_site


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'completed',
        'created_at',
        'updated_at',
        'user'
    )
    list_display_links = ('id', 'title', 'description')
    ordering = ('-created_at', )


admin_site.register(Task, TaskAdmin)
