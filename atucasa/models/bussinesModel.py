''' File with models bussines '''

from django.db import models
from .authModel import User

class Audit(models.Model):
    ''' Base audit model'''
    date_created = models.DateTimeField('Fecha creación',auto_now_add=True)
    date_update = models.DateTimeField('Fecha última actualización',auto_now=True)
    is_active = models.BooleanField('Estado', default=True)

    class Meta:
        abstract = True

class City(Audit):
    ''' Cities model '''
    name = models.CharField('Ciudad o Municipio', max_length=64)
    departament = models.CharField('Departamento', max_length=64)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'City'
        db_table = 'atc_city'

class Category_Store(Audit):
    ''' Model for categories by store '''
    name = models.CharField('Nombre Categoría', max_length=128)
    description = models.CharField('Descripción', max_length=512, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Category_store'
        db_table = 'atc_category_store'

class Store(Audit):
    ''' Stores model '''
    name = models.CharField('Nombre Tienda', max_length=128)
    user = models.ForeignKey(User, verbose_name='Cliente', on_delete=models.CASCADE)
    category_store = models.ManyToManyField(Category_Store, verbose_name='Tiendas')
    url_logo = models.URLField('Logotipo', max_length=248)
    description = models.CharField('Descripción de la empresa', max_length=512)
    email = models.CharField('Correo electrónico', max_length=512, null=True, blank=True)
    contact_name = models.CharField('Nombre de contacto', max_length=128, null=True, blank=True)
    phone = models.CharField('Número teléfono', max_length=32)
    star = models.BooleanField('start', default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Store'
        db_table = 'atc_store'

class Branch(Audit):
    ''' Branches model '''
    name = models.CharField('Nombre sede', max_length=128)
    city = models.ForeignKey(City, verbose_name='Ciudad', on_delete=models.CASCADE)
    store = models.ForeignKey(Store, verbose_name='Tienda', on_delete=models.CASCADE)
    direction = models.CharField('Dirección', max_length=256, null=True, blank=True)
    coor_x = models.CharField('Coordenada x', max_length=16, null=True, blank=True)
    coor_y = models.CharField('Coordenada y', max_length=16, null=True, blank=True)
    phone = models.CharField('Número teléfono', max_length=32, null=True, blank=True)
    email = models.CharField('Correo electrónico', max_length=64, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Branch'
        db_table = 'atc_branch'

class Category_Product(Audit):
    ''' Model for categories by products '''
    name = models.CharField('Nombre Categoría', max_length=128)
    description = models.CharField('Descripción', max_length=512, null=True, blank=True)
    url_image = models.URLField('Imagen', max_length=256, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Category_product'
        db_table = 'atc_category_product'

class Product(Audit):
    ''' Products model '''
    name = models.CharField('Nombre producto', max_length=128)
    store = models.ForeignKey(Store, verbose_name='Tienda', on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, verbose_name='Sede', on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField('Descripción', max_length=512, null=True, blank=True)
    presentation = models.CharField('Presentación', max_length=64, null=True, blank=True)
    price = models.BigIntegerField('Precio')
    brand = models.CharField('Marca', max_length=32, null=True, blank=True)
    units = models.IntegerField('Unidades disponibles')
    discount_porcentual = models.IntegerField('Porcentaje de descuento', null=True, blank=True)
    url_image = models.URLField('Imagen', max_length=256, null=True, blank=True)
    name_store = models.CharField('Nombre tienda', max_length=128, null=True, blank=True)
    category_product = models.ManyToManyField(Category_Product, verbose_name='Categoria')
    star = models.BooleanField('start', default=False)
    
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Product'
        db_table = 'atc_product'
