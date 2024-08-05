from django.contrib import admin
from django.urls import path,re_path

from datavis.views import upload_file ,contact_us
# Correct import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', upload_file, name='upload_file'),
    path('contact_us/', contact_us, name='contact_us'),
]
