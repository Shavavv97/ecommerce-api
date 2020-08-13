from django.contrib import admin
from django.urls import path,include

from rest_framework import routers
from api.api import UserAPI, ProductAPI, OrderAPI, UserCreateAPI

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),

    #EndPoints
    path('api/users', UserAPI.as_view()),
    path('api/users/create', UserCreateAPI.as_view()),
    path('api/products', ProductAPI.as_view()),
    path('api/orders', OrderAPI.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
