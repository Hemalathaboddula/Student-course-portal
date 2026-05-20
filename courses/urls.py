from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('dashboard/', views.dashboard),
    path('courses/', views.courses_list),
    path('add/', views.add_course),
    path('delete/<int:course_id>/', views.delete_course),
    path('update/<int:course_id>/', views.update_course),
]
