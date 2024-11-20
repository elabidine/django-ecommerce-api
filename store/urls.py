from django.urls import path

from store.views.product_media_views import ProductMediaView,ProductAllMediaView,ProductMediaViewDetail
from .views.product_views import ProductView,ProductDetailView
from .views.collection_views import CollectionView,CollectionDetailView




urlpatterns = [

    path('product/', ProductView.as_view(), name='product'),
    path('product/<uuid:id>', ProductDetailView.as_view(), name='product_list'),
    path('collection/', CollectionView.as_view(), name='collection'),
    path('collection/<int:id>', CollectionDetailView.as_view(), name='collection_list'),
    path('product/<uuid:product_id>/media/', ProductMediaView.as_view(), name='create-product-media'),
    path('product/<uuid:product_id>/media/<int:media_id>', ProductMediaViewDetail.as_view(), name='create-product-media'),
    path('media/', ProductAllMediaView.as_view(), name='media'),
]