from typing import Dict

from pandas.core.indexes import category

from .models import CompleteProduct, Product
from .exceptions import NotFoundError, NotUniqueError

import csv


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

    def importCSV(path):
        with open(path) as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                product, created = CompleteProduct.objects.get_or_create(
                    product_id=row['id'],
                    name=row['name'],
                    base_price=row['base_price'],
                    description=row['description'],
                    location=row['location'],
                    delivery_time=row['delivery_time'],
                    amount=row['amount'],
                    weight=row['weight'],
                    category=row['category'],
                )
                # product = CompleteProduct()
                # product.product_id=row['id']
                # product.name=row['name']
                # product.base_price=row['base_price']
                # product.description=row['description']
                # product.location=row['location']
                # product.delivery_time=row['delivery_time']
                # product.amount=row['amount']
                # product.weight=row['weight']
                # product.category=row['category']
                # product.save()
        f.close()
                    
                