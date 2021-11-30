from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('todo_fm.urls')),
    path('api/', include('product_feedback_fm.urls')),
    path('api/', include('user.urls')),
    path('admin/', admin.site.urls),
]
