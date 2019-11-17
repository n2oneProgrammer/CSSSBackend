from server.users.models import User, Permissions, PermissionsFunction
from rest_framework import viewsets
from server.users.serializers import UserSerializer, PermissionsSerializer, PermissionsFunctionSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PermissionsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Permissions.objects.all()
    serializer_class = PermissionsSerializer
    
class PermissionsFunctionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = PermissionsFunction.objects.all()
    serializer_class = PermissionsFunctionSerializer