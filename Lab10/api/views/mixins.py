from rest_framework import mixins, generics
from api.models import Product
from api.serializers import ProductSerializer



class ProductListAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)
class ProductDetailAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Product.object.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'
    def get(self, requset, *args, **kwargs):
        return self.retrieve(requset, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
