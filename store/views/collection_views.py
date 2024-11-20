from django.shortcuts import get_object_or_404
from store.models import Collection
from ..serializers import ProductSerializer,CollectionSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status


class CollectionView(APIView):
    
    def get(self,request):
        
         collection = Collection.objects.all()
         serializer = CollectionSerializer(collection, many=True)
         return Response(serializer.data)
 
    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    
    
class CollectionDetailView(APIView):
    
    def get(self,id):
      collection = get_object_or_404(Collection,pk=id)
      serializer = ProductSerializer(collection)
      return Response(serializer.data)
     
    def put(self,request,id):
        collection = get_object_or_404(Collection,pk=id)
        serializer = CollectionSerializer(collection, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
      
    def delete(self,id):
      collection = CollectionSerializer(Collection,pk=id)
      collection.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
      