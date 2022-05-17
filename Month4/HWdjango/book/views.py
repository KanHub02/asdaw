from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book


# Create your views here.
def title(request):
    return HttpResponse("<h1>Library</h1>")


def all_books(request):
    books = Book.objects.all()
    return render(request, "book.html", {"main": books})

def book_info(request):
    object = get_object_or_404(models.Book, id=id)
    return render(request, "detail.html", {"show": object})
