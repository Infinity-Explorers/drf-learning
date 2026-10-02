from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from django.db.models import Q

# Create your views here.

class ProductListView(APIView):
    def get(self, request):
        return Response({
            "products": Product.objects.all()
        })
        product = Product.objects.create(
            name='laptop',
            price=20000,
            description='Best laptop for gaming',
            image='https://unsplash.com/photos/black-and-silver-laptop-on-white-table-V14hT658-p0'
        )
        product.save()
        return Response({
            "message": "Product created successfully"
        })   

        # product = Product.objects.get(id=1)
        # product.price = 3
        # product.save()

        # product = Product .objects.filter(id=2).update(price=1)

        # products = Product.objects.all()
        # products = Product.filter(price__gte=1000)
        # products = Product.filter(price__lte=50000)
        # products = Product.filter(name__startswith='l')
        

        products = (
            Product.objects
            .filter(price__gte=1000)
            .filter(
                price__lte=50000
            )
            .filter(name__startswith='l')
        )
        Product.objects.order_by("price")

        products = Product.objects.filter(
                price__lte=50000,
                name="laptop"
            )

        products = Product.objects.filter(
                Q(price__lte=50000) &
                Q(name="laptop")
            )