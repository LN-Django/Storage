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
        type=openapi.TYPE_FILE,
        
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
    }
    )
    
    def post(self, request):
        csv_data = request.data
        try:
            validate_csv_file(csv_data)
        except ValidationError:
            self.logger.info('file is not in CSV format')
            return Response({'message: failed to import csv file'}, status=500)
        return Response(StorageInfoService.importCSV(csv_data))