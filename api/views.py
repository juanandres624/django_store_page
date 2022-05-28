from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from store.models import Product
from category.models import Category

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/greatkart/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an Array'
        },
        {
            'Endpoint': '/greatkart/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a Single'
        },
        {
            'Endpoint': '/greatkart/create/',
            'method': 'POST',
            'body': {'body':""},
            'description': 'Creates a New Prod'
        },
        {
            'Endpoint': '/greatkart/id/update/',
            'method': 'PUT',
            'body': {'body':""},
            'description': 'Updates and existing product'
        },
        {
            'Endpoint':'/greatkart/id/delete/',
            'method':'DELETE',
            'body':None,
            'description': 'Deletes and existing product'
        }
    ]
    return Response(routes)

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createProduct(request):
    data = request.data

    product = Product.objects.create(
    product_name    = data['product_name'],
    slug            = data['slug'],
    description     = data['description'],
    price           = data['price'],
    category        = Category.objects.get(id=data['category']),
    stock           = data['stock']
    )
    serializer = ProductSerializer(product,many=False)
    return Response(serializer.data)

@api_view(['GET','PUT'])
def updateProduct(request, pk):
    data = request.data

    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteProduct(request, pk):
    data = request.data

    product = Product.objects.get(id=pk)
    product.delete()
    return Response('Product was Deleted!')