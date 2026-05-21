from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    faculty_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    course_link = models.URLField(blank=True)

    # ✅ New fields
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    rating = models.FloatField(default=4.0)

    def __str__(self):
        return self.course_name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return self.user.username