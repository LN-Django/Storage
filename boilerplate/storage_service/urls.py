from django.conf.urls import url
from django.urls import path

from .views.storage_info_post import StorageInfoPostView
from .views.storage_info import StorageInfoView
from .views.import_csv import ImportCsvView
from .views.import_product_info import ImportProductInfo

urlpatterns = [
    path('api/storage/<int:product_id>',
         StorageInfoView.as_view(), name='get_single_product_storage_info'),
    url('api/storage', StorageInfoPostView.as_view(), name='storage_info_create'),
    url('api/import_csv', ImportCsvView.as_view(), name='import_csv'),
    url('api/import_product_info', ImportProductInfo.as_view(), name='import_product_info'),
]
