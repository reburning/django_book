# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from mysite.books.models import Book

def search_form(request):
    return render_to_response('search_from.html')

def search(request):
    if 'q' in request.GET:
        q = request.GEt['q']
        books = Book.objects.filter(title__icontains=q)
        return render_to_response('search_results.html',{'books': books, 'query': q})
    else:
        message = 'You submitted an empty form.'
        return HttpResponse('Please submit a search term.')