from django.db import models


# Create your models here.

class Salon(models.Model):
    # id = models.AutoField(primary_key=True)
    aula = models.CharField(max_length=2)
    hora_entrada = models.TimeField()

    class Meta:
        verbose_name = 'Salon'
        verbose_name_plural = 'Salons'


class Alumno(models.Model):
    # id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
