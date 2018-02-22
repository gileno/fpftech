from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import ProductModelSerializer
from .models import Product


# class ProductAPIView(APIView):

#     def get(self, request, pk=None):
#         if pk is None:
#             serializer = ProductModelSerializer(Product.objects.all(), many=True)
#             return Response(serializer.data)
#         else:
#             product = Product.objects.get(pk=pk)
#             serializer = ProductModelSerializer(product)
#             return Response(serializer.data)
    
#     def post(self, request):
#         serializer = ProductModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

class ProductAPIView(ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

    def get_queryset(self):
        return Product.objects.active()


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProductModelSerializer
    lookup_url_kwarg = 'id'
    queryset = Product.objects.all()
