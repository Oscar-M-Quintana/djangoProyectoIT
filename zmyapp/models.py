from pickle import TRUE
from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=128)
    inscriptos = models.IntegerField()


class Instructor(models.Model):
    nombre = models.CharField(max_length=128, unique=TRUE)
    email = models.CharField(max_length=32)
    cursos_asignados = models.IntegerField()
