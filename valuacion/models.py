from django.db import models

# Create your models here.
class valuacion(models.Model):
	origen=models.CharField(max_length=50, blank=True)
	cod_fabrica=models.IntegerField(null=True, blank=True)
	cod_marca=models.CharField(max_length=5, blank=True)
	cod_tipo=models.IntegerField(null=True, blank=True)
	cod_modelo=models.CharField(max_length=50,null=True, blank=True)
	tv=models.CharField(max_length=3, blank=True)
	marca=models.CharField(max_length=50, blank=True)
	descripcion=models.CharField(max_length=100, blank=True)
	tipo=models.CharField(max_length=100, blank=True)
	val_okm=models.IntegerField( null=True, blank=True)
	val_1=models.IntegerField(null=True, blank=True)
	val_2=models.IntegerField( null=True, blank=True)
	val_3=models.IntegerField(null=True, blank=True)
	val_4=models.IntegerField(null=True, blank=True)
	val_5=models.IntegerField(null=True, blank=True)
	val_6=models.IntegerField(null=True, blank=True)
	val_7=models.IntegerField(null=True, blank=True)
	val_8=models.IntegerField(null=True, blank=True)
	val_9=models.IntegerField(null=True, blank=True)
	val_10=models.IntegerField(null=True, blank=True)
	val_11=models.IntegerField(null=True, blank=True)
	val_12=models.IntegerField(null=True, blank=True)
	val_13=models.IntegerField(null=True, blank=True)
	val_14=models.IntegerField(null=True, blank=True)
	val_15=models.IntegerField(null=True, blank=True)
	val_16=models.IntegerField(null=True, blank=True)
	val_17=models.IntegerField(null=True, blank=True)
	val_18=models.IntegerField(null=True, blank=True)
	val_19=models.IntegerField(null=True, blank=True)
	val_20=models.IntegerField(null=True, blank=True)
	val_21=models.IntegerField(null=True, blank=True)
	val_22=models.IntegerField(null=True, blank=True)
	val_23=models.IntegerField(null=True, blank=True)
	val_24=models.IntegerField(null=True, blank=True)
	def __str__(self):
		

		return self.origen + self.cod_marca + self.tv + self.marca + self.descripcion + self.tipo
