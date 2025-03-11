#!/usr/bin/python
import sys
import requests

# variables
API_KEY = "AIzaSyAEgTD5z1HJNimTYiAo_YJh-XfXrLVfpww"
url = "https://www.googleapis.com/youtube/v3/search"

def buscar_youtube(query):
    data = {
        "key": API_KEY,
        "part": "id,snippet",
        "q": query,
        "max_results": 10,
        "relevanceLanguage": "es"
    }
    r = requests.get(url, params=data)
    j = r.json()
    
    return [ (v["id"]["videoId"], v["snippet"]["title"]) for v in j["items"] ]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Error: Debes proporcionar la cadena de búsqueda.")
        print("Uso: python buscadr_youtube.py <cadena de búsqueda>")
        sys.exit(1)
    
    resultado = buscar_youtube(sys.argv[1])
    print("\n".join("   ".join(data) for data in resultado))



    