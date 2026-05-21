from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from courses import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ Default route → login page
    path('', include('courses.urls')),

    # ✅ optional explicit root
    path('', include('courses.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# from courses import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.login_view),   # ✅ FIXED root
    path('', include('courses.urls')),
]