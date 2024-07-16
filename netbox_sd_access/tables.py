import django_tables2 as tables
from netbox.tables import NetBoxTable, ChoiceFieldColumn

from .models import *


class SDAccessTable(NetBoxTable):
    name = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = SDAccess
        fields = ("pk", "id", "name", "actions")
        default_columns = ("name",)

class FabricSiteTable(NetBoxTable):
    name = tables.Column(linkify=True)
    
    class Meta(NetBoxTable.Meta):
        model = FabricSite
        fields = ("pk", "id", "name", "physical_site", "location", "ip_prefixes", "device_count", "actions")
        default_columns = ("name", "physical_site", "location", "device_count")

class SDADeviceTable(NetBoxTable):
    id = tables.Column(linkify=True)
    device = tables.Column(linkify=True)
    fabric_site = tables.Column(linkify=True)
    role = ChoiceFieldColumn()
    
    class Meta(NetBoxTable.Meta):
        model = SDADevice
        fields = ('pk', 'id', 'device', 'role', 'fabric_site', 'actions')
        default_columns = ('id', 'device', 'role', 'fabric_site')