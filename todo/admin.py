from django.contrib import admin
from .models import Todo


class Todoreader(admin.ModelAdmin):
    readonly_fields = ('datecreated', )


admin.site.register(Todo, Todoreader)
