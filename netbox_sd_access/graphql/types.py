from typing import Annotated, List
import strawberry
import strawberry_django
from netbox.graphql.types import NetBoxObjectType
from .. import models
from . import filters

@strawberry_django.type(
    models.IPPool,
    fields='__all__',
    filters=filters.IPPoolFilter
)
class IPPoolType(NetBoxObjectType):
    id: int
    name: str
    prefix: Annotated["PrefixType", strawberry.lazy('ipam.graphql.types')]
    gateway: Annotated["IPAddressType", strawberry.lazy('ipam.graphql.types')]
    dhcp_server: Annotated["IPAddressType", strawberry.lazy('ipam.graphql.types')]
    dns_servers: List[Annotated["IPAddressType", strawberry.lazy('ipam.graphql.types')]]
    
    
@strawberry_django.type(
    models.FabricSite,
    fields='__all__',
    filters=filters.FabricSiteFilter
)
class FabricSiteType(NetBoxObjectType):
    id: int
    name: str
    physical_site: Annotated["SiteType", strawberry.lazy('dcim.graphql.types')]
    location: Annotated["LocationType", strawberry.lazy('dcim.graphql.types')]
    ip_prefixes: List[IPPoolType]
    devices: List[Annotated["DeviceType", strawberry.lazy('dcim.graphql.types')]]
