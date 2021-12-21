from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
import logging

from ..validators import validate_csv_file
from ..services import StorageInfoService
from .const import all_product_properties 


class ImportCsvView(APIView):
    logger = logging.getLogger('mainLogger')
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'text': openapi.Schema(type=openapi.TYPE_STRING, description='csv text'),
        }
        
    ), responses={
        '200': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties=all_product_properties
        ),
        '500': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'message': openapi.Schema(type=openapi.TYPE_STRING, description='Error message'),
            },
            description='Internal server error'
        )
    },
        operation_description='Import product data from a csv text. This operation will overwrite existing products'
    )
    
    def post(self, request):
        key = 'text'
        if key in request.data:
            csv_data = request.data[key]      
            return Response(StorageInfoService.importCSV(csv_data))
        else:
            return Response({'message': 'Bad request: request body is missing'}, status=400)