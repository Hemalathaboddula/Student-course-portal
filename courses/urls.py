from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('enroll/<int:course_id>/', views.enroll, name='enroll'),
    path('my-courses/', views.my_courses, name='my_courses'),

    path('signup/', views.signup_view, name='signup'),
    path('forgot/', views.forgot_password_view, name='forgot'),
]
