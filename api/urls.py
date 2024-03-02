""" Urls """

from django.urls import path
from api.views import Bank_List, Test

urlpatterns = [
    path('banks/', Bank_List.as_view(), name='Bank_List'),
    path('test/', Test.as_view(), name='Test'),
]
