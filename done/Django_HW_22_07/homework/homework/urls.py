from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("task_01/", include("task_01.urls")),
    path('task_02/', include('task_02.urls')),
    path('task_03/', include('task_03.urls')),
    path("task_04/", include("task_04.urls")),
    path("task_05/", include("task_05.urls")),


]