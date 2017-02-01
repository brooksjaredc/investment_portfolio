from __future__ import unicode_literals
from django.contrib.auth.models import User
from django import forms
from django.forms import extras
from django.db import models

DOY = ('1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
       '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003',
       '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
       '2012', '2013', '2014', '2015', '2016', '2017')

class Stock(models.Model):
	user = models.ForeignKey(User)
	stock = models.CharField(max_length=5)
	date = models.DateTimeField()#widget=extras.SelectDateWidget(empty_label="Nothing", years = DOY))
	shares = models.DecimalField(max_digits=10,decimal_places=4)

	def __str__(self):
		return self.stock


# Create your models here.
