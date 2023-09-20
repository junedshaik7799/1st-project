from rest_framework.response import Response
from rest_framework.decorators import api_view
from app1.api.serializers import Companyserializer
from app1.models1 import company 
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class CompanyList(APIView):
    authentication_classes = [ BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

class CompanyList(APIView):
    def get (self, request):
        company_obj = company.objects.all()
        serializer = Companyserializer(company_obj,many = True)
        return Response(serializer.data)

    def post (self, request):
        serializer = Companyserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response("error")
        
class CompanyDetails(APIView):
    def get (self,request,pk):
        com = company.objects.get(pk=pk)
        com_serializer = Companyserializer(com)
        return Response(com_serializer.data)
    
    def put (self,request,pk):
        company_obj = company.objects.get(pk=pk)
        serializer = Companyserializer(company_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response("error")

    def delete (self, request, pk):
        try:
            company_obj = company.objects.get(pk=pk)
            company_obj.delete()
            return Response("succesfully deleted")
        except:
            return Response("invalid data")


            
        

    




        