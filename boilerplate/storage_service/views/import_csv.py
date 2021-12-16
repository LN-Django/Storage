from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
import logging
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
            )
    }
    )
    
    def post(self, request):
        self.logger.info('test log')
        return Response()