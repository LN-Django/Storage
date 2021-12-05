from drf_yasg import openapi

product_properties = {
    'location': openapi.Schema(type=openapi.TYPE_STRING, description='Location of the product'),
    'amount': openapi.Schema(type=openapi.TYPE_INTEGER, description='Remaining amount of the product'),
    'delivery_time': openapi.Schema(type=openapi.TYPE_INTEGER, description='Estimated delivery time of the product'),
    'product_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the product, exported from the application service')
}
