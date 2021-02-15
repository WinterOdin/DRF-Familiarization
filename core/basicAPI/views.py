from django.shortcuts import render
from .serializers import *
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.


class ArticleAPIView(APIView):
    def get(self, request):
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_404_NOT_FOUND)


class articleDetail(APIView):
    def get_object(self, id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return HttpResponse(content= "There was no article with this id", status = status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request,id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return HttpResponse(status=204)
    




#@api_view(['GET','POST' ])
#def articleList(requset):
#    if requset.method == "GET":
#        article = Article.objects.all()
#        serializer = ArticleSerializer(article, many=True)
#        return Response(serializer.data)
#
#    elif requset.method == "POST":
#        serializer = ArticleSerializer(data=requset.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status = status.HTTP_201_CREATED)
#        return Response(serializer.errors, status = status.HTTP_404_NOT_FOUND)


#@api_view(['GET','PUT','DELETE' ])
#def articleDetail(requset,pk):
#    try:
#        article = Article.objects.get(pk=pk)
#    except Article.DoesNotExist:
#        return HttpResponse(content= "There was no article with this id", status = status.HTTP_404_NOT_FOUND)
    
#    if requset.method == "GET":
#        serializer = ArticleSerializer(article)
#        return Response(serializer.data)
#
 #   elif requset.method == "PUT":
#        
#        serializer = ArticleSerializer(article,data=requset.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status = status.HTTP_201_CREATED)
#        return Response(serializer.errors, status = status.HTTP_404_NOT_FOUND)
#    
#    elif requset.method == "DELETE":
##        article.delete()
#        return HttpResponse(status=204)