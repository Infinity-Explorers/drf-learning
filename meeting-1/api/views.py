from django.http import JsonResponse

def hello_api(request):
    return JsonResponse({"message": "Hello from django api"})


def good_by_api(request):
    return JsonResponse({"message": "good by from django"})

def product_api(request):
    products = [
        {
            "id":1,
            "name":"Pizza",
            "price": 100,
        },
    ]
    return JsonResponse(products , safe=False)