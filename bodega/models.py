from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.hashers import make_password, check_password

class usuario(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    password =models.CharField(max_length=50)
    nombres = models.CharField(max_length=100,default="")

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(usuario, self).save(*args, **kwargs)

class bodega(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=70)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    def natural_key(self):
        return (self.id, self.nombre,self.direccion)

class producto(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=70)
    detalle = models.TextField(default='')
    valor = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

    def natural_key(self):
        return (self.id, self.codigo,self.nombre,self.detalle,self.valor)

class bodegaProducto(models.Model):
    id = models.AutoField(primary_key=True)
    idBodega = models.ForeignKey(bodega, on_delete=CASCADE)
    idProducto = models.ForeignKey(producto, on_delete=CASCADE)
    stock = models.IntegerField(default=0)