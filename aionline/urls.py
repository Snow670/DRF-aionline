from django.urls import path
import xadmin
from django.views.generic import TemplateView

urlpatterns = [
    path('xadmin/',xadmin.site.urls),
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('login/',TemplateView.as_view(template_name='userinfo/login.html'),name='login'),
]
