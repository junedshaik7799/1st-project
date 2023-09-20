from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from app1.api.serializers import employeeserializer
from app1.models import employee


@api_view(['GET','POST'])
def employee_list(request):
    

    if request.method == 'GET':
     employee_obj = employee.objects.all()
     serializer = employeeserializer(employee_obj,many = True).data
     print("serialiser",serializer)
     return Response(serializer) 
    
    if request.method == 'POST':
       serializer = employeeserializer(data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
       else:
          return Response(serializer.errors)



@api_view(['GET','PUT','DELETE'])
def employee_details(request,pk):
    print("helloo-->",request.method)
    if request.method == 'GET':
     employee_obj = employee.objects.get(pk=pk)
     serializer = employeeserializer(employee_obj)
     return Response(serializer.data)
    
    if request.method == 'PUT':  
       employee_obj = employee.objects.get(pk=pk)
       serializer = employeeserializer(employee_obj,data=request.data,partial=True)
       if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
       else:
          return Response(serializer.errors)
       
    if request.method == 'DELETE':
       employee_obj = employee.objects.get(id=pk)
       employee_obj.delete()
       return Response("Deleted Sucessfully")
