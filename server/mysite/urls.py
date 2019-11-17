from django.urls import include, path
from rest_framework import routers
from server.users import views as viewsUsers
from server.fileSystem import views as viewsFile

router = routers.DefaultRouter()
router.register(r'users', viewsUsers.UserViewSet)
router.register(r'permissions', viewsUsers.PermissionsViewSet)
router.register(r'permissionsFunction', viewsUsers.PermissionsFunctionViewSet)
router.register(r'files', viewsFile.fileViewSet)
router.register(r'types', viewsFile.typesViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    ]