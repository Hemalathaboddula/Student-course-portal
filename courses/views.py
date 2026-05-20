from django.shortcuts import render, redirect, get_object_or_404
from .models import Course


def home(request):
    return render(request, 'courses/index.html')


def dashboard(request):
    total_courses = Course.objects.count()
    return render(request, 'courses/dashboard.html', {'total_courses': total_courses})


def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/courses.html', {'courses': courses})


def add_course(request):
    if request.method == "POST":
        Course.objects.create(
            course_name=request.POST['course_name'],
            faculty_name=request.POST['faculty_name'],
            duration=request.POST['duration']
        )
        return redirect('/courses/')
    return render(request, 'courses/add_course.html')


def delete_course(request, course_id):
    Course.objects.filter(id=course_id).delete()
    return redirect('/courses/')


def update_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == "POST":
        course.course_name = request.POST['course_name']
        course.faculty_name = request.POST['faculty_name']
        course.duration = request.POST['duration']
        course.save()
        return redirect('/courses/')

    return render(request, 'courses/update_course.html', {'course': course})
