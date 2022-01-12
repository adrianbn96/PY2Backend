from django.db import models
from django.db.models import (
    CharField,
)
# Create your models here.
class Usuario(models.Model):

    name = CharField(max_length=45, help_text='nombre')
    telephone = CharField(max_length=45, help_text='telefono')
    email = models.EmailField(max_length=45, unique=True,help_text='email')
    password = CharField(max_length=10, help_text='password')
    rol = CharField(max_length=45, help_text='rol')
    fechaNacimiento = models.DateField(help_text='fecha nacimiento')
    estadoUsuario = models.BooleanField(default=True,help_text='Estado del usuario')
    def __str__(self):
        return self.name 


class SolicitudPartida(models.Model):
    """Clase que representa una Establecimiento"""

    name = CharField(max_length=45, help_text='nombre')
    estado = CharField(max_length=45, help_text='estado')
    usuario = models.ForeignKey(
        
        Usuario,related_name="temples", on_delete=models.CASCADE
    )
    fechaPartida = models.DateField(help_text='fecha partida')

    def __str__(self):
        return self.name



