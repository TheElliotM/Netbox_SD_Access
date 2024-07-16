from django import forms
from ipam.models import Prefix
from dcim.models import Site, Location, Device
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField, DynamicModelMultipleChoiceField

from .models import *


class SDAccessForm(NetBoxModelForm):
    class Meta:
        model = SDAccess
        fields = ("name", "tags")

class FabricSiteForm(NetBoxModelForm):
    physical_site = DynamicModelChoiceField(queryset=Site.objects.all(),required=True)
    location = DynamicModelChoiceField(queryset=Location.objects.all(), required=False, query_params={'site_id': '$physical_site'} )
    ip_prefixes = DynamicModelMultipleChoiceField(queryset=Prefix.objects.all(), required=True, label='IP Prefixes')
    
    class Meta:
        model = FabricSite
        fields = ('name', 'physical_site', 'location', 'ip_prefixes')

class FabricSiteFilterForm(NetBoxModelFilterSetForm):
    model = FabricSite
    physical_site = forms.ModelMultipleChoiceField(
        queryset=Site.objects.all(),
        required=False
    )

class SDADeviceForm(NetBoxModelForm):
    physical_site = DynamicModelChoiceField(queryset=Site.objects.all(), required=False)
    location = DynamicModelChoiceField(queryset=Location.objects.all(), required=False, query_params={'site_id': '$physical_site'})
    fabric_site = DynamicModelChoiceField(
        queryset=FabricSite.objects.all(), 
        required=True,
        query_params={'physical_site': '$physical_site', 'location': '$location'}
    )
    device = DynamicModelChoiceField(
        queryset=Device.objects.all(), 
        required=True, 
        query_params={'site_id': '$physical_site', 'location_id': '$location'}
    )
    
    class Meta:
        model = SDADevice
        fields = ('physical_site', 'location', 'fabric_site', 'device', 'role',)

class SDADeviceFilterForm(NetBoxModelFilterSetForm):
    model = SDADevice
    site = forms.ModelChoiceField(queryset=FabricSite.objects.all(), required=False)
    role = forms.MultipleChoiceField(choices=SDADeviceRoleChoices, required=False, initial=None)