from django.db import models


class contactus(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    email=models.EmailField(primary_key=True)
    comment=models.CharField(max_length=255)
    class Meta:
        db_table="contactus"
