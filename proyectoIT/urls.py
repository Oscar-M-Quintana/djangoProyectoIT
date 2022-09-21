import imp
from django.urls import path, include

urlpatterns = [path("zmyapp/", include("zmyapp.urls"))]
