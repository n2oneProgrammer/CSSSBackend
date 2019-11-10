from rest_framework import viewsets
from server.fileSystem.serializers import fileSerializer, typesSerializer
from server.fileSystem.models import file, types

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