from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    '''
    Modelo de usuarios o clientes
    '''
    TYPE_DOCUMENT = [
        ('CC', 'Cédula de ciudadanía'),
        ('CE', 'Cédula de extranjería'),
        ('P', 'Pasaporte')
    ]
    contact_phone = models.CharField('Teléfono de contacto', max_length=32, default='123456789')
    type_identification = models.CharField('Tipo de identificación', max_length=20, default='CC')
    identification = models.CharField('Número de identificación', max_length=12, default='123456789')
    # shop = models.ForeignKey(Shops, verbose_name='Tiendas')


class City(models.Model):
    '''
    Modelo de ciudades
    '''
    name = models.CharField('Ciudad o Municipio', max_length=64)
    departament = models.CharField('Departamento', max_length=64)

    date_created = models.DateTimeField('Fecha creación',auto_now_add=True)
    date_update = models.DateTimeField('Fecha última actualización',auto_now=True)
    is_active = models.BooleanField('Estado', default=True)
    delete = models.BooleanField('Eliminado', default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'City'
        db_table = 'atc_city'


class Category_Store(models.Model):
    '''
    Modelo de categorias en tiendas
    '''
    name = models.CharField('Nombre Categoría', max_length=128)
    description = models.CharField('Descripción', max_length=512, null=True, blank=True)

    date_created = models.DateTimeField('Fecha creación',auto_now_add=True)
    date_update = models.DateTimeField('Fecha última actualización',auto_now=True)
    is_active = models.BooleanField('Estado', default=True)
    delete = models.BooleanField('Eliminado', default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Category_store'
        db_table = 'atc_category_store'


class Store(models.Model):
    '''
    Módelo de las tiendas
    '''
    name = models.CharField('Nombre Tienda', max_length=128)
    user = models.ForeignKey(User, verbose_name='Cliente', on_delete=models.CASCADE)
    category_store = models.ManyToManyField(Category_Store, verbose_name='Tiendas')
    url_logo = models.URLField('Logotipo', max_length=248)
    description = models.CharField('Descripción de la empresa', max_length=512)
    email = models.CharField('Correo electrónico', max_length=512, null=True, blank=True)
    contact_name = models.CharField('Nombre de contacto', max_length=128, null=True, blank=True)
    phone = models.CharField('Número teléfono', max_length=32)

    date_created = models.DateTimeField('Fecha creación',auto_now_add=True)
    date_update = models.DateTimeField('Fecha última actualización',auto_now=True)
    is_active = models.BooleanField('Estado', default=True)
    delete = models.BooleanField('Eliminado', default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Store'
        db_table = 'atc_store'


class Branch(models.Model):
    '''
    Modelo de las sedes
    '''
    name = models.CharField('Nombre sede', max_length=128)
    city = models.ForeignKey(City, verbose_name='Ciudad', on_delete=models.CASCADE)
    store = models.ForeignKey(Store, verbose_name='Tienda', on_delete=models.CASCADE)
    direction = models.CharField('Dirección', max_length=256, null=True, blank=True)
    coor_x = models.CharField('Coordenada x', max_length=16, null=True, blank=True)
    coor_y = models.CharField('Coordenada y', max_length=16, null=True, blank=True)
    phone = models.CharField('Número teléfono', max_length=32, null=True, blank=True)
    email = models.CharField('Correo electrónico', max_length=64, null=True, blank=True)

    date_created = models.DateTimeField('Fecha creación',auto_now_add=True)
    date_update = models.DateTimeField('Fecha última actualización',auto_now=True)
    is_active = models.BooleanField('Estado', default=True)
    delete = models.BooleanField('Eliminado', default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Branch'
        db_table = 'atc_branch'


class Category_Product(models.Model):
    '''
    Modelo de categorias por producto
    '''
    name = models.CharField('Nombre Categoría', max_length=128)
    description = models.CharField('Descripción', max_length=512, null=True, blank=True)

    date_created = models.DateTimeField('Fecha creación',auto_now_add=True)
    date_update = models.DateTimeField('Fecha última actualización',auto_now=True)
    is_active = models.BooleanField('Estado', default=True)
    delete = models.BooleanField('Eliminado', default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Category_product'
        db_table = 'atc_category_product'


class Product(models.Model):
    '''
    Modelo de productos
    '''
    name = models.CharField('Nombre producto', max_length=128)
    store = models.ForeignKey(Store, verbose_name='Tienda', on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, verbose_name='Sede', on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField('Descripción', max_length=512)
    presentation = models.CharField('Presentación', max_length=64)
    price = models.BigIntegerField('Precio')
    brand = models.CharField('Marca', max_length=32, null=True, blank=True)
    units = models.IntegerField('Unidades disponibles')
    discount_porcentual = models.DecimalField('Porcentaje de descuento', max_digits = 3, decimal_places = 3)
    url_image = models.URLField('Imagen', max_length=256)
    name_store = models.CharField('Nombre tienda', max_length=128, null=True, blank=True)
    category_product = models.ManyToManyField(Category_Product, verbose_name='Categoria')

    date_created = models.DateTimeField('Fecha creación',auto_now_add=True)
    date_update = models.DateTimeField('Fecha última actualización',auto_now=True)
    is_active = models.BooleanField('Estado', default=True)
    delete = models.BooleanField('Eliminado', default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Product'
        db_table = 'atc_product'