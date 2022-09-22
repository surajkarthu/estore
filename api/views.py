from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Books,Reviews
from api.serializers import BookSerializer,ReviewSerializer
from rest_framework.viewsets import ViewSet

# class ProductsView(APIView):
#     def get(self,request,*args,**kwargs):
#         return Response({"msg":"inside products get"})
#
# class MorningView(APIView):
#     def get(self,request,*args,**kwargs):
#         return Response({"msg":"good morning"})
#
# #class AddView(APIView):
#  #   def get(self,request,*args,**kwargs):
#   #      num1=int(input("enter number1"))
#    #     num2=int(input("enter number2"))
#     #    res=num1+num2
#      #   return Response({"result": res})
#
#
# #class SubView(APIView):
#  #   def get(self,request,*args,**kwargs):
#   #      num1=int(input("enter number1"))
#    #     num2=int(input("enter number2"))
#     #    res=num1-num2
#      #   return Response({"result": res})
#
# class MulView(APIView):
#     def get(self, request, *args, **kwargs):
#         num1 = int(input("enter number1"))
#         num2 = int(input("enter number2"))
#         res = num1 * num2
#         return Response({"result": res})
#
# class DivView(APIView):
#     def get(self,request,*args,**kwargs):
#         num1=int(input("enter number1"))
#         num2=int(input("enter number2"))
#         res=num1/num2
#         return Response({"result": res})
#
# class ModView(APIView):
#     def get(self,request,*args,**kwargs):
#         num1=int(input("enter number1"))
#         num2=int(input("enter number2"))
#         res=num1%num2
#         return Response({"result": res})
#
# class AddView(APIView):
#     def post(self,request,*args,**kwargs):
#         n1=request.data.get("num1")
#         n2=request.data.get("num2")
#         res=int(n1)+int(n2)
#         return Response({"result": res})
#
#
#
# class SubView(APIView):
#     def post(self,request,*args,**kwargs):
#         n1=request.data.get("num1")
#         n2=request.data.get("num2")
#         res=int(n1)-int(n2)
#         return Response({"result": res})
#
class CubeView(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get("num"))
        res=n**3
        return Response({"result":res})

class Numcheck(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get("num"))
        res=""
        if n%2==0:
            res="number is even"
        else:
            res="number is odd"
        return Response({"result": res})


class FactView(APIView):
    def post(self,request,*args,**kwargs):
        n = int(request.data.get("num"))
        res=1
        for i in range(1,(n+1)):
            res=res*i
        return Response({"result": res})

class WordCountView(APIView):
    def post(self, request, *args, **kwargs):
        txt=request.data.get("text")
        words=txt.split(" ")
        word_count={}
        for w in words:
            if w in word_count:
                word_count[w]+=1
            else:
                word_count[w]=1

        return Response(data=word_count)

class ProductsView(APIView):

    def get(self,request,*args,**kwargs):
        qs=Books.objects.all()
        serializer=BookSerializer(qs,many=True)
        return Response(data=serializer.data)


    def post(self,request,*args,**kwargs):
        # bname=request.data.get("name")
        # bauthor=request.data.get("author")
        # bprice=request.data.get("price")
        # bpublisher=request.data.get("publisher")
        # Books.objects.create(name=bname,author=bauthor,price=bprice,publisher=bpublisher)

        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            Books.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class ProductDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        book=Books.objects.get(id=id)
        serializer=BookSerializer(book,many=False)
        return Response(data=serializer.data)
        return Response(data="inside details")

    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")
        Books.objects.get(id=id).delete()
        return Response(data="deleted")

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            Books.objects.filter(id=id).update(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class ReviewView(APIView):
    def get(self,request,*args,**kwargs):
        reviews=Reviews.objects.all()
        serializer=ReviewSerializer(reviews,many=True)
        return Response(data=serializer.data)


    def post(self,request,*args,**kwargs):
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class ReviewDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Reviews.objects.get(id=id)
        serializer=ReviewSerializer(qs,many=False)
        return Response(data=serializer.data)

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        object=Reviews.objects.get(id=id)
        serializer=ReviewSerializer(instance=object,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")
        Books.objects.get(id=id).delete()
        return Response(data="deleted")


class ProductsViewsetView(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Books.objects.all()
        serializer=BookSerializer(qs,many=True)
        return Response(data=serializer.data)

    def create(self,request,*args,**kwargs):
        serializer=BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("id")
        book=Books.objects.get(id=id)
        serializer=BookSerializer(book,many=False)
        return Response(data=serializer.data)

    def update(self,request,*args,**kwargs):
        id=kwargs.get("id")
        book=Books.objects.filter(id=id)
        serializer = ReviewSerializer(instance=object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def destroy(self,request,*args,**kwargs):
        id = kwargs.get("id")
        Books.objects.get(id=id).delete()
        return Response(data="deleted")

