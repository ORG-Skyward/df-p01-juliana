from django.contrib import admin
from django.urls import path
from mi_app.views import index

urlpatterns = [
    path('admin/', admin.site.admin_view if hasattr(admin.site, 'admin_view') else admin.site.urls),
    path('', index, name='index'),
]
 