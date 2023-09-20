from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

class Arthematiclist(APIView):
    def post (self, request):
        print (request.data)
        Arthematics = ["ADD","SUB","MUL","DIV"] 


        choices = request.data["choices"]
        if choices in Arthematics:
            print("valid input")
            first_input = request.data["first_value"]
            second_input = request.data["second_value"]
            if choices == "ADD":
                calculation = first_input+second_input
            elif choices == "SUB":
                calculation = first_input-second_input
            elif choices == "MUL":
                calculation = first_input*second_input
            elif choices == "DIV":
                calculation = first_input%second_input
            final = calculation
            print("final value",final)
            return Response(f"output : {final}")

        else:
            print("invalid input")
            return Response("invalid input")