import os

output_dir = os.path.join("public", "django")
os.makedirs(output_dir, exist_ok=True)

# Simulación de renderizado de la vista de Django
from mi_app.views import calculadora_view
from django.test import RequestFactory

rf = RequestFactory()
request = rf.get('/django/')
response = calculadora_view(request)

with open(os.path.join(output_dir, "index.html"), "wb") as f:
    f.write(response.content)

print("¡Página de Django empaquetada con éxito en public/django/index.html!")

