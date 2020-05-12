from django.contrib import admin
from .models import Schedule, Teacher
from django.utils.safestring import mark_safe

# Register your models here.


@admin.register(Schedule)
class SheduleAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher', 'startTime', 'endTime')
    save_as = True


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'name', 'position', 'get_image')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.imageUrl.url} width="100" height="100"')

    get_image.short_description = "Image"
