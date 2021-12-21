from typing import Dict

from .models import CompleteProduct, Product
from .exceptions import NotFoundError, NotUniqueError

from io import StringIO
import csv
from django.forms.models import model_to_dict


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

    def importCSV(str):
        '''
        Method to import csv string to models
        '''
        products = []
        f = StringIO(str)
        reader = csv.reader(f, delimiter=",")
        CompleteProduct.objects.all().delete()
        for row in reader:
            product, created = CompleteProduct.objects.get_or_create(
                product_id=row[0],
                name=row[1],
                base_price=row[2],
                description=row[3],
                location=row[4],
                delivery_time=row[5],
                amount=row[6],
                weight=row[7],
                category=row[8],
            )
            if created:
                product.save()
                product_dict = model_to_dict(product)
                products.append(product_dict)
            else:
                return created
        f.close()
        return products
                    
                