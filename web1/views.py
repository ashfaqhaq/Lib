from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from .models import books_taken,books_requested
import requests
import speech_recognition as sr
from bs4 import BeautifulSoup
import urllib.request

# Create your views here.
def homepage(request):
	return render(request=request,
			template_name="web1/home.html",
			context={"context1":books_taken.objects.all,"context2":books_requested.objects.all})


def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("web1:homepage")


def login_request(request):
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect('/')
			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")
	form = AuthenticationForm()
	return render(request = request,
				template_name = "web1/login.html",
				context={"form":form})

def button(request):

	return render(request,'web1/home.html')



def output(request):
	r = sr.Recognizer()

	with sr.Microphone() as source:
		print('Hey! Vishnu speak something')
		audio = r.listen(source)
		try:
			text = r.recognize_google(audio)
			
			book = text.replace(" ",'+')
			url = 'https://www.goodreads.com/search?q='+book
			oururl = urllib.request.urlopen(url)
			soup = BeautifulSoup(oururl,'html.parser')
			phref=soup.table.tr.td.a['href']
			s=phref.find("w/")
			e=phref.find(".")
			book_id = phref[s+2:e]
			print(book_id)
			new_url = 'https://www.goodreads.com'+phref
			new_oururl = urllib.request.urlopen(new_url)
			soup = BeautifulSoup(new_oururl,'html.parser')
			x=soup.find_all('a',{'class':'actionLinkLite bookPageGenreLink'})
			li=[]
			for i in x:
				li.append(i.text)
			return render(request,'web1/home.html',{'list':li})
		except:
			text='Sorry cannot recognize your voice'
	return render(request,'web1/home.html',{'text':text})