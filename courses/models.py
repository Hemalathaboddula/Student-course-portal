from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    faculty_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    course_link = models.URLField()

    rating = models.FloatField(default=4.0)

    CATEGORY_CHOICES = [
        ('python', 'Python'),
        ('aws', 'AWS'),
        ('ai', 'AI'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='python')

    def __str__(self):
        return self.course_name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return self.user.username
