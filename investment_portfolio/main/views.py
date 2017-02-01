from django.shortcuts import render
from django.http import HttpResponseRedirect
import datetime
from .models import Stock
from .forms import BuyForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
	stocks = Stock.objects.all()
	#return HttpResponse('<h1>Hello There!</h1>')
	form = BuyForm()
	return render(request, 'index.html', {'stocks':stocks, 'form': form})

def buy_stock(request):
	form = BuyForm(request.POST)
	#user = User.objects.get(username=username)
	if form.is_valid():
		# stock = Stock(stock = form.cleaned_data['stock'],
		# 			  date = form.cleaned_data['date'],
		# 			  shares = form.cleaned_data['shares'])
		# stock.save()
		stock = form.save(commit = False)
		stock.user=request.user
		stock.save()
	return HttpResponseRedirect(reverse(profile, args=[request.user.username]))
	#return render(request, 'profile.html', {'form': form})

def profile(request, username):
	user = User.objects.get(username=username)
	stocks = Stock.objects.filter(user=user)
	form = BuyForm()
	return render(request, 'profile.html', {'username': username, 'stocks': stocks, 'form': form})

def login_view(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			u = form.cleaned_data['username']
			p = form.cleaned_data['password']
			user = authenticate(username = u, password = p)
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/')
				else:
					print("The account has been disabled!")
			else:
				print("The username and password were incorrect.")

	else:
		form = LoginForm()
		return render(request, 'login.html', {'form': form})

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')


def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/login/')
	else:
		form = UserCreationForm()
		return render(request, 'registration.html', {'form': form})

# class Stock:
# 	def __init__(self, stock, date, shares):
# 		self.stock = stock
# 		self.date = date
# 		self.shares = shares

stocks = [
	Stock('INTC', datetime.datetime(2012,1,1,00,00,00), 10),
	Stock('MU', datetime.datetime(2012,1,1,00,00,00), 100),
	Stock('INX', datetime.datetime(2012,1,1,00,00,00), 2)
]