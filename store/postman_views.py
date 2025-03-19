from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
from store.models import Product  # Import your Product model

@csrf_exempt  # Disable CSRF for testing (not recommended for production)
def product_api(request, product_id=None):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            product = Product.objects.create(
                name=data["name"],
                description=data["description"],
                price=data["price"]
            )
            return JsonResponse({"message": "Product added successfully!", "product_id": product.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    elif request.method == "PUT" and product_id:
        product = get_object_or_404(Product, id=product_id)
        try:
            data = json.loads(request.body)
            product.name = data.get("name", product.name)
            product.description = data.get("description", product.description)
            product.price = data.get("price", product.price)
            product.save()
            return JsonResponse({"message": "Product updated successfully!", "product_id": product.id}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    elif request.method == "DELETE" and product_id:
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        return JsonResponse({"message": "Product deleted successfully!", "product_id": product_id}, status=200)

    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)
