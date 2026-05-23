from django.contrib import admin
from django.urls import path, include
from courses import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    #  default page → login
    path('', views.login_view),

    #  app routes
    path('', include('courses.urls')),

    # monitoring endpoint
    path('', include('django_prometheus.urls')),
]

# media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)