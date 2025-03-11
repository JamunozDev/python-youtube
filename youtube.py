import requests
import json

def get_video_info(query, limit=10):
    API_KEY = "AIzaSyAEgTD5z1HJNimTYiAo_YJh-XfXrLVfpww"
    url = f"https://www.googleapis.com/youtube/v3/search"
    data = {
        "key": API_KEY,
        "part": "id,snippet",
        "q": query,
        "max_results": limit,
        "relevanceLanguage": "es"
    }
    r = requests.get(url, params=data)
    j = r.json()
    #print(j)
    # Construir y retornar lista simplificada
    return [ (v["id"]["videoId"], v["snippet"]["title"]) for v in j["items"] ]

resultados = get_video_info("vscode spring boot extensiones",20)
print("\n".join("   ".join(data) for data in resultados))
