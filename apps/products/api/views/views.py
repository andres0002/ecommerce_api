from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from apps.products.api.serializers.serializers import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(status=True)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(status=True)
        return self.get_serializer().Meta.model.objects.filter(status=True).filter(id=pk).first()

    def patch(self, request, pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk))
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error':'The product was not fount!'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        product = self.get_queryset(pk)
        if product:
            product.status=False
            product.save()
            return Response({'message':'Product deleted successfully!'}, status=status.HTTP_200_OK)
        return Response({'error':'The product was not fount!'}, status=status.HTTP_400_BAD_REQUEST)
