from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')


# 
# Product  
# --------------------------
# name : String (max_length=100)
# description : String (text)
# price : DecimalField (max_digits=10, decimal_places=2)
# image : ImageField (upload_to='product_images/')

# 
# 
# 
# products = Product.objects.all()

# product =  Product(
#     name="laptop",
#     price=20000,
#     description="Best laptop for gaming",
#     image="https://unsplash.com/photos/black-and-silver-laptop-on-white-table-V14hT658-p0"
# )

# # product.save() 