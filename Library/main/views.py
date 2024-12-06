from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Book,Library,Event
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html',{'user': request.user})

# def books(request):
#     all_books = Book.objects.all()
#     return render(request, 'books.html', {'books': all_books})

def books(request):
    query = 'a'
    query = request.GET.get('q', '') 
    results = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    return render(request, 'books.html', {'query': query, 'books': results})

def libo(request):
    library = Library.objects.all()
    return render(request, 'about.html', {'library': library})

def events(request):
    event = Event.objects.all()
    return render(request, 'events.html', {'events': event})

def contacts(request):
    return render(request, 'contact.html')


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def custom_logout(request):
    logout(request)
    return redirect('login')