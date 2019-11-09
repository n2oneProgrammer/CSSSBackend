from django.db import models

def cerate_path(Type):
    return '.\files\\'+str(Type.name)


class file (models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    fileType = models.ForeignKey('types', on_delete=models.CASCADE)
    upload = models.FileField(upload_to=cerate_path(fileType))
    
    
    def getUrl():
        return self.fileType.url


class types (models.Model):
    name = models.CharField(max_length=50)
