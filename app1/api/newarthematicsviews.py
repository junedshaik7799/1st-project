from datetime import datetime,timedelta
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from app1.models2 import Arthematics
from app1.api.serializers import Arthematicsserializer


class Arthematics_list(APIView):
    def get(self, request):
        start_date =  request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        hour= request.query_params.get('hour')
        id =  request.query_params.get('id')
        arth = Arthematics.objects.all().order_by('-date_1')
        if id:
            arth = arth.filter(id=id)
        if start_date and end_date:
            arth = arth.filter(date_1__range=[start_date,end_date])
        if hour:
            current_time = datetime.now()
            end_date = current_time - timedelta(hours=int(hour))
            arth = arth.filter(date_1__range=(end_date,current_time))
            print (current_time,end_date)

        arth_serializer = Arthematicsserializer(arth,many=True)
        return Response(arth_serializer.data)
    
   
    def post(self,request):
        serializer = Arthematicsserializer(data=request.data)
        if serializer.is_valid():
            final=serializer.save()
            choices = request.data["choicefield"]
            print("valid input")
            first_input = request.data["number_1"]
            second_input = request.data["number_2"]
            if choices == "ADD":
                calculation = first_input+second_input
            elif choices == "SUB":
                calculation = first_input-second_input
            elif choices == "MUL":
                calculation = first_input*second_input
            elif choices == "DIV":
                calculation = first_input%second_input
            final.result = calculation
            final.save()
            print("final value",final)
            return Response(serializer.data)

        else:
            print("invalid input")
            return Response("invalid input")


