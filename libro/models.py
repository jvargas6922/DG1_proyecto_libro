from django.db import models

# Create your models here.
class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200, null=False)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField(null=False)

    class Meta:
        managed = False
        db_table = 'libros'

    def __str__(self):
        return self.titulo
