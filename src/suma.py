import os

if __name__ == "__main__":
    # Crear la carpeta public si no existe
    os.makedirs("public", exist_ok=True)
    
    # Generar el archivo index.html con inputs e interactividad
    html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora Interactiva de Suma</title>
    <style>
        * {
            box-sizing: border-box;
        }
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
            max-width: 420px;
            width: 90%;
        }
        h1 {
            color: #4a5568;
            margin-bottom: 1.5rem;
            font-size: 1.8rem;
        }
        .input-group {
            display: flex;
            flex-direction: column;
            gap: 1rem;
            margin-bottom: 1.5rem;
        }
        input[type="number"] {
            width: 100%;
            padding: 0.8rem;
            font-size: 1.1rem;
            border: 2px solid #cbd5e0;
            border-radius: 8px;
            outline: none;
            text-align: center;
            transition: border-color 0.2s;
        }
        input[type="number"]:focus {
            border-color: #667eea;
        }
        .button-group {
            display: flex;
            gap: 0.5rem;
            margin-bottom: 1rem;
        }
        button {
            flex: 1;
            padding: 0.9rem;
            font-size: 1rem;
            font-weight: bold;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.2s, transform 0.1s;
        }
        .btn-calc {
            background-color: #5a67d8;
        }
        .btn-calc:hover {
            background-color: #4c51bf;
        }
        .btn-rand {
            background-color: #38a169;
        }
        .btn-rand:hover {
            background-color: #2f855a;
        }
        button:active {
            transform: scale(0.98);
        }
        .result-container {
            margin-top: 1.5rem;
        }
        .result-label {
            font-size: 1rem;
            color: #718096;
            margin-bottom: 0.5rem;
        }
        .result {
            font-size: 2.5rem;
            font-weight: bold;
            color: #2b6cb0;
            background: #ebf8ff;
            padding: 1rem;
            border-radius: 10px;
            border: 2px dashed #90cdf4;
            min-height: 4rem;
            display: flex;
            align-items: center;
            justify-content: center;
        }
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
            <div class="result-label">Resultado:</div>
            <div class="result" id="resultado">0</div>
        </div>
    </div>

    <script>
        function realizarSuma() {
            const val1 = parseFloat(document.getElementById('num1').value) || 0;
            const val2 = parseFloat(document.getElementById('num2').value) || 0;
            const suma = val1 + val2;
            
            document.getElementById('resultado').textContent = suma;
        }

        function generarAleatorios() {
            // Genera dos números aleatorios entre 1 y 100
            const random1 = Math.floor(Math.random() * 100) + 1;
            const random2 = Math.floor(Math.random() * 100) + 1;

            document.getElementById('num1').value = random1;
            document.getElementById('num2').value = random2;

            realizarSuma();
        }

        // Calcula automáticamente la suma conforme escribes los números
        document.getElementById('num1').addEventListener('input', realizarSuma);
        document.getElementById('num2').addEventListener('input', realizarSuma);
    </script>
</body>
</html>
"""
    
    with open("public/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print("¡Página web interactiva y con números aleatorios generada con éxito!")
    