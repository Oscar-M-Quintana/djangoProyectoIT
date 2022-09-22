from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("acerca-de", views.acerca_de, name="acerca_de"),
    path("cursos", views.cursos, name="cursos"),
    path("cursos/Json", views.cursos_json, name="cursos_Json"),
    path("cotizacion-dolar", views.cotidacion_dolar, name="cotizacion_dolar"),
    path("aeropuertos", views.aeropuertos, name="aeropuertos"),
    path("aeropuertos/Json", views.aeropuertos_json, name="aeropuertos_Json"),
    path("indexFromTemplates", views.indexTemplates, name="indexFromTemplates"),
    path("curso/<str:nombre_curso>", views.curso, name="curso"),
    path("tablacomentarios", views.tabla_comentarios, name="tabla_comentarios"),
    path("nuevocomentario", views.nuevo_comentario, name="nuevocomentario"),
    path(
        "peliculas/<str:nombre>/comentario/<int:numero_comentario>",
        views.peliculas,
        name="peliculas_comentarios",
    ),
    path("agregar-curso", views.nuevo_curso, name="agregar_curso"),
    path("nuevapelicula", views.nueva_pelicula, name="nueva_pelicula"),
    path("tablapeliculas", views.tabla_peliculas, name="tabla_peliculas"),
]
