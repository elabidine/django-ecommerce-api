from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import ProductMedia

  
@receiver(pre_delete, sender=ProductMedia)
def delete_product_media(sender, instance, using,**kwargs):
     print(f"Deleting image for ProductMedia instance {instance}")
     instance.image.delete(save=False)  
     print(f"Image deleted successfully.")
    