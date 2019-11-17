from server.users.models import User, Permissions, PermissionsFunction
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = dir(User)


class PermissionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permissions
        fields = dir(Permissions)

class PermissionsFunctionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PermissionsFunction
        fields = dir(PermissionsFunction)