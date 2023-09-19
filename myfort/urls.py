
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path("",views.index,name="index"),
    path("inner/",views.inner,name="inner"),
    path("port/",views.port,name="port"),
    path('admin/', admin.site.urls),
]
