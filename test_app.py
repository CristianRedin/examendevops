from app import app

def test_home():
    cliente = app.test_client()
    respuesta = cliente.get("/")
    assert respuesta.status_code == 200
    assert b"Juego del Click" in respuesta.data

def test_puntos():
    cliente = app.test_client()
    respuesta = cliente.get("/puntos")
    assert respuesta.status_code == 200
    assert b"puntos" in respuesta.data

def test_sumar():
    cliente = app.test_client()
    respuesta = cliente.get("/sumar")
    assert respuesta.status_code == 200
    assert b"puntos" in respuesta.data
