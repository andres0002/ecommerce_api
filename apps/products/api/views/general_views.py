from apps.base.api import GenericsListAPIView
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer, IndicatorSerializer

class MeasureUnitList(GenericsListAPIView):
    serializer_class = MeasureUnitSerializer

class CategoryProductList(GenericsListAPIView):
    serializer_class = CategoryProductSerializer

class IndicatorList(GenericsListAPIView):
    serializer_class = IndicatorSerializer