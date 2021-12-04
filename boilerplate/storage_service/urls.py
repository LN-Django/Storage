from rest_framework import routers

from .views.storage_info import StorageInfoView

from django.conf.urls import url

urlpatterns = [
    url('api/storage', StorageInfoView.as_view())
]
