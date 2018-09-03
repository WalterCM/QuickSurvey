from django.db import models

class Survey(models.Model):
    SEX_CHOICES = [
        ("M", "Masculino"),
        ("F", "Femenino")
    ]

    first_name = models.CharField(("Nombre"), max_length=100)
    last_name = models.CharField(("Apellido"), max_length=100)
    dni = models.PositiveIntegerField(("DNI"), primary_key=True)
    sex = models.CharField(("Sexo"), max_length=1, choices=SEX_CHOICES)
    birthdate = models.DateField(("Fecha de nacimiento"))
    email = models.EmailField()
    category = models.CharField(("Categoria"), max_length=50)
    reason = models.CharField(("Por que te interesa esta categoria?"), max_length=500)

    def __str__(self):
        return "encuesta de " + self.first_name + " " + self.last_name + "(" + str(self.dni) + ")"

    class Meta:
        verbose_name = "Encuesta"
        verbose_name_plural = "Encuestas"
        ordering = ['dni']