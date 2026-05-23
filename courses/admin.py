from django.contrib import admin
from .models import Course, Student


class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'faculty_name', 'duration', 'rating', 'category')

    # NO IMAGE FIELD HERE
    fields = (
        'course_name',
        'faculty_name',
        'duration',
        'course_link',
        'rating',
        'category'
    )


class StudentAdmin(admin.ModelAdmin):
    list_display = ('user',)
    filter_horizontal = ('courses',)


admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)