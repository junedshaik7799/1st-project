from rest_framework.response import Response
from rest_framework.decorators import APIView
from django.shortcuts import render
from app1.models import employee
from app1.api.serializers import employeeserializer

class Employee_List(APIView):
    def post (self,request):
        employee_obj = employee(
            name = request.data.get("name"),
            salary = request.data.get("salary"),
        )
        employee_obj.save()
        return Response(employeeserializer(employee_obj).data)
    
    def put(self,request):
        employee_obj = employee(
                name = request.data.get("name"),
            salary = request.data.get("salary"),
        )
        employee_obj.save()
        return Response(employeeserializer(employee_obj).data)
    
    def delete(self,request, id):
        employee_obj = employee.objects.get(id=id)
        employee_obj.delete()
        return Response("succesfully deleted")
    

    def get(self,request):
        employee_obj = employee.objects.all()
        return Response(employeeserializer(employee_obj,many = True).data)
    
