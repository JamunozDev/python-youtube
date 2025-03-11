#!/usr/bin/python3
import sys
import signal
import os
import requests


def def_handler(sig, frame):  # pylint: disable=unused-argument
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)


# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

# Variables globales
API_KEY = "AIzaSyAEgTD5z1HJNimTYiAo_YJh-XfXrLVfpww"
if not API_KEY:
    raise ValueError(
        "La clave API de YouTube no está configurada en las variables de entorno."
    )
URL_YOUTUBE = "https://www.googleapis.com/youtube/v3/search"


def inicia_poc_youtube():
    print("Iniciando prueba")
    query = "vscode spring boot extensiones"
    data = {
        "key": API_KEY,
        "part": "id,snippet",
        "q": query,
        "max_results": 20,
        "relevanceLanguage": "es",
    }
    try:
        r = requests.get(URL_YOUTUBE, params=data, timeout=20)
        r.raise_for_status()  # Esto lanzará una excepción para códigos de estado HTTP 4xx/5xx
        j = r.json()
        # Construir y retornar lista simplificada
        resultados = [(v["id"]["videoId"], v["snippet"]["title"]) for v in j["items"]]
        print("\n".join("   ".join(data) for data in resultados))
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud HTTP: {e}")
        return []

    return resultados


if __name__ == "__main__":
    inicia_poc_youtube()
