from django.urls import path

from . import views

urlpatterns = [
    path('load', views.load, name='load'),
    path('getAll', views.get_all_transactions, name='getAll'),
    path('get/<str:id>', views.get_transaction_by_id, name='get_by_id'),
    path('search', views.search, name='search')
]
