#!/usr/bin/python
class Video:
    def __init__(self, id, videoId, titulo, imagen):
        self.id = id
        self.videoId = videoId
        self.titulo = titulo
        self.imagen = imagen

    def __str__(self):
        return f"{self.id} {self.videoId} {self.titulo} {self.imagen}"