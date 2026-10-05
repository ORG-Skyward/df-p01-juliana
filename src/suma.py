import os

def sumar(a, b):
    return a + b

if __name__ == "__main__":
    num1 = 8
    num2 = 7
    resultado = sumar(num1, num2)
    
    # Crear la carpeta public si no existe
    os.makedirs("public", exist_ok=True)
    
    # Generar el archivo index.html dentro de public/
    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora de Suma</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            height: 100vh;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #333;
        }}
        .card {{
            background: white;
            padding: 2.5rem;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            text-align: center;
            max-width: 400px;
            width: 90%;
        }}
        h1 {{
            color: #4a5568;
            margin-bottom: 1.5rem;
            font-size: 1.8rem;
        }}
        .operation {{
            font-size: 1.2rem;
            color: #718096;
            margin-bottom: 1rem;
        }}
        .result {{
            font-size: 3rem;
            font-weight: bold;
            color: #5a67d8;
            background: #ebf8ff;
            padding: 1rem;
            border-radius: 10px;
            border: 2px dashed #90cdf4;
        }}
    </style>
</head>
<body>
    <div class="card">
        <h1>Resultado de la Suma</h1>
        <div class="operation">{num1} + {num2}</div>
        <div class="result">{resultado}</div>
    </div>
</body>
</html>
"""
    
    with open("public/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print("¡Página web generada con éxito en public/index.html!")
    