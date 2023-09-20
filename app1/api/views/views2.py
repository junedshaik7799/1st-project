from rest_framework.response import Response
from rest_framework.decorators import api_view
from app1.api.serializers import employeeserializer
from app1.models import employee 
from rest_framework.views import APIView


class EmployeeList(APIView):
    def get (self,request):
        employee_obj = employee.objects.all()
        serializer = employeeserializer(employee_obj,many = True)
        return Response(serializer.data)
    
    def post (self,request):
        serializer = employeeserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response("error")
        

class EmployeeDetails(APIView):
    def get(self, request, pk):
        emp = employee.objects.get(pk=pk)
        emp_serialiser = employeeserializer(emp)
        return Response(emp_serialiser.data)
           
        
    def put(self,request,pk):
        employee_obj = employee.objects.get(pk=pk)
        serializer = employeeserializer(employee_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response("error")
        
    def delete(self, request, pk):
        try:
            employee_obj = employee.objects.get(pk=pk)
            employee_obj.delete()
            return Response("sucess")
        except:
            return Response("invalid id")




                
            



