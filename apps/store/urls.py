from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url(r'store/$', views.index, name='index'),
    url(r'store/buy', views.buy, name='buy'),
    url(r'store/checkout', views.checkout, name='checkout'),
    url(r'store/reset', views.reset, name='reset'),
    path('',views.home,name='home'),
    path('store/invoice/pdf/<int_pk>/',views.SaleInvoicePdfView,name='sale_invoice_pdf'),
   
]