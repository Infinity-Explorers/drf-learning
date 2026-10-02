from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ProductSerializer

class ProductListAPIView(APIView):
    def get(self, request):
        return Response({"message": "Get product"})
    
    def post(self, request):
        return Response({"message": "Create product"})

    