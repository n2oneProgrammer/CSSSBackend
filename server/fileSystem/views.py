from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from server.fileSystem.serializers import fileSerializer, typesSerializer, GroupSerializer, UserSerializer
from server.fileSystem.models import file, types

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class fileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = file.objects.all()
    serializer_class = fileSerializer


class typesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = types.objects.all()
    serializer_class = typesSerializer