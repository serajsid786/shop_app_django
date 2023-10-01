from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:id>/',views.detail,name='detail'),
    path('createproduct/',views.create_product,name='createproduct'),
    path('editproduct/<int:id>',views.edit_product,name='editproduct'),
    path('deleteproduct/<int:id>',views.delete_product,name='deleteproduct')
]