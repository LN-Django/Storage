from typing import Dict

from .models import Product
from .exceptions import NotFoundError, NotUniqueError


class StorageInfoService():
    def post_storage_information(storage_data: Dict) -> Dict:
        """Method to post storage information"""

        queryset = Product.objects.filter(
            product_id=storage_data['product_id'])

        if queryset.count() != 0:
            raise NotUniqueError()

        product: Product = Product.objects.create(
            location=storage_data['location'], amount=storage_data['amount'],
            delivery_time=storage_data['delivery_time'], product_id=storage_data['product_id'])

        response_data = storage_data
        del response_data['id']
        return response_data

    def get_storage_information_by_product_id(product_id: int) -> Product:
        """Method to get storage information of a single product by its product id"""
        queryset = Product.objects.filter(product_id=product_id)
        product_count = queryset.count()
        if product_count == 0:
            raise NotFoundError()
        elif product_count > 1:
            raise NotUniqueError()

        return queryset.values()[0]
