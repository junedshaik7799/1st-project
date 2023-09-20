from rest_framework import serializers
from app1.models import employee
from app1.models1 import company
from app1.models2 import Arthematics

class employeeserializer(serializers.ModelSerializer):
    class Meta:
        model =  employee
        fields = "__all__"
    def validate(self,data):
        return data


    
class Companyserializer(serializers.ModelSerializer):
    class Meta:
        model = company
        fields = "__all__"
    def validate(self,data):
        return data
    

class Arthematicsserializer(serializers.ModelSerializer):
    class Meta:
        model = Arthematics
        fields = "__all__"


    