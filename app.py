from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

HTML_JUEGO = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Juego del Click</title>
    <style>
        body {
            font-family: Arial;
            text-align: center;
            margin-top: 50px;
        }
        button {
            padding: 15px 25px;
            font-size: 20px;
            background: #3498db;
            color: white;
            border: none;
            border-radius: 10px;
            cursor: pointer;
        }
        button:hover { background: #2980b9; }
        h1 { color: #2c3e50; }
    </style>
</head>
<body>

    <h1>Juego del Click</h1>
    <h2>Puntos: <span id="puntos">0</span></h2>

    <button onclick="sumar()">Sumar Punto</button>

    <script>
        async function sumar() {
            const res = await fetch("/sumar");
            const data = await res.json();
            document.getElementById("puntos").innerText = data.puntos;
        }

        async function cargarPuntos() {
            const res = await fetch("/puntos");
            const data = await res.json();
            document.getElementById("puntos").innerText = data.puntos;
        }

        cargarPuntos();
    </script>

</body>
</html>
"""

puntos = 0

@app.route("/")
def home():
    return render_template_string(HTML_JUEGO)

@app.route("/puntos")
def obtener_puntos():
    return jsonify({"puntos": puntos})

@app.route("/sumar")
def sumar_punto():
    global puntos
    puntos += 1
    return jsonify({"puntos": puntos})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
