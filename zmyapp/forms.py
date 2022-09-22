from django import forms

edades = (
    (1, "U (para todos los públicos)"),
    (2, "PG (con supervisión de los padres)"),
    (3, "12A (para mayores de 12 años)"),
    (4, "15 (para mayores de 15 años)"),
    (5, "18 (para mayores de 18 años)"),
    (6, "R-18 (restringido y para mayores de 18 años)"),
)


class FormularioCurso(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=128)
    inscriptos = forms.IntegerField(label="Inscriptos")


class FormularioComentario(forms.Form):
    id = forms.IntegerField(label="ID", min_value=0, max_value=64)
    pelicula = forms.CharField(label="pelicula", max_length=64)
    comentario = forms.CharField(label="Comentario")


class FormularioPelicula(forms.Form):
    nombre = forms.CharField(label="Nombre:", max_length=32)
    fecha = forms.DateField(
        label="Fecha de estrenos:", widget=forms.DateInput(attrs={"type": "date"})
    )
    restriccion = forms.ChoiceField(label="Clasificación:", choices=edades)
    preventa = forms.BooleanField(label="¿Preventa online?", required=False)
