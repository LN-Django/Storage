from django.conf.urls import url
from django.urls import path

from .views.storage_info_post import StorageInfoPostView
from .views.storage_info import StorageInfoView

urlpatterns = [
    path('api/storage/<int:product_id>',
         StorageInfoView.as_view(), name='get_single_product_storage_info'),
    url('api/storage', StorageInfoPostView.as_view(), name='storage_info_create'),
]
