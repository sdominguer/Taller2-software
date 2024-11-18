import os

pokeneas = [
    {
        "id": 1,
        "nombre": "Pokenea1",
        "altura": "1.2m",
        "habilidad": "Fuego",
        "imagen": "https://storage.googleapis.com/pokenea_bucket1/pokeneafuego.png",
        "frase": "La sabiduría está en el fuego."
    },
    {
        "id": 2,
        "nombre": "Pokenea2",
        "altura": "0.9m",
        "habilidad": "Agua",
        "imagen": "https://storage.googleapis.com/pokenea_bucket1/pkeneaAgua.png",
        "frase": "La paciencia fluye como el agua."
    },
    {
        "id": 3,
        "nombre": "Pokenea3",
        "altura": "1.5m",
        "habilidad": "Tierra",
        "imagen": "https://storage.googleapis.com/pokenea_bucket1/pokeneaTierra.png",
        "frase": "La fuerza está en nuestras raíces."
    },
    {
        "id": 4,
        "nombre": "Pokenea4",
        "altura": "1.1m",
        "habilidad": "Viento",
        "imagen": "https://storage.googleapis.com/pokenea_bucket1/pokeneaViento.png",
        "frase": "Los cambios llegan como una brisa inesperada."
    },
    {
        "id": 5,
        "nombre": "Pokenea5",
        "altura": "1.0m",
        "habilidad": "Rayo",
        "imagen": "https://storage.googleapis.com/pokenea_bucket1/pokeneaRayo.png",
        "frase": "La energía fluye en cada tormenta."
    },
    {
        "id": 6,
        "nombre": "Pokenea6",
        "altura": "1.8m",
        "habilidad": "Hielo",
        "imagen": "https://storage.googleapis.com/pokenea_bucket1/pokeneaHielo.png",
        "frase": "La calma es el poder del hielo."
    },
    {
        "id": 7,
        "nombre": "Pokenea7",
        "altura": "0.8m",
        "habilidad": "Planta",
        "imagen": "https://storage.googleapis.com/pokenea_bucket1/pokenaPlanta.png",
        "frase": "El crecimiento lleva su propio ritmo."
    },
    {
        "id": 8,
        "nombre": "Pokenea8",
        "altura": "1.3m",
        "habilidad": "Oscuridad",
        "imagen": "https://storage.googleapis.com/pokenea_bucket1/pokeneaOscuridad.png",
        "frase": "El misterio es una fuerza en sí misma."
    },
    {
        "id": 9,
        "nombre": "Pokenea9",
        "altura": "1.7m",
        "habilidad": "Luz",
        "imagen": "https://storage.googleapis.com/pokenea_bucket1/pokeneaLuz.png",
        "frase": "La luz brilla en la oscuridad."
    },
    {
        "id": 10,
        "nombre": "Pokenea10",
        "altura": "1.4m",
        "habilidad": "Veneno",
        "imagen": "https://storage.googleapis.com/pokenea_bucket1/pokemonVeneno.png",
        "frase": "Cada veneno tiene su antídoto."
    }
]

container_id = os.getenv("HOSTNAME", "No_ID")
