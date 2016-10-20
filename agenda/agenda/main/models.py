from django.db import models

class Producto(models.Model):
	nombre=models.CharField(max_length=140)
	desc=models.TextField()
	precio=models.CharField(max_length=140)

	def __str__ (self):
		return self.nombre
		#return "El nombre del producto es: {} y su precio es: {}".format(self.nombre,self.precio)
