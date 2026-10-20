from django.shortcuts import render
from .models import HistorialCalculadora
from datetime import datetime
import os

# Intentamos importar pymongo de forma segura para MongoDB
try:
    from pymongo import MongoClient
    mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
    client = MongoClient(mongo_uri, serverSelectionTimeoutMS=2000)
    db_mongo = client['df_p01_mongo']
    coleccion_mongo = db_mongo['historial_calculadora']
except Exception as e:
    coleccion_mongo = None

def index(request):
    resultado = None
    operacion_str = ""
    usuario_nombre = "Anónimo"

    if request.method == 'POST':
        # Capturamos el nombre de usuario y los datos del cálculo
        usuario_nombre = request.POST.get('usuario', 'Anónimo').strip() or 'Anónimo'
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        operador = request.POST.get('operador')

        if num1 and num2 and operador:
            try:
                n1 = float(num1)
                n2 = float(num2)
                
                if operador == '+':
                    res = n1 + n2
                elif operador == '-':
                    res = n1 - n2
                elif operador == '*':
                    res = n1 * n2
                elif operador == '/':
                    res = n1 / n2 if n2 != 0 else "Error (División por 0)"
                else:
                    res = "Operador no válido"

                resultado = res
                operacion_str = f"{num1} {operador} {num2}"

                # 1. Guardar en PostgreSQL / MySQL (Relacional)
                nuevo_registro = HistorialCalculadora.objects.create(
                    usuario=usuario_nombre,
                    operacion=operacion_str,
                    resultado=str(resultado)
                )

                # 2. Guardar en MongoDB (NoSQL Documental)
                if coleccion_mongo is not None:
                    try:
                        coleccion_mongo.insert_one({
                            "usuario": usuario_nombre,
                            "operacion": operacion_str,
                            "resultado": str(resultado),
                            "fecha": datetime.now()
                        })
                    except Exception as mongo_err:
                        print(f"Nota: MongoDB local no conectado o fuera de línea ({mongo_err})")

            except ValueError:
                resultado = "Error de entrada"

    # Obtener el historial de las últimas 5 operaciones desde PostgreSQL / MySQL
    historial = HistorialCalculadora.objects.all()[:5]

    context = {
        'resultado': resultado,
        'operacion': operacion_str,
        'usuario': usuario_nombre,
        'historial': historial,
    }
    return render(request, 'mi_app/index.html', context)
