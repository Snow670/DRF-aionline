# from rest_framework import permissions
#
#
# class IsOwnerReadOnly(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         #允许get,head,options请求
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.owner == request.user
