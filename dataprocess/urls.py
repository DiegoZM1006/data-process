from django.urls import path
from dataprocess.views.index import Index

urlpatterns = [
    path('', Index.as_view(), name = "index"),
]