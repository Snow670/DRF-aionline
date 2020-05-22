from .models import UserProfile
from users.serializer import UserProfileSerializers
# from .permissions import IsOwnerReadOnly

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework import permissions


@api_view(['GET'])
def api_root(request,format=None):
    return Response({
        "users":reverse('user-list',request=request,format=format)
    })


class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    #自动提供了List和detail操作
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerReadOnly]
    #
    # def perform_create(self,serializer):
    #     serializer.save(owner=self.request.user)
