from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from apps.products.api.serializers.serializers import ProductSerializer
from apps.user.authentication_mixins import AuthenticationMixin

class ProductViewSet(AuthenticationMixin, viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(status=True)

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_object(), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        if product:
            product.status=False
            product.save()
            return Response({'message':'Product deleted successfully!'}, status=status.HTTP_200_OK)
        return Response({'error':'The product was not fount!'}, status=status.HTTP_400_BAD_REQUEST)
