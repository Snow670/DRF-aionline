from .models import UserProfile

from rest_framework import serializers


class UserProfileSerializers(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = UserProfile
        fields = ('url','owner','id','username','nick_name','birthday','gender','address','mobile','image')
