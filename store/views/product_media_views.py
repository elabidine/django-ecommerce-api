from django.shortcuts import get_object_or_404
from store.models import Product, ProductMedia
from ..serializers import ProductMediaSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import pagination,status
from ..permissions import IsAdminOrReadOnly
from rest_framework.parsers import FormParser, MultiPartParser



class ProductAllMediaView(APIView,pagination.PageNumberPagination):
    def get(self, request,*args ,**kwargs):
         product_media = ProductMedia.objects.all()
         paginate = self.paginate_queryset(product_media,request,view=self)
         serializer = ProductMediaSerializer(paginate,many=True)
         return self.get_paginated_response(serializer.data)
     
     
class ProductMediaView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    
    def get(self, request, product_id,*args,format=None ,**kwargs):
         print('idddddddddddddddddddddddddddddddddddddddd',product_id)
         product = get_object_or_404(Product, id=product_id)
         serializer = ProductMediaSerializer(product.image.all(),many=True)
         return Response(serializer.data)
     
    def post(self, request, product_id, format=None):
       
        serializer = ProductMediaSerializer(data=request.data,context={'product_id':product_id})
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',serializer.context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
         print(serializer.errors)  
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
     
class ProductMediaViewDetail(APIView):

      def get(self, request, *args,format=None ,**kwargs):
         product_id = kwargs.get('media_id')
         product = get_object_or_404(ProductMedia, id=product_id)
         serializer = ProductMediaSerializer(product)
         return Response(serializer.data)
    
      def put(self, request, *args, format=None, **kwargs):
        media_id = kwargs.get('media_id')
        product_media = get_object_or_404(ProductMedia, id=media_id)
        serializer = ProductMediaSerializer(product_media, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      def delete(self, request, *args, format=None, **kwargs):
        media_id = kwargs.get('media_id')
        product_media = get_object_or_404(ProductMedia, id=media_id)
        product_media.delete()
        return Response({'message': 'ProductMedia deleted successfully'}, status=status.HTTP_204_NO_CONTENT)