from rest_framework.response import Response
from rest_framework.decorators import APIView
from django.shortcuts import render
from app1.models1 import company
from app1.api.serializers import Companyserializer


class Company_list(APIView):
    def get(self,request):
        company_obj = company.objects.all()
        return Response(Companyserializer(company_obj,many=True).data)
    
    def post (self,request):
        company_obj = company(
            name = request.data.get("name"),
            place = request.data.get("place"),
            employee_id = request.data.get("employee")
        )
        company_obj.save()
        return Response(Companyserializer(company_obj).data)
    
    def put (self,request):
        company_obj = company(
            name = request.data.get("name"),
            place = request.data.get("place"),
            employee_id = request.data.get("employee")
        )
        company_obj.save()
        return Response (Companyserializer(company_obj).data)
    

    def delete (self,request,id):
        company_obj = company.objects.get(id=id)
        company_obj.delete()
        return Response("deleted")




    

     