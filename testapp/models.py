from django.db import models


# Create your models here.
class PaystackData(models.Model):
    client_id = models.CharField(max_length=100)
    amount = models.IntegerField()
    currency = models.CharField(max_length=100)

    def __str__(self):
        return self.client_id


class Client(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    mobile_no = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
