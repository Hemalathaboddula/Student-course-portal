from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Course, Student


# LOGIN
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            # Admin → admin panel
            if user.is_staff:
                return redirect('/admin/')

            return redirect('dashboard')

        else:
            return render(request, 'courses/login.html', {'error': 'Invalid credentials'})

    return render(request, 'courses/login.html')


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')


# SIGNUP
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'courses/signup.html', {'error': 'Username exists'})

        User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'courses/signup.html')


# DASHBOARD (only students)
@login_required
def dashboard(request):

    if request.user.is_staff:
        return redirect('/admin/')

    courses = Course.objects.all()

    student, _ = Student.objects.get_or_create(user=request.user)

    return render(request, 'courses/dashboard.html', {
        'courses': courses,
        'enrolled_courses': student.courses.all()
    })


# ENROLL
@login_required
def enroll(request, course_id):

    if request.user.is_staff:
        return redirect('/admin/')

    course = get_object_or_404(Course, id=course_id)
    student, _ = Student.objects.get_or_create(user=request.user)

    if course not in student.courses.all():
        student.courses.add(course)

    return redirect('dashboard')


# MY COURSES
@login_required
def my_courses(request):

    if request.user.is_staff:
        return redirect('/admin/')

    student, _ = Student.objects.get_or_create(user=request.user)

    return render(request, 'courses/my_courses.html', {
        'courses': student.courses.all()
    })
