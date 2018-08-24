from django.db import models


# Create your models here.

class persona(models.Model):

	nombre=models.CharField(max_length=50, blank=True)
	cuit_cuil=models.IntegerField()
	domicilio=models.CharField(max_length=50)

	def __str__(self):
		
		return self.nombre + self.domicilio

class marca(models.Model):
	nombre_marca=models.CharField(max_length=100)
	def __str__(self):
		return self.nombre_marca
class origen(object):
	"""docstring for origen"""
	nombre_origen=models.CharField(max_length=10)
	def __str__(self:
		
		return self.nombre_origen
class fabrica(object):
	cod_fabrica=models.
			"""docstring for fabrica"""
			
						
class tipo(object):
	"""docstring for tipo"""
	tv=models.CharField(max_length=50)
	def __str__(self):
		return self.nombre_tipo
class descripcion(object):
	"""docstring for descripcion"""
	cod_modelo=models.ForeignKey(modelo)
	desc=models.CharField(max_length=50)
		

		
class auto(models.Model):
	id_origen=models.IntegerField(max_length=50, blank=True)
	cod_fabrica=models.IntegerField(null=True, blank=True)
	cod_marca=models.CharField(max_length=5, blank=True)
	cod_tipo=models.IntegerField(null=True, blank=True)
	cod_modelo=models.CharField(max_length=50,null=True, blank=True)
	tv=models.CharField(max_length=3, blank=True)
	marca=models.CharField(max_length=50, blank=True)
	descripcion=models.CharField(max_length=100, blank=True)
	tipo=models.CharField(max_length=100, blank=True)
	valuacion=models.FloatField()
	
	def __str__(self):

		return self.origen + self.cod_marca + self.cod_modelo + self.tv + self.marca+ self.descripcion+ self.tipo
	
class vehiculo(models.Model):
	
	dominio=models.CharField(max_length=8)
	fechaalta=models.DateField()
	id_propietario=models.ForeignKey(persona, on_delete=models.CASCADE)
	id_auto=models.ForeignKey(auto, on_delete=models.CASCADE)

	def __str__(self):

		return self.dominio		

class impuesto(models.Model):
	id_vehiculo=models.ForeignKey(vehiculo, on_delete=models.CASCADE)
	monto=models.FloatField()
	fecha_inicio=models.DateField()
	fecha_final=models.DateField()
	concepto_bonificacion=models.CharField(max_length=100, blank=True)
	porcentaje_bonificacion=models.IntegerField()
	estado=models.CharField(max_length=50)
	def __str__(self):

		return self.concepto_bonificacion

class cuotas(object):
	id_impuesto=models.IntegerField()
	valor=models.FloatField()
	estado=models.CharField(max_length=50)
	fecha_1er_vencimiento=models.DateField()
	fecha_2do_vencimiento=models.DateField()
	interes1=models.IntegerField()
	interes2=models.IntegerField()
	def __str__(self):
		
		return self.estado


		
		



		
		