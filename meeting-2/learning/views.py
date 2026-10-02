from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import ProductSerializer

class Hello(APIView):
    def get(self, request):
        product = {
            "name":"Pizza",
            "price":20.00,
        }
        serializer = ProductSerializer(product)

        return Response(serializer.data)
    
class Desserialization(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     