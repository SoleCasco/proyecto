from django.db import models

# Create your models here.
class valuacion(models.Model):
	origen=models.charField(max_length=1)
	cod_fabrica=models.integerField(null=true, blank=True)
	cod_marca=models.charField(max_length=5)
	cod_tipo=models.integerField()
	cod_modelo=models.integerField()
	tv=models.charField(max_length=1)
	marca=models.charField(max_length=50)
	descripcion=models.charField(max_length=100)
	tipo=models.charField(max_length=100)
	val_okm=models.IntegerField()
	val_2016=models.IntegerField()
	val_2015=models.IntegerField()
	val_2014=models.IntegerField()
	val_2013=models.IntegerField()
	val_2012=models.IntegerField()
	val_2011=models.IntegerField()
	val_2010=models.IntegerField()
	val_2009=models.IntegerField()
	val_2008=models.IntegerField()
	val_2007=models.IntegerField()
	val_2006=models.IntegerField()
	val_2005=models.IntegerField()
	val_2004=models.IntegerField()
	val_2003=models.IntegerField()
	val_2002=models.IntegerField()
	val_2001=models.IntegerField()
	val_2000=models.IntegerField()
	val_1999=models.IntegerField()
	val_1998=models.IntegerField()
	val_1997=models.IntegerField()
	val_1996=models.IntegerField()
	val_1995=models.IntegerField()
	val_1994=models.IntegerField()
	val_1993=models.IntegerField()
	def__str__(self):

		return self.origen + self.cod_marca + self.tv + self.marca + self.descripcion + self.tipo +





	








{código de marca, tipo y modelo
origen (nacional o importado)
tipo de fabricante (automotor, motovehículos, M.A.V.I.)
código de fabrica
código de marca
código de tipo
código de modelo
descripción de marca
descripción de modelo
descripción de tipo}