from django import forms
from django.forms import extras, ModelForm
from .models import Stock

DOY = ('1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
       '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003',
       '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
       '2012', '2013', '2014', '2015', '2016', '2017')

class BuyForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['stock', 'date', 'shares']
	# stock = forms.CharField(max_length=5)
	date = forms.DateTimeField(widget=extras.SelectDateWidget(empty_label="Nothing", years = DOY))
	# shares = forms.DecimalField(max_digits=10,decimal_places=4)

class LoginForm(forms.Form):
	username = forms.CharField(label='User Name', max_length=64)
	password = forms.CharField(widget=forms.PasswordInput())