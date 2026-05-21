from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('add/', views.add_course),
    path('edit/<int:id>/', views.edit_course, name='edit_course'),
    path('delete/<int:id>/', views.delete_course, name='delete_course'),

    path('enroll/<int:course_id>/', views.enroll, name='enroll'),
    path('my-courses/', views.my_courses, name='my_courses'),

    path('signup/', views.signup_view, name='signup'),
    path('forgot/', views.forgot_password_view, name='forgot'),
]