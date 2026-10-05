from django.contrib import admin
from django.urls import path
from mi_app.views import calculadora_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', calculadora_view, name='calculadora'),
]