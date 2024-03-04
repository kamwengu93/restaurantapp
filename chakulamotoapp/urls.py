
from django.contrib import admin
from django.urls import path
from chakulamotoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index , name='index'),
    path('inner/', views.inner, name='inner'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('adminhome/', views.adminhome, name='adminhome'),
]
