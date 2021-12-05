from rest_framework import routers

from .views.storage_info_post import StorageInfoPostView

from .views.storage_info import StorageInfoView

from django.conf.urls import url

urlpatterns = [
    url('api/storage', StorageInfoPostView.as_view(), name='storage_info_create')
]
