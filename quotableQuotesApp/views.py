from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
from django.db.models import Q
from datetime import date

def register(request):
	return render(request, "index.html")

def createuser(request):
	print(request.POST)
	errors = User.objects.userValidator(request.POST)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect("/")
	else:
		password = request.POST['pw']
		hashedpassword = bcrypt.hashpw(request.POST ['pw'].encode(), bcrypt.gensalt()).decode()
		newuser = User.objects.create(firstName = request.POST['fname'], lastName = request.POST ['lname'], email = request.POST['useremail'], password = hashedpassword )
		print (newuser.id)
		request.session['loggedInID'] = newuser.id
	return redirect("/quotes")

def quotes(request):
	loggedInUser = User.objects.get(id=request.session['loggedInID'])
	context = {
		'loggedUser': loggedInUser,
		'allquotes' : Quotes.objects.exclude(likes = loggedInUser).order_by("-created_at"),	
		'allfavorites' : Quotes.objects.filter(likes = loggedInUser)
	}
	return render (request, "quotes.html", context)	

def login(request):
	print(request.POST)
	validationErrors = User.objects.loginValidator(request.POST)
	if len(validationErrors) > 0:
		for key, value in validationErrors.items():
			messages.error(request, value)
		return redirect("/")
	loggedInUser = User.objects.get(email = request.POST['useremail'])
	print("*******")
	print(loggedInUser)
	print("********")
	request.session['loggedInID'] = loggedInUser.id
	return redirect("/quotes")

def addQuote(request):
	print(request.POST)	
	errors = Quotes.objects.quoteValidator(request.POST)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect("/quotes")
	loggedInUser = User.objects.get(id=request.session['loggedInID'])
	newquote = Quotes.objects.create(desc = request.POST['desc'], quoter = request.POST['quoter'], creator = loggedInUser)
	return redirect("/quotes")

def delete(request, quoteId):
	quote = Quotes.objects.get (id = quoteId)
	quote.delete()
	return redirect("/quotes")

def edit(request, quoteId):
	loggedInUser = User.objects.get(id=request.session['loggedInID'])
	quote = Quotes.objects.get (id = quoteId)
	context = {
	'loggedUser' : loggedInUser,
	'quote' : 	quote
	}
	return render(request, 'edit.html', context)

def update(request, quoteId):
	print(request.POST)
	quote = Quotes.objects.get(id = quoteId)
	quote.desc = request.POST['desc']
	quote.quoter = request.POST['quoter']
	quote.save()
	return redirect("/quotes")

def addfavor(request, quoteId):
	loggedUser = User.objects.get(id=request.session['loggedInID'])
	quote = Quotes.objects.get(id = quoteId)
	quote.likes.add(loggedUser)
	return redirect("/quotes")

def removefavor(request, quoteId):
	loggedUser = User.objects.get(id=request.session['loggedInID'])
	quote = Quotes.objects.get(id = quoteId)
	quote.likes.remove(loggedUser)
	return redirect("/quotes")

def display(request, userId):
	loggedInUser  = User.objects.get(id=userId)
	context = {
		'blogger' : loggedInUser,
		'allqoutes' : Quotes.objects.filter(creator = loggedInUser)
	}
	return render(request, 'users.html', context)
	
def logout(request):
	request.session.clear()
	return redirect("/")