from django.contrib import admin
from django.urls import path
from kwik import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test', views.testing, name='test')
]
