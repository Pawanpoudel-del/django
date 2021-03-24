from django.urls import path
from myapp import views
urlpatterns =[
    path('custom', views.new)
    ]