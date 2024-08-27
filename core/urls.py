from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('quotation/', views.quotation_view, name='quotation'),
    path('submit_quotation/', views.submit_quotation, name='submit_quotation'),  # 修改為對應 submit_quotation 視圖
    path('contact/', views.contact, name='contact'),
]
