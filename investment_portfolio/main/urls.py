from django.conf.urls import include, url
from django.conf import settings
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'buy_url/$', views.buy_stock, name='buy_stock'),
	#url(r'^user/(\w+)/buy_url/$', views.buy_stock, name='buy_stock'),
	url(r'^user/(\w+)/$', views.profile, name='profile'),
	url(r'^login/$', views.login_view, name='login'),
	url(r'^register/$', views.register, name='register'),
	url(r'^logout/$', views.logout_view, name='logout')
]