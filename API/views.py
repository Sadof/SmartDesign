from rest_framework import generics
from API.serializers import *
from API.models import Product
from mongoengine import ValidationError
from rest_framework.exceptions import NotFound




# Function to find searching product or raise an exception
def get_obj_or_404(klass, *args, **kwargs):
    try:
        return klass.objects.get(*args, **kwargs)
    except klass.DoesNotExist:
        raise NotFound()
    except ValidationError:
        raise NotFound()


# If GET request then check url params and apply it to queryset or return all products else
# add new product to DB
class ProductAdd(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        name = self.request.query_params.get('name')
        param = self.request.query_params.get('param')
        value = self.request.query_params.get('value')
        if name:
            queryset = queryset.filter(name__iexact = name)
        if param and value:
            filter = 'params__' + param
            queryset = queryset.filter(**{filter: int(value) if value.isdigit() else value})

        if queryset:            #if parameters given and nothing find return Not Found
            return queryset
        else:
            raise NotFound()

class ProductView(generics.RetrieveAPIView):
    serializer_class =  ProductSerializer
    queryset = Product.objects.all()

    def get_object(self):
        queryset = get_obj_or_404(Product, pk=self.kwargs['pk'])
        return queryset


