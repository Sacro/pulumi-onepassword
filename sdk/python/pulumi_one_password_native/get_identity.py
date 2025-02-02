# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import identity as _identity
from . import outputs
from ._enums import *

__all__ = [
    'GetIdentityResult',
    'AwaitableGetIdentityResult',
    'get_identity',
    'get_identity_output',
]

@pulumi.output_type
class GetIdentityResult:
    def __init__(__self__, address=None, attachments=None, category=None, fields=None, identification=None, internet_details=None, notes=None, references=None, sections=None, tags=None, title=None, uuid=None, vault=None):
        if address and not isinstance(address, dict):
            raise TypeError("Expected argument 'address' to be a dict")
        pulumi.set(__self__, "address", address)
        if attachments and not isinstance(attachments, dict):
            raise TypeError("Expected argument 'attachments' to be a dict")
        pulumi.set(__self__, "attachments", attachments)
        if category and not isinstance(category, dict):
            raise TypeError("Expected argument 'category' to be a dict")
        pulumi.set(__self__, "category", category)
        if fields and not isinstance(fields, dict):
            raise TypeError("Expected argument 'fields' to be a dict")
        pulumi.set(__self__, "fields", fields)
        if identification and not isinstance(identification, dict):
            raise TypeError("Expected argument 'identification' to be a dict")
        pulumi.set(__self__, "identification", identification)
        if internet_details and not isinstance(internet_details, dict):
            raise TypeError("Expected argument 'internet_details' to be a dict")
        pulumi.set(__self__, "internet_details", internet_details)
        if notes and not isinstance(notes, str):
            raise TypeError("Expected argument 'notes' to be a str")
        pulumi.set(__self__, "notes", notes)
        if references and not isinstance(references, dict):
            raise TypeError("Expected argument 'references' to be a dict")
        pulumi.set(__self__, "references", references)
        if sections and not isinstance(sections, dict):
            raise TypeError("Expected argument 'sections' to be a dict")
        pulumi.set(__self__, "sections", sections)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if title and not isinstance(title, str):
            raise TypeError("Expected argument 'title' to be a str")
        pulumi.set(__self__, "title", title)
        if uuid and not isinstance(uuid, str):
            raise TypeError("Expected argument 'uuid' to be a str")
        pulumi.set(__self__, "uuid", uuid)
        if vault and not isinstance(vault, str):
            raise TypeError("Expected argument 'vault' to be a str")
        pulumi.set(__self__, "vault", vault)

    @property
    @pulumi.getter
    def address(self) -> Optional['_identity.outputs.AddressSection']:
        return pulumi.get(self, "address")

    @property
    @pulumi.getter
    def attachments(self) -> Mapping[str, 'outputs.OutField']:
        return pulumi.get(self, "attachments")

    @property
    @pulumi.getter
    def category(self) -> str:
        return pulumi.get(self, "category")

    @property
    @pulumi.getter
    def fields(self) -> Mapping[str, 'outputs.OutField']:
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter
    def identification(self) -> Optional['_identity.outputs.IdentificationSection']:
        return pulumi.get(self, "identification")

    @property
    @pulumi.getter(name="internetDetails")
    def internet_details(self) -> Optional['_identity.outputs.InternetDetailsSection']:
        return pulumi.get(self, "internet_details")

    @property
    @pulumi.getter
    def notes(self) -> Optional[str]:
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter
    def references(self) -> Mapping[str, 'outputs.OutField']:
        return pulumi.get(self, "references")

    @property
    @pulumi.getter
    def sections(self) -> Mapping[str, 'outputs.OutSection']:
        return pulumi.get(self, "sections")

    @property
    @pulumi.getter
    def tags(self) -> Sequence[str]:
        """
        An array of strings of the tags assigned to the item.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def title(self) -> str:
        """
        The title of the item.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def uuid(self) -> str:
        """
        The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
        """
        return pulumi.get(self, "uuid")

    @property
    @pulumi.getter
    def vault(self) -> str:
        """
        The UUID of the vault the item is in.
        """
        return pulumi.get(self, "vault")


class AwaitableGetIdentityResult(GetIdentityResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIdentityResult(
            address=self.address,
            attachments=self.attachments,
            category=self.category,
            fields=self.fields,
            identification=self.identification,
            internet_details=self.internet_details,
            notes=self.notes,
            references=self.references,
            sections=self.sections,
            tags=self.tags,
            title=self.title,
            uuid=self.uuid,
            vault=self.vault)


def get_identity(title: Optional[str] = None,
                 uuid: Optional[str] = None,
                 vault: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIdentityResult:
    """
    Use this data source to access information about an existing resource.

    :param str title: The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
    :param str uuid: The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
    :param str vault: The UUID of the vault the item is in.
    """
    __args__ = dict()
    __args__['title'] = title
    __args__['uuid'] = uuid
    __args__['vault'] = vault
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('one-password-native:index:GetIdentity', __args__, opts=opts, typ=GetIdentityResult).value

    return AwaitableGetIdentityResult(
        address=__ret__.address,
        attachments=__ret__.attachments,
        category=__ret__.category,
        fields=__ret__.fields,
        identification=__ret__.identification,
        internet_details=__ret__.internet_details,
        notes=__ret__.notes,
        references=__ret__.references,
        sections=__ret__.sections,
        tags=__ret__.tags,
        title=__ret__.title,
        uuid=__ret__.uuid,
        vault=__ret__.vault)


@_utilities.lift_output_func(get_identity)
def get_identity_output(title: Optional[pulumi.Input[Optional[str]]] = None,
                        uuid: Optional[pulumi.Input[Optional[str]]] = None,
                        vault: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIdentityResult]:
    """
    Use this data source to access information about an existing resource.

    :param str title: The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
    :param str uuid: The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
    :param str vault: The UUID of the vault the item is in.
    """
    ...
