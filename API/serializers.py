from rest_framework_mongoengine.serializers import DocumentSerializer
from API.models import Product




class ProductSerializer(DocumentSerializer):
    class Meta:
        model = Product




