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

    def create(self,validated_data):
        return Books.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get("name")
        instance.author=validated_data("author")
        instance.price=validated_data("price")
        instance.publisher=validated_data("publisher")
        instance.qty=validated_data("qty")
        instance.save()
        return instance





    # def validate_price(self,value):
    #     if value not in range(50,1000):
    #         raise serializers.ValidationError("invalid price")
    #     return value
    #
    # def validate_qty(self,value):
    #     if value not in range(1,500):
    #         raise serializers.ValidationError("invalid quantity")
    #     return value

    # def validate(self, data):
    #     price = data.get("price")
    #     # print("price",price)
    #     qty=data.get("qty")
    #     if qty not in range(1,500):
    #         raise serializers.ValidationError("invalid quantity")
    #
    #     if price not in range(50, 1000):
    #         raise serializers.ValidationError("invalid price")
    #     return data


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

