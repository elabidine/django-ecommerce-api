from django.shortcuts import get_object_or_404
from store.models import Product,Collection
from ..serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import pagination,status
from ..permissions import IsAdminOrReadOnly


class ProductView(APIView,pagination.PageNumberPagination):
    def get(self, request):
         title = request.query_params.get('title')
         if title is not None:
            products = Product.objects.filter(title=title)
         else:
            products = Product.objects.all()
         paginate = self.paginate_queryset(products,request,view=self)
         serializer = ProductSerializer(paginate, many=True)
         return self.get_paginated_response(serializer.data)
 
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
      

class ProductDetailView(APIView):
    
    def get(self, request,id):

      product = get_object_or_404(Product,pk=id)
      serializer = ProductSerializer(product)
      return Response(serializer.data)
     
    def put(self,request,id):
        product = get_object_or_404(Product,pk=id)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
      
    def delete(self,request,id):
      product = get_object_or_404(Product,pk=id)
      product.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
      
      


       
