from django.db import models


class Propietario(models.Model):

	nombre=models.CharField(max_length=50, blank=True)
	tipo_doc=models.CharField(max_length=5)
	cuit_cuil=models.IntegerField()
	domicilio=models.CharField(max_length=50)

	def __str__(self):
		
		return self.nombre + self.domicilio+ self.tipo_doc

class Origen(models.Model):
	nombre_origen=models.CharField(max_length=10)
	def __str__(self):

		return self.nombre_origen

class Fabrica(models.Model):
	cod_fabrica=models.IntegerField(max_length=4)
	id_origen=models.ForeignKey(origen,null=True, blank=True)
			
			
						
class Tipo(models.Model):
	tv=models.CharField(max_length=50)
	id_fabrica=models.ForeignKey(fabrica)
	def __str__(self):
		return self.nombre_tipo

class Marca(models.Model):

	nombre_marca=models.CharField(max_length=100)
	id_tipo=models.ForeignKey(tipo)
	def __str__(self):
		return self.nombre_marca

class Modelo(models.Model):
	nombre_modelo=models.CharField(max_length50)
	id_marca=models.ForeignKey(marca)
		

class Descripcion(models.Model):
	
	desc=models.CharField(max_length=50)
	id_modelo=models.ForeignKey(modelo)	

		
class Anio(models.Model):
	
	anio=models.DateField()
	id_descripcion=models.ForeignKey(descripcion)
	def __str__(self):
		return self.anio + self.id_descripcion

class Valor(self):
	id_anio=models.ForeignKey(Anio)
	precio=models.FloatField()
	def __str__(self):

		return self.precio+ self.id_anio
	
	
class Vehiculo(models.Model):
	
	dominio=models.CharField(max_length=8)
	fechaalta=models.DateField()
	id_propietario=models.ForeignKey(persona, on_delete=models.CASCADE)
	id_auto=models.ForeignKey(auto, on_delete=models.CASCADE)

	def __str__(self):

		return self.dominio		

class Impuesto(models.Model):
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


		
		



		
		