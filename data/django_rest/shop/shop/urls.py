"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from products import views #ls1
from users import views as user_views #ls5

from django.conf import settings  #ls7
from django.conf.urls.static import static  #ls7

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/test/', views.test), #ls1
    path('api/v1/test_post/', views.test_post), #ls3
    # path('api/v1/products/', views.product_list_view), #ls1
    path('api/v1/products/', views.product_list_create_view), #ls3
    path('api/v1/products/<int:id>/', views.product_item_view), #ls1
    # path('api/v1/register/', user_views.registration), #ls5
    # path('api/v1/login/', user_views.authorization), #ls5
    path('api/v1/register/', user_views.RegisterAPIView.as_view()), #ls6
    path('api/v1/login/', user_views.AuthAPIView.as_view()), #ls6
    path('api/v1/brands', views.BrandListAPIView.as_view()), #ls6
    # path('api/v1/brands/<int:id>', views.BrandItemAPIView.as_view()), #ls6
    path('api/v1/brands/<int:pk>/', views.BrandItemAPIView.as_view()), #ls6
    path('api/v1/reviews/', views.ReviewModelViewSet.as_view({'get': 'list', 'post': 'create'})), #ls6
    path('api/v1/reviews/<int:pk>/',
         views.ReviewModelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})), #ls6
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  #ls7