from __future__ import unicode_literals

from django.db import models

class Stock(models.Model):
	stock = models.CharField(max_length=5)
	price = models.DecimalField(max_digits=10,decimal_places=2)
	shares = models.DecimalField(max_digits=10,decimal_places=4)

	def __str__(self):
		return self.stock


# Create your models here.
