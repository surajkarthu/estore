# python to query set is called SERIALIZATION
# QUERY SET TO PYTHON IS CALLED DESERIALIZATION

from rest_framework import serializers
from api.models import Books,Reviews

class BookSerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name = serializers.CharField()
    author = serializers.CharField()
    price = serializers.IntegerField()
    publisher = serializers.CharField()
    qty = serializers.IntegerField()


class BookModelSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    class Meta:
        model=Books
        fields="__all__"


class ReviewSerializer(serializers.ModelSerializer):
    created_date=serializers.CharField(read_only=True)
    class Meta:
        model = Reviews
        fields="__all__"
        #exclude = ("created_date",)


