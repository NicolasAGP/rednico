from django.conf.urls import url, include
from catalog.views import index
from django.urls import path
from . import views

app_name="catalog"

urlpatterns = [
    path('', index)

]
