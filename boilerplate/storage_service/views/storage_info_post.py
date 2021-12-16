import logging
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.core.exceptions import ValidationError


from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .const import product_properties_storage
from ..serializers import ProductSerializer
from ..services import StorageInfoService
from ..exceptions import NotUniqueError


class StorageInfoPostView(APIView):
    permission_classes = [permissions.AllowAny]
    logger = logging.getLogger('mainLogger')

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties=product_properties_storage,

    ), responses={
        '201': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties=product_properties_storage),
        '400': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'message': openapi.Schema(type=openapi.TYPE_STRING, description='Error message'),
                'errors': openapi.Schema(type=openapi.TYPE_OBJECT, description='Django auto-generated errors via serializer')
            },
            description='Invalid parameter'
        )
    })
    def post(self, request, format=None):
        """Post a new entry of storage informations for a product"""
        request_data = JSONParser().parse(request)
        new_product = ProductSerializer(data=request_data)

        if not new_product.is_valid():
            self.logger.info('Product data serializer error')
            return Response({'message': 'Bad request: invalid parameter', 'errors': new_product.errors}, status=400)

        try:
            return_data = StorageInfoService.post_storage_information(
                new_product.data)
            return Response(return_data, status=201)
        except ValidationError as error:
            self.logger.info('Validation error while creating product')
            return Response({'message': 'Bad request: validation error', 'errors': error}, status=400)
        except NotUniqueError as error:
            self.logger.info('Non unique error while posting storage info')
            return Response({'message': 'Bad request: Info of the product with the product id {:d} already exists'.format(request_data['product_id'])}, status=400)
