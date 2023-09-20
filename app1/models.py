from django.db import models

# Create your models here.
class employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=11)
    salary = models.IntegerField()

    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = 'new.app1_employee'
