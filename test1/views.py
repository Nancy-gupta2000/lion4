'''from django.shortcuts import render
from rest_framework import generics
from test1.models import Book
from test1.serializers import BookSerializer

# Create your views here.
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book
    serializer_class = BookSerializer
'''
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from test1.models import books
from test1.serializers import BookSerializer

from django.core.files.storage import default_storage


@csrf_exempt
def BookApi(request, id=0):
    if request.method == 'GET':
        books = books.objects.all()
        book_serializer = BookSerializer(books, many=True)
        return JsonResponse(book_serializer.data, safe=False)
    elif request.method == 'POST':
        Book_data = JSONParser().parse(request)
        book_serializer = BookSerializer(data=Book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse("Added", safe=False)
        return JsonResponse("Failed", safe=False)
    elif request.method == 'PUT':
        Book_data = JSONParser().parse(request)
        book = books.objects.get(titleid=Book_data['titleid'])
        book_serializer = BookSerializer(Book, data=Book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse("updated", safe=False)
        return JsonResponse("failed to update")
    elif request.method == 'DELETE':
        book = books.objects.get(titleid=id)
        book.delete()
        return JsonResponse("deleted", safe=False)
