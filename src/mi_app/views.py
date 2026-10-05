from django.http import HttpResponse

def calculadora_view(request):
    html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora en Django</title>
    <style>
        * { box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #09203f 0%, #537895 100%);
            min-height: 100vh;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #333;
        }
        .card {
            background: white;
            padding: 2.5rem;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            text-align: center;
            max-width: 420px;
            width: 90%;
        }
        h1 { color: #09203f; margin-bottom: 1.5rem; }
        .input-group { display: flex; flex-direction: column; gap: 1rem; margin-bottom: 1.5rem; }
        input[type="number"] {
            width: 100%; padding: 0.8rem; font-size: 1.1rem;
            border: 2px solid #cbd5e0; border-radius: 8px; outline: none; text-align: center;
        }
        .button-group { display: flex; gap: 0.5rem; margin-bottom: 1rem; }
        button {
            flex: 1; padding: 0.9rem; font-size: 1rem; font-weight: bold;
            color: white; border: none; border-radius: 8px; cursor: pointer;
        }
        .btn-calc { background-color: #09203f; }
        .btn-rand { background-color: #38a169; }
        .result-container { margin-top: 1.5rem; }
        .result {
            font-size: 2.5rem; font-weight: bold; color: #09203f;
            background: #e2e8f0; padding: 1rem; border-radius: 10px;
        }
        .nav-link { display: block; margin-top: 1.5rem; color: #537895; font-weight: bold; text-decoration: none; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Calculadora (Django App)</h1>
        <div class="input-group">
            <input type="number" id="num1" placeholder="Primer número" value="0">
            <input type="number" id="num2" placeholder="Segundo número" value="0">
        </div>
        <div class="button-group">
            <button class="btn-calc" onclick="realizarSuma()">Calcular</button>
            <button class="btn-rand" onclick="generarAleatorios()">Aleatorios</button>
        </div>
        <div class="result-container">
            <div>Resultado:</div>
            <div class="result" id="resultado">0</div>
        </div>
        <a class="nav-link" href="../index.html">← Volver a la Calculadora Principal</a>
    </div>

    <script>
        function realizarSuma() {
            const v1 = parseFloat(document.getElementById('num1').value) || 0;
            const v2 = parseFloat(document.getElementById('num2').value) || 0;
            document.getElementById('resultado').textContent = v1 + v2;
        }
        function generarAleatorios() {
            document.getElementById('num1').value = Math.floor(Math.random() * 100) + 1;
            document.getElementById('num2').value = Math.floor(Math.random() * 100) + 1;
            realizarSuma();
        }
        document.getElementById('num1').addEventListener('input', realizarSuma);
        document.getElementById('num2').addEventListener('input', realizarSuma);
    </script>
</body>
</html>"""
    return HttpResponse(html_content)

