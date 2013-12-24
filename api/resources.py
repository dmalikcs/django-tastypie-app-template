from tastypie.resources import ModelResource
from tastypie.authentication import Authentication, ApiKeyAuthentication
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization, Authorization, ReadOnlyAuthorization
from tastypie.serializers import Serializer
from tastypie.throttle import CacheDBThrottle

from tastypie import fields

from {{ app_name }}.models import *


class DemoResource(ModelResource):
    class Meta:
        queryset = DemaModel.objects.all()
        resource_name = 'demo_resource_name'
        allowed_methods = ['get', 'post', ]
