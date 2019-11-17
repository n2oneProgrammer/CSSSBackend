from django.db import models

#this function ceretwe path to file
def cerate_path(Type):
    return '\\'+str(Type.name)


class file (models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    fileType = models.ForeignKey('types', on_delete=models.CASCADE)
    upload = models.FileField(upload_to=cerate_path(fileType))
    #autor = models.ForeignKey('server.auth.User', on_delete=models.CASCADE)

    
    #this function return url to file
    def getUrl(self):
        return self.fileType.url()



class types (models.Model):
    name = models.CharField(max_length=50)
