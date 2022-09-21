import re
import sqlite3
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
from django.http import Http404
from . import forms


def index(resquest):
    return render(resquest, "zmyapp/index.html")


def acerca_de(request):
    return HttpResponse("¡Curso de Python y Django!")


def cotidacion_dolar(request):
    peticion = requests.get("https://api.recursospython.com/dollar")
    cotizacion = peticion.json()
    html = """
    <html>
    <title>Cotización del dolar</title>
    """
    for valor in cotizacion:
        html += f"""
        <h3>{valor} : {cotizacion[valor]}</h1>
        """
    html += "</html>"
    return HttpResponse(html)


def aeropuertos(request):
    archivo = open("aeropuertos.csv", encoding="utf8")
    diccionario = []
    for datos in archivo:
        lista = datos.split(sep=",")
        nombre = lista[1].replace('"', "")
        ciudad = lista[2].replace('"', "")
        pais = lista[3].replace('"', "")
        diccionario.append((nombre, ciudad, pais))
    archivo.close()
    ctx = {"lista_aeropuertos": diccionario}
    return render(request, "zmyapp/aeropuertos.html", ctx)


def aeropuertos_json(request):
    archivo = open("aeropuertos.csv", encoding="utf8")
    diccionario = open("aeropuertos2.csv", mode="w", encoding="utf8")
    lectura = []
    diccionario.write("Aeropuerto;Ciudad;Pais\n")
    for datos in archivo:
        lista = datos.split(sep=",")
        a = lista[1].strip('"')
        b = lista[2].strip('"')
        c = lista[3].strip('"')
        linea = f"Aeropuerto: {a} ; Ciudad: {b}; Pais: {c} \n"
        diccionario.write(linea)
        lectura.append(linea)
    archivo.close()
    diccionario.close()
    return JsonResponse(lectura, safe=False)


def indexTemplates(request):
    ctx = {
        "nombre": "Juan Carlos",
        "cursos": 5,
        "curso_actual": {"nombre": "Python & Django", "turno": "Noche"},
        "cursos_anteriores": ["Java", "PHP", "JavaScript", "Python"],
    }
    return render(request, "zmyapp/index2.html", ctx)


def peliculas(request, numero_comentario, nombre):
    conn = sqlite3.connect("cursos.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, pelicula, comentario FROM comentarios WHERE id=?",
        [numero_comentario],
    )
    pelicula = cursor.fetchone()
    print(pelicula[1])
    print("hola!!!!")
    if pelicula is None:
        raise Http404
    """ if nombre != pelicula:
        raise Http404 """
    ctx = {"pelicula": pelicula}
    conn.close()
    return render(request, "zmyapp/peliculas.html", ctx)


def tabla_comentarios(request):
    conn = sqlite3.connect("cursos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, pelicula, comentario FROM comentarios")
    peli = cursor.fetchall()
    conn.close()
    ctx = {"peliculas": peli}
    return render(request, "zmyapp/tabla_comentarios.html", ctx)


def nueva_pelicula(request):
    if request.method == "POST":
        form = forms.FormularioPelicula(request.POST)
        if form.is_valid():
            conn = sqlite3.connect("cursos.db")
            cursor = conn.cursor()
            datos = (
                form.cleaned_data["nombre"],
                form.cleaned_data["fecha"],
                form.cleaned_data["restriccion"],
                form.cleaned_data["preventa"],
            )
            cursor.execute(
                "INSERT INTO peliculas VALUES (?, ?, ?, ?)",
                datos,
            )
            conn.commit()
            conn.close()
            ctx = {"form": datos}
            return render(request, "zmyapp/peliculacargada.html", ctx)
    else:
        form = forms.FormularioPelicula()
        ctx = {"form": form}
        return render(request, "zmyapp/nuevapelicula.html", ctx)


def tabla_peliculas(request):
    conn = sqlite3.connect("cursos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, fecha, restriccion, preventa FROM peliculas")
    peliculas = cursor.fetchall()
    conn.close()
    ctx = {"peliculas": peliculas}
    return render(request, "zmyapp/tablapeliculas.html", ctx)


def curso(request, nombre_curso):
    conn = sqlite3.connect("cursos.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT nombre, inscriptos FROM cursos WHERE nombre=?", [nombre_curso]
    )
    curso = cursor.fetchone()
    if curso is None:
        raise Http404
    ctx = {"curso": curso}
    conn.close()
    return render(request, "zmyapp/curso.html", ctx)


def cursos(request):
    conn = sqlite3.connect("cursos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, inscriptos FROM cursos")
    cursos = cursor.fetchall()
    conn.close()
    ctx = {"cursos": cursos}
    return render(request, "zmyapp/cursos.html", ctx)


def cursos_json(request):
    conn = sqlite3.connect("cursos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, inscriptos FROM cursos")
    response = JsonResponse(cursor.fetchall(), safe=False)
    conn.close()
    return response


def nuevo_curso(request):
    if request.method == "POST":
        form = forms.FormularioCurso(request.POST)
        if form.is_valid():
            conn = sqlite3.connect("cursos.db")
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO cursos VALUES (?, ?)",
                (form.cleaned_data["nombre"], form.cleaned_data["inscriptos"]),
            )
            conn.commit()
            conn.close()
            return HttpResponse("¡Curso creado correctamente!")
    else:
        form = forms.FormularioCurso()
        ctx = {"form": form}
        return render(request, "zmyapp/agregar.html", ctx)
