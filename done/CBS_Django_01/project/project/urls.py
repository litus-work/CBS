from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),
    path('contact/', include('contact.urls')),
    path('lesson_1_1/', include('lesson_11.urls')),
    path('about/', include('about.urls'))

]