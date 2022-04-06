from django.db import models
from stat import FILE_ATTRIBUTE_DIRECTORY
from django.forms import CharField


class Familiar(models.Model):
    name = models.CharField("Nombre",max_length=30)
    surname = models.CharField("Apellido",max_length=30)
    age = models.IntegerField()
    birth_date = models.DateField("Año de nacimiento")
    link = models.CharField("Parentezco", max_length=30)

    def __str__(self) -> str:
        return f"{self.name} - {self.surname} - {self.age} - {self.birth_date} - {self.link}"


