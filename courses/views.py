from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
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


# ✅ DASHBOARD
@login_required
def dashboard(request):
    query = request.GET.get('q')

    if query:
        courses = Course.objects.filter(course_name__icontains=query)
    else:
        courses = Course.objects.all()

    student, _ = Student.objects.get_or_create(user=request.user)
    enrolled_courses = student.courses.all()

    return render(request, 'courses/dashboard.html', {
        'courses': courses,
        'enrolled_courses': enrolled_courses
    })


# ✅ COURSE LIST (ADMIN VIEW)
@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/courses.html', {'courses': courses})


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
        return redirect('courses')

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
        return redirect('courses')

    return render(request, 'courses/edit_course.html', {'course': course})


# ✅ DELETE COURSE
@login_required
def delete_course(request, id):
    course = get_object_or_404(Course, id=id)
    course.delete()
    return redirect('courses')


# ✅ ENROLL COURSE
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
    if request.user.is_staff:
        return redirect('courses')

    student, _ = Student.objects.get_or_create(user=request.user)
    courses = student.courses.all()

    return render(request, 'courses/my_courses.html', {'courses': courses})