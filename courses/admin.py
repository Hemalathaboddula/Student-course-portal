from django.contrib import admin
from .models import Course, Student


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'faculty_name', 'duration', 'rating')
    search_fields = ('course_name', 'faculty_name')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user',)
    filter_horizontal = ('courses',)

    # ✅ Enable mass deletion
    actions = ['delete_selected']


# ✅ Add default delete action
admin.site.add_action(admin.actions.delete_selected)