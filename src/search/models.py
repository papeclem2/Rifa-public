# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.postgres.fields import ArrayField

#Custom tables
class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    is_leaf = models.BooleanField(blank=True, null=True)
    category_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['category_name']

    def __str__(self):
        return self.category_name + " (" + str(self.category_id) + ")"


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    ean = models.TextField(blank=True, null=True)
    category_name = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)
    images = ArrayField(models.CharField(max_length=1000), blank=True, null=True)
    scoringdate = models.DateField(db_column='scoringDate', blank=True, null=True)  # Field name made lowercase.
    scoringlink = models.TextField(db_column='scoringLink', blank=True, null=True)  # Field name made lowercase.
    scoringsource = models.TextField(db_column='scoringSource', blank=True, null=True)  # Field name made lowercase.
    scoringimg = models.BinaryField(db_column='scoringImg', blank=True, null=True)  # Field name made lowercase.
    sku = models.TextField(blank=True, null=True)
    fk_id_category = models.ForeignKey(Category, models.DO_NOTHING, db_column='fk_id_category', blank=True, null=True)
    score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'
        verbose_name = 'Product'
        ordering = ['score', 'brand', 'title']

    def __str__(self):
        return self.title + " (" + self.brand + ")"