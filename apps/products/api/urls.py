from django.urls import path
from apps.products.api.views.views import (
        ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView
    )
from apps.products.api.views.general_views import MeasureUnitList, CategoryProductList, IndicatorList

urlpatterns = [
    path('', ProductListCreateAPIView.as_view(), name='products'),
    path('retrieve_update_destroy/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='retrieve_update_destroy'),
    path('measure_unit/', MeasureUnitList.as_view(), name='measure_unit'),
    path('product_category/', CategoryProductList.as_view(), name='product_category'),
    path('indicator/', IndicatorList.as_view(), name='indicator')
]