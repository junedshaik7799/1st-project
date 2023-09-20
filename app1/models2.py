from django.db import models

Arthematicchoice_fields= (
    ("ADD","ADD"),
    ("SUB","SUB"),
    ("MUL","MUL"),
    ("DIV","DIV")
)

class Arthematics(models.Model):
    number_1 = models.FloatField()
    number_2 = models.FloatField()
    date_1 = models.DateTimeField(auto_now_add=True)
    choicefield = models.CharField(max_length=200,choices=Arthematicchoice_fields)
    result = models.FloatField(null=True,blank=True)

    def __str__(self) -> str:
        return str(self.id)
