import os
import sys

# Asegurar que el directorio actual esté en el PATH de Python
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Importar y configurar Django
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_proyecto.settings')
django.setup()

# Crear la carpeta public/django en la raíz del proyecto
ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
output_dir = os.path.join(ruta_raiz, "public", "django")
os.makedirs(output_dir, exist_ok=True)

# Simulación de renderizado de la vista de Django
from mi_app.views import calculadora_view
from django.test import RequestFactory

rf = RequestFactory()
request = rf.get('/django/')
response = calculadora_view(request)

# Guardar el index.html en public/django/
with open(os.path.join(output_dir, "index.html"), "wb") as f:
    f.write(response.content)

print("¡Página de Django empaquetada con éxito en public/django/index.html!")
 