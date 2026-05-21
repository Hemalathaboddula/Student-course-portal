from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Course, Student


# ✅ LOGIN
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'courses/login.html', {'error': 'Invalid credentials'})

    return render(request, 'courses/login.html')


# ✅ LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')


# ✅ SIGNUP
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'courses/signup.html', {'error': 'Username already exists'})

        User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'courses/signup.html')


# ✅ FORGOT PASSWORD
def forgot_password_view(request):
    return render(request, 'courses/forgot.html')


# ✅ DASHBOARD
@login_required
def dashboard(request):
    courses = Course.objects.all()

    student, _ = Student.objects.get_or_create(user=request.user)
    enrolled_courses = student.courses.all()

    return render(request, 'courses/dashboard.html', {
        'courses': courses,
        'enrolled_courses': enrolled_courses
    })


# ✅ ADD COURSE
@login_required
def add_course(request):
    if request.method == 'POST':
        Course.objects.create(
            course_name=request.POST.get('course_name'),
            faculty_name=request.POST.get('faculty_name'),
            duration=request.POST.get('duration'),
            course_link=request.POST.get('course_link')
        )
        return redirect('dashboard')

    return render(request, 'courses/add_course.html')


# ✅ EDIT COURSE
@login_required
def edit_course(request, id):
    course = get_object_or_404(Course, id=id)

    if request.method == 'POST':
        course.course_name = request.POST.get('course_name')
        course.faculty_name = request.POST.get('faculty_name')
        course.duration = request.POST.get('duration')
        course.course_link = request.POST.get('course_link')
        course.save()

        return redirect('dashboard')

    return render(request, 'courses/edit_course.html', {'course': course})


# ✅ DELETE COURSE
@login_required
def delete_course(request, id):
    course = get_object_or_404(Course, id=id)
    course.delete()
    return redirect('dashboard')


# ✅ ENROLL
@login_required
def enroll(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    student, _ = Student.objects.get_or_create(user=request.user)

    if course not in student.courses.all():
        student.courses.add(course)

    return redirect('dashboard')


# ✅ MY COURSES
@login_required
def my_courses(request):
    student, _ = Student.objects.get_or_create(user=request.user)
    courses = student.courses.all()

    return render(request, 'courses/my_courses.html', {'courses': courses})