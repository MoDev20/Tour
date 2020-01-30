from django.urls import path     
from . import views
urlpatterns = [
	path('', views.register),
	path('createuser', views.createuser),
	path('quotes', views.quotes),
	path('login', views.login),
	path('createQuote', views.addQuote),
	path('quotes/<quoteId>/delete', views.delete),
	path('quotes/<quoteId>/edit', views.edit),
	path('updatequote/<quoteId>', views.update),
	path('quotes/<quoteId>/add', views.addfavor),
	path('quotes/<quoteId>/remove', views.removefavor),
	path('users/<userId>', views.display),
	path('logout', views.logout),
	


]