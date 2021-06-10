from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel

# Create your models here.

class MeasureUnit(BaseModel):
    description = models.CharField('Description', max_length=50, blank=False, null=False, unique=True)
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Measure Unit'
        verbose_name_plural = 'Measure Units'

    def __str__(self):
        return self.description

class CategoryProduct(BaseModel):
    description = models.CharField('Description', max_length=50, blank=False, null=False, unique=True)
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.description

class Indicator(BaseModel):
    descount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Indicator of ofert')
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Indicator of Ofert'
        verbose_name_plural = 'Indicators of Ofert'

    def __str__(self):
        return f'Ofert of category {self.category_product}: {self.descount_value}%'

class Product(BaseModel):
    name = models.CharField('Product Name', max_length=150, unique=True, blank=False, null=False)
    description = models.TextField('Product Description', blank=False, null=False)
    image = models.ImageField('Product Image', upload_to='products/', blank=True, null=True)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Product Category')
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Measure Unit')
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name