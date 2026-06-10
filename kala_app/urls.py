from django.urls import path
from . import  views
urlpatterns = [
    path('prof/',views.index,name='prof'),
    path('product/<int:id>/',views.product_detail,name='product_detail'),
]