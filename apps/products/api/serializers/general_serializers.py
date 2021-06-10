from rest_framework import serializers
from apps.products.models import MeasureUnit, CategoryProduct, Indicator

class MeasureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureUnit
        exclude = ('status', 'create_date', 'update_date', 'delete_date')

class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProduct
        exclude = ('status', 'create_date', 'update_date', 'delete_date')

class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicator
        exclude = ('status', 'create_date', 'update_date', 'delete_date')