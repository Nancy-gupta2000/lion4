from rest_framework import serializers
from test1.models import book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['titleid', 'authorid', 'isbnid', 'publisherid']
