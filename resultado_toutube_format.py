from dataclasses import dataclass
from typing import List, Dict, Optional
import json

@dataclass
class Video:
    id: str
    titulo: str
    imagen: str


@dataclass
class RespuestaYouTube:
    videos: List[Video]

    @staticmethod
    def from_json(json_string: str) -> "RespuestaYouTube":
        data = json.loads(json_string)
        return RespuestaYouTube(
            videos=[
                Video(
                    id=item["id"]["videoId"],
                    titulo=item["snippet"]["title"],
                    imagen=item["snippet"]["thumbnails"]["default"]["url"],
                )
                for item in data["items"]
            ],
        )

    def to_json(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)