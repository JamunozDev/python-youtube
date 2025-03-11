#!/usr/bin/python
import sys
import signal
import os
import requests
import json
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from resultado_toutube_format import RespuestaYouTube
import resultado_youtube

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)

def def_handler(sig, frame):  # pylint: disable=unused-argument
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)


# Ctrl+C
signal.signal(signal.SIGINT, def_handler)


@app.route('/buscar_videos', methods=['POST'])
def procesar_json():
    try:
        # Obtener el JSON en formato clave-valor
        consulta = request.form.get("consulta")  

        if not consulta:
            return jsonify({"error": "El parámetro 'consulta' es obligatorio"}), 400

        # Convertir la cadena JSON a un objeto RespuestaYouTube
        respuesta_youtube = inicia_poc_youtube(consulta)

        # Convertir el objeto de vuelta a JSON
        respuesta_json = respuesta_youtube.to_json()

        # Devolver el JSON como respuesta
        return jsonify(json.loads(respuesta_json)), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    

# Variables globales
API_KEY = os.getenv("YOUTUBE_API_KEY")
if not API_KEY:
    raise ValueError(
        "La clave API de YouTube no está configurada en las variables de entorno."
    )
URL_YOUTUBE = "https://www.googleapis.com/youtube/v3/search"

def from_json(json_string):
    data = json.loads(json_string)  # Convertir JSON a diccionario
    return resultado_youtube(**data)

def inicia_poc_youtube(query):
    # print("Iniciando prueba")
    # query = "vscode spring boot extensiones"
    data = {
        "key": API_KEY,
        "part": "id,snippet",
        "q": query,
        "max_results": 10,
        "relevanceLanguage": "es",
    }
    try:
        r = requests.get(URL_YOUTUBE, params=data, timeout=20)
        r.raise_for_status()  # Esto lanzará una excepción para códigos de estado HTTP 4xx/5xx
        j = r.json()
        json_string = json.dumps(j, indent=4)
        respuesta_youtube = RespuestaYouTube.from_json(json_string)
        # json_output = respuesta_youtube.to_json()
        # print(json_output)
        return respuesta_youtube
        #print(respuesta_youtube)
        # Convertir a JSON y formatear
        # json_string = json.dumps(j, indent=4)
        # print(json_string)
        # Construir y retornar lista simplificada
        #resultados = [(v["id"]["videoId"], v["snippet"]["title"], v["snippet"]["thumbnails"]["default"]["url"]) for v in j["items"]]
        #print(resultados)
        #print("\n".join("   ".join(data) for data in resultados))
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud HTTP: {e}")
        return []

    #return resultados


if __name__ == "__main__":
    #inicia_poc_youtube("vscode spring boot extensiones")
    app.run(debug=True)

