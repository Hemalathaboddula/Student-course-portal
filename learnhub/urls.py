from django.contrib import admin
from django.urls import path, include   # ✅ FIXED HERE

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ Main app URLs
    path('', include('courses.urls')),
]

# ✅ MEDIA FILES (for images)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
