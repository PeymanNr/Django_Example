from django.db import models


class ProductType(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)

    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "ProductType"
        verbose_name_plural = "ProductTypes"
    def __str__(self):
        return self.name

class ProductAttribute(models.Model):
    INTEGER = 1
    STRING = 2
    FLOAT = 3

    ATTRIBUTE_TYPE_FIELDS = (
        (INTEGER, "Integer"),
        (STRING, "String"),
        (FLOAT, "Float"),
    )

    title = models.CharField(max_length=32)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='attributes')
    attribute_type = models.PositiveSmallIntegerField(default=INTEGER, choices=ATTRIBUTE_TYPE_FIELDS)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=32)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=32)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT, related_name='products')
    upc = models.BigIntegerField(unique=True)
    title = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='products')
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class ProductAttributeValue(models.Model):
    product_attribute = models.ForeignKey(ProductAttribute, on_delete=models.PROTECT, related_name='values')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_attributes')
    value = models.CharField(max_length=48)

    def __str__(self):
        return f"{self.product}({self.product_attribute}): {self.value}"