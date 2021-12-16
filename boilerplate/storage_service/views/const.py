from drf_yasg import openapi

product_properties_storage = {
    'location': openapi.Schema(type=openapi.TYPE_STRING, description='Location of the product'),
    'amount': openapi.Schema(type=openapi.TYPE_INTEGER, description='Remaining amount of the product'),
    'delivery_time': openapi.Schema(type=openapi.TYPE_INTEGER, description='Estimated delivery time of the product'),
    'product_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the product, exported from the application service')
}


product_properties = {
    'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the product (max length: 64 characters.)'),
    'base_price': openapi.Schema(type=openapi.TYPE_NUMBER, description='Base price of the product'),
    'description': openapi.Schema(type=openapi.TYPE_STRING, description='Product description (max length: 128 characters)'),
    'weight': openapi.Schema(type=openapi.TYPE_NUMBER, description='Product weight'),
    'category': openapi.Schema(type=openapi.TYPE_STRING, description='Product category')
}

all_product_properties = {
    **product_properties_storage,
    **product_properties
}

product_properties_info = {
    **all_product_properties,
    'taxed_price': openapi.Schema(type=openapi.TYPE_NUMBER, description='Product price inclusive tax')
}