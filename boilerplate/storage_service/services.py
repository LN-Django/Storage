from typing import Dict

from .models import Product


class StorageInfoService():
    def post_storage_information(storage_data: Dict) -> Dict:
        """Method to post storage information"""
        product: Product = Product.objects.create(
            location=storage_data['location'], amount=storage_data['amount'],
            delivery_time=storage_data['delivery_time'], product_id=storage_data['product_id'])

        response_data = storage_data
        response_data['id'] = product.id
        return response_data
