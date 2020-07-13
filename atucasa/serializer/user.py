''' File user serializers '''

from django.contrib.auth.models import Group
from rest_framework import serializers

from atucasa.models import User


class UserSerializer(serializers.ModelSerializer):
  ''' user or clients serializer '''

  def validate_first_name (self, value):
    if value == '':
      raise serializers.ValidationError('Este campo es obligatorio.')
    return value

  def validate_last_name (self, value):
    if value == '':
      raise serializers.ValidationError('Este campo es obligatorio.')
    return value

  def validate_email (self, value):
    if value == '':
      raise serializers.ValidationError('Este campo es obligatorio.')
    return value

  def create(self, validated_data):
    '''  serializer for create users or clients '''

    group_data = validated_data.pop('groups')

    user = super().create(validated_data)
    user.set_password(validated_data.get('password'))
    user.groups.set(group_data)
    user.save()

    return user
  
  def update(self, instance, validated_data):
    ''' serializer for update users or clients'''
    group_data = validated_data.pop('groups')
    
    user = super().update(instance, validated_data)
    # remove current group
    groupDelete = Group.objects.get(user=user.id)
    groupDelete.user_set.remove(user.id)
    # update current group
    user.groups.set(group_data)
    
    if instance.password != validated_data.get('password'):
        user.set_password(validated_data.get('password'))
    user.save()
      
    return user

  class Meta:

    model = User
    fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'contact_phone',
              'is_staff', 'type_identification', 'identification', 'groups', 'password')
