from django.contrib.auth.models import Group, User
from rest_framework import serializers
from server.fileSystem.models import file, types

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class fileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = file
        fields = dir(file)

class typesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = types
        fields = dir(types)

