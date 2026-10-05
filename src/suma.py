import os

if __name__ == "__main__":
    os.makedirs("public", exist_ok=True)
    
    html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora Principal</title>
    <style>
        * { box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
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
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            text-align: center;
            max-width: 450px;
            width: 90%;
        }
        h1 { color: #4a5568; margin-bottom: 1.5rem; }
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
        .btn-calc { background-color: #5a67d8; }
        .btn-rand { background-color: #38a169; }
        .result-container { margin-top: 1.5rem; }
        .result {
            font-size: 2.5rem; font-weight: bold; color: #2b6cb0;
            background: #ebf8ff; padding: 1rem; border-radius: 10px; border: 2px dashed #90cdf4;
        }
        .links-box {
            margin-top: 2rem;
            padding-top: 1rem;
            border-top: 1px solid #e2e8f0;
            display: flex;
            justify-content: space-around;
        }
        .link-btn {
            color: #5a67d8;
            font-weight: bold;
            text-decoration: none;
            padding: 0.5rem 1rem;
            border: 1px solid #5a67d8;
            border-radius: 6px;
        }
        .link-btn:hover { background: #ebf8ff; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Calculadora de Suma</h1>
        <div class="input-group">
            <input type="number" id="num1" placeholder="Ingresa el primer número" value="0">
            <input type="number" id="num2" placeholder="Ingresa el segundo número" value="0">
        </div>
        <div class="button-group">
            <button class="btn-calc" onclick="realizarSuma()">Calcular Suma</button>
            <button class="btn-rand" onclick="generarAleatorios()">Números Aleatorios</button>
        </div>
        <div class="result-container">
            <div>Resultado:</div>
            <div class="result" id="resultado">0</div>
        </div>

        <!-- Panel con los DOS Enlaces requeridos -->
        <div class="links-box">
            <a class="link-btn" href="./index.html">🔗 Enlace 1: Calculadora Base</a>
            <a class="link-btn" href="./django/index.html">🚀 Enlace 2: Módulo Django</a>
        </div>
    </div>

    <script>
        function realizarSuma() {
            const val1 = parseFloat(document.getElementById('num1').value) || 0;
            const val2 = parseFloat(document.getElementById('num2').value) || 0;
            document.getElementById('resultado').textContent = val1 + val2;
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
</html>
"""
    with open("public/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
         