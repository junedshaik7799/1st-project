from django.contrib import admin
from app1.models import employee
from app1.models1 import company
from app1.models2 import Arthematics

# Register your models here.
admin.site.register(employee)
admin.site.register(company)
admin.site.register(Arthematics)
