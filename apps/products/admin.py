from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from apps.products.models import *

class MeasureUnitResource(resources.ModelResource):
    class Meta:
        model = MeasureUnit

class MeasureUnitAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('id', 'description',)
    readonly_fields = ('create_date', 'update_date', 'delete_date')
    list_display = ('id', 'description', 'create_date', 'update_date', 'delete_date')
    list_filter = ('create_date', 'update_date', 'delete_date')
    resource_class = MeasureUnitResource

class CategoryProductResource(resources.ModelResource):
    class Meta:
        model = CategoryProduct

class CategoryProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('id', 'description',)
    readonly_fields = ('create_date', 'update_date', 'delete_date')
    list_display = ('id', 'description', 'create_date', 'update_date', 'delete_date')
    list_filter = ('create_date', 'update_date', 'delete_date')
    resource_class = CategoryProductResource

class IndicatorResource(resources.ModelResource):
    class Meta:
        model = Indicator

class IndicatorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('id', 'description',)
    readonly_fields = ('create_date', 'update_date', 'delete_date')
    list_display = ('id', 'descount_value', 'create_date', 'update_date', 'delete_date')
    list_filter = ('create_date', 'update_date', 'delete_date')
    resource_class = IndicatorResource

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product

class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('id', 'name', 'description', 'category_product', 'measure_unit',)
    readonly_fields = ('create_date', 'update_date', 'delete_date')
    list_display = ('id', 'name', 'description', 'category_product', 'measure_unit', 'create_date', 'update_date', 'delete_date')
    list_filter = ('create_date', 'update_date', 'delete_date')
    resource_class = ProductResource

# Register your models here.

admin.site.register(MeasureUnit, MeasureUnitAdmin)
admin.site.register(CategoryProduct, CategoryProductAdmin)
admin.site.register(Indicator, IndicatorAdmin)
admin.site.register(Product, ProductAdmin)