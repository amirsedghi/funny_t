from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index),
    url(r'^cart$', views.cart),
    url(r'^admin$', views.admin),
    url(r'^login$', views.login),
    url(r'^dashboard/orders/(?P<id>\d+)$', views.orderdash),
    url(r'^ordershow$', views.ordershow),
    url(r'^dashboard/products/(?P<id>\d+)$', views.productdash),
    url(r'^add$', views.add),
    url(r'^product/adding$', views.adding),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^editing/(?P<id>\d+)$', views.editing),
    url(r'^product/show/(?P<id>\d+)$', views.show),
    url(r'^addcart$', views.addcart),
    url(r'^process_order$', views.processorder),
]
