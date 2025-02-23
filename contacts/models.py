from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=152, default="")
    # could use django phone number package here, but its beyond scope of this exercise IMO
    phoneNumber = models.IntegerField(default=0)

    def __str__(self):
        return self.name