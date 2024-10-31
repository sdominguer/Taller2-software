import os

pokeneas = [
    {
        "id": 1,
        "nombre": "Pokenea1",
        "altura": "1.2m",
        "habilidad": "Fuego",
        "imagen": "https://storage.googleapis.com/tu_bucket_publico/pokenea1.png",
        "frase": "La sabiduría está en el fuego."
    },
    {
        "id": 2,
        "nombre": "Pokenea2",
        "altura": "0.9m",
        "habilidad": "Agua",
        "imagen": "https://storage.googleapis.com/tu_bucket_publico/pokenea2.png",
        "frase": "La paciencia fluye como el agua."
    },
    {
        "id": 3,
        "nombre": "Pokenea3",
        "altura": "1.5m",
        "habilidad": "Tierra",
        "imagen": "https://storage.googleapis.com/tu_bucket_publico/pokenea3.png",
        "frase": "La fuerza está en nuestras raíces."
    },
    {
        "id": 4,
        "nombre": "Pokenea4",
        "altura": "1.1m",
        "habilidad": "Viento",
        "imagen": "https://storage.googleapis.com/tu_bucket_publico/pokenea4.png",
        "frase": "Los cambios llegan como una brisa inesperada."
    },
    {
        "id": 5,
        "nombre": "Pokenea5",
        "altura": "1.0m",
        "habilidad": "Rayo",
        "imagen": "https://storage.googleapis.com/tu_bucket_publico/pokenea5.png",
        "frase": "La energía fluye en cada tormenta."
    },
    {
        "id": 6,
        "nombre": "Pokenea6",
        "altura": "1.8m",
        "habilidad": "Hielo",
        "imagen": "https://storage.googleapis.com/tu_bucket_publico/pokenea6.png",
        "frase": "La calma es el poder del hielo."
    },
    {
        "id": 7,
        "nombre": "Pokenea7",
        "altura": "0.8m",
        "habilidad": "Planta",
        "imagen": "https://storage.googleapis.com/tu_bucket_publico/pokenea7.png",
        "frase": "El crecimiento lleva su propio ritmo."
    },
    {
        "id": 8,
        "nombre": "Pokenea8",
        "altura": "1.3m",
        "habilidad": "Oscuridad",
        "imagen": "https://storage.googleapis.com/tu_bucket_publico/pokenea8.png",
        "frase": "El misterio es una fuerza en sí misma."
    },
    {
        "id": 9,
        "nombre": "Pokenea9",
        "altura": "1.7m",
        "habilidad": "Luz",
        "imagen": "https://storage.googleapis.com/tu_bucket_publico/pokenea9.png",
        "frase": "La luz brilla en la oscuridad."
    },
    {
        "id": 10,
        "nombre": "Pokenea10",
        "altura": "1.4m",
        "habilidad": "Veneno",
        "imagen": "https://storage.googleapis.com/tu_bucket_publico/pokenea10.png",
        "frase": "Cada veneno tiene su antídoto."
    }
]

container_id = os.getenv("HOSTNAME", "No_ID")  # ID del contenedor
