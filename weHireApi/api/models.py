from django.db import models

# Create your models here.
class Rol(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Usuarios(models.Model):
    nombre=models.CharField(max_length=50)
    correo=models.EmailField(max_length=255)
    clave=models.CharField(max_length=255,null=True)
    rol = models.ForeignKey(
        Rol, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name="usuarios"  
    )
    def __str__(self):
        return self.nombre
    

class Publicaciones(models.Model):
    titulo=models.CharField(max_length=255)
    descripcion=models.TextField(null=True)
    salario=models.DecimalField(max_digits=10, decimal_places=2, null=True)
    requisitos=models.TextField(null=True)
    estado=models.BooleanField()
    reclutador = models.ForeignKey(
        Usuarios, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name="publicaciones"
    )
    def __str__(self):
        return self.titulo
    
class EtapaInicial(models.Model):
    estado=models.BooleanField(null=True) 
    observaciones = models.TextField(null=True)
    usuario = models.ForeignKey(
        Usuarios, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name="etapa_inicial"
    )
    publicacion = models.ForeignKey(
        Publicaciones, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name="etapa_inicial"
    )
    def __str__(self):
        return f"Etapa Inicial de {self.usuario} en {self.publicacion}"
    
class EtapaMedia(models.Model):
    estado=models.BooleanField(null=True) 
    observaciones = models.TextField(null=True)
    archivo = models.FileField(upload_to='uploads/', null=True, blank=True)
    usuario = models.ForeignKey(
        Usuarios, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name="etapa_media"
    )
    publicacion = models.ForeignKey(
        Publicaciones, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name="etapa_media"
    )
    def __str__(self):
        return f"Etapa media de {self.usuario} en {self.publicacion}"
    
class EtapaFinal(models.Model):
    estado=models.BooleanField(null=True) 
    observaciones = models.TextField(null=True)
    archivo = models.FileField(upload_to='uploads/', null=True, blank=True)
    retroalimentacion = models.TextField(null=True)
    usuario = models.ForeignKey(
        Usuarios, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name="etapa_final"
    )
    publicacion = models.ForeignKey(
        Publicaciones, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name="etapa_final"
    )
    def __str__(self):
        return f"Etapa final de {self.usuario} en {self.publicacion}"