# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from . import rewardprogram as _rewardprogram
from ._enums import *

__all__ = [
    'GetRewardProgramResult',
    'AwaitableGetRewardProgramResult',
    'get_reward_program',
    'get_reward_program_output',
]

@pulumi.output_type
class GetRewardProgramResult:
    def __init__(__self__, category=None, company_name=None, fields=None, id=None, member_id=None, member_name=None, more_information=None, notes=None, pin=None, sections=None, tags=None, title=None, uuid=None, vault=None):
        if category and not isinstance(category, dict):
            raise TypeError("Expected argument 'category' to be a dict")
        pulumi.set(__self__, "category", category)
        if company_name and not isinstance(company_name, str):
            raise TypeError("Expected argument 'company_name' to be a str")
        pulumi.set(__self__, "company_name", company_name)
        if fields and not isinstance(fields, list):
            raise TypeError("Expected argument 'fields' to be a list")
        pulumi.set(__self__, "fields", fields)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if member_id and not isinstance(member_id, str):
            raise TypeError("Expected argument 'member_id' to be a str")
        pulumi.set(__self__, "member_id", member_id)
        if member_name and not isinstance(member_name, str):
            raise TypeError("Expected argument 'member_name' to be a str")
        pulumi.set(__self__, "member_name", member_name)
        if more_information and not isinstance(more_information, dict):
            raise TypeError("Expected argument 'more_information' to be a dict")
        pulumi.set(__self__, "more_information", more_information)
        if notes and not isinstance(notes, str):
            raise TypeError("Expected argument 'notes' to be a str")
        pulumi.set(__self__, "notes", notes)
        if pin and not isinstance(pin, str):
            raise TypeError("Expected argument 'pin' to be a str")
        pulumi.set(__self__, "pin", pin)
        if sections and not isinstance(sections, list):
            raise TypeError("Expected argument 'sections' to be a list")
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
    def category(self) -> Optional[str]:
        return pulumi.get(self, "category")

    @property
    @pulumi.getter(name="companyName")
    def company_name(self) -> Optional[str]:
        return pulumi.get(self, "company_name")

    @property
    @pulumi.getter
    def fields(self) -> Optional[Sequence['outputs.GetField']]:
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="memberId")
    def member_id(self) -> Optional[str]:
        return pulumi.get(self, "member_id")

    @property
    @pulumi.getter(name="memberName")
    def member_name(self) -> Optional[str]:
        return pulumi.get(self, "member_name")

    @property
    @pulumi.getter(name="moreInformation")
    def more_information(self) -> Optional['_rewardprogram.outputs.MoreInformation']:
        return pulumi.get(self, "more_information")

    @property
    @pulumi.getter
    def notes(self) -> Optional[str]:
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter
    def pin(self) -> Optional[str]:
        return pulumi.get(self, "pin")

    @property
    @pulumi.getter
    def sections(self) -> Optional[Sequence['outputs.GetSection']]:
        return pulumi.get(self, "sections")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence[str]]:
        """
        An array of strings of the tags assigned to the item.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def title(self) -> Optional[str]:
        """
        The title of the item.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def uuid(self) -> Optional[str]:
        """
        The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
        """
        return pulumi.get(self, "uuid")

    @property
    @pulumi.getter
    def vault(self) -> Optional[str]:
        """
        The UUID of the vault the item is in.
        """
        return pulumi.get(self, "vault")


class AwaitableGetRewardProgramResult(GetRewardProgramResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRewardProgramResult(
            category=self.category,
            company_name=self.company_name,
            fields=self.fields,
            id=self.id,
            member_id=self.member_id,
            member_name=self.member_name,
            more_information=self.more_information,
            notes=self.notes,
            pin=self.pin,
            sections=self.sections,
            tags=self.tags,
            title=self.title,
            uuid=self.uuid,
            vault=self.vault)


def get_reward_program(title: Optional[str] = None,
                       uuid: Optional[str] = None,
                       vault: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRewardProgramResult:
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
    __ret__ = pulumi.runtime.invoke('onepassword:index:GetRewardProgram', __args__, opts=opts, typ=GetRewardProgramResult).value

    return AwaitableGetRewardProgramResult(
        category=__ret__.category,
        company_name=__ret__.company_name,
        fields=__ret__.fields,
        id=__ret__.id,
        member_id=__ret__.member_id,
        member_name=__ret__.member_name,
        more_information=__ret__.more_information,
        notes=__ret__.notes,
        pin=__ret__.pin,
        sections=__ret__.sections,
        tags=__ret__.tags,
        title=__ret__.title,
        uuid=__ret__.uuid,
        vault=__ret__.vault)


@_utilities.lift_output_func(get_reward_program)
def get_reward_program_output(title: Optional[pulumi.Input[Optional[str]]] = None,
                              uuid: Optional[pulumi.Input[Optional[str]]] = None,
                              vault: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRewardProgramResult]:
    """
    Use this data source to access information about an existing resource.

    :param str title: The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
    :param str uuid: The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
    :param str vault: The UUID of the vault the item is in.
    """
    ...
