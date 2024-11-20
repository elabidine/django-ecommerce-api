from rest_framework import serializers
from .models import Product,Collection,ProductMedia

class ProductMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMedia
        fields = ['id','image']
        
    def create(self, validated_data):
        product_id = self.context['product_id']
        validated_data['product_id']=product_id
        existing_image  = ProductMedia.objects.filter(image=['image']).first()
        if existing_image:
            raise serializers.ValidationError("an image with the same file name exist")
        return ProductMedia.objects.create(**validated_data)

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id','title','product']

class ProductSerializer(serializers.ModelSerializer):
    image = ProductMediaSerializer(many=True,read_only = True)

    class Meta:
        model = Product
        fields = ['id','title','price','image','collections']
   
     