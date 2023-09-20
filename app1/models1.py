from django.db import models
from app1.models import employee
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class company(models.Model):
    name = models.CharField(max_length=22)
    place = models.CharField(max_length=22)
    employee = models.ForeignKey(employee,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = 'new.app1_company'

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


