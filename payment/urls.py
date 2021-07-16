

from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('esewa-reguest', views.EsewaRequestView.as_view(),name="request"),
    path('esewa-verified',views.EsewaVerifyView.as_view(),name="esewaverify"),
]