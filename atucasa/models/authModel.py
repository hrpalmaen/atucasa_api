''' File with models authentication '''

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ''' Model users or clients '''
    TYPE_DOCUMENT = [
        ('CC', 'Cédula de ciudadanía'),
        ('CE', 'Cédula de extranjería'),
        ('P', 'Pasaporte'),
        ('NIT', 'Nit')
    ]
    contact_phone = models.CharField('Teléfono de contacto', max_length=32, default='123456789')
    type_identification = models.CharField('Tipo de identificación', max_length=20, default='NIT')
    identification = models.CharField('Número de identificación', max_length=12, default='123456789')
    # shop = models.ForeignKey(Shops, verbose_name='Tiendas')