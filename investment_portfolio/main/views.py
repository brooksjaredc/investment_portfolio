from django.shortcuts import render
from .models import Stock
#from django.http import HttpResponse

# Create your views here.
def index(request):
	stocks = Stock.objects.all()
	#return HttpResponse('<h1>Hello There!</h1>')
	return render(request, 'index.html', {'stocks':stocks})


class Stock:
	def __init__(self, stock, price, shares):
		self.stock = stock
		self.price = price
		self.shares = shares

stocks = [
	Stock('INTC', 1000.00, 10),
	Stock('MU', 20, 100),
	Stock('INX', 2200, 2)
]