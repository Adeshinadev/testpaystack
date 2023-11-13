from django.urls import path
from .views import PayStackRequest,Client

urlpatterns = [
    path("paystack/payment-request/", PayStackRequest.as_view(), name="paystack/payment-request"),
    path("clients/", Client.as_view(), name="clients")
]
