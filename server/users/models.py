from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    
class Permissions (models.Model):
    name = models.CharField(max_length=50)
    #todo 
    #tabela PermissionsFun.


class PermissionsFunction (models.Model):
    name = models.CharField(max_length=50)
    

