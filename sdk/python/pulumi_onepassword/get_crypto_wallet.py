# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import cryptowallet as _cryptowallet
from . import outputs
from ._enums import *

__all__ = [
    'GetCryptoWalletResult',
    'AwaitableGetCryptoWalletResult',
    'get_crypto_wallet',
    'get_crypto_wallet_output',
]

@pulumi.output_type
class GetCryptoWalletResult:
    def __init__(__self__, category=None, fields=None, id=None, notes=None, password=None, recovery_phrase=None, sections=None, tags=None, title=None, uuid=None, vault=None, wallet=None):
        if category and not isinstance(category, dict):
            raise TypeError("Expected argument 'category' to be a dict")
        pulumi.set(__self__, "category", category)
        if fields and not isinstance(fields, list):
            raise TypeError("Expected argument 'fields' to be a list")
        pulumi.set(__self__, "fields", fields)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if notes and not isinstance(notes, str):
            raise TypeError("Expected argument 'notes' to be a str")
        pulumi.set(__self__, "notes", notes)
        if password and not isinstance(password, str):
            raise TypeError("Expected argument 'password' to be a str")
        pulumi.set(__self__, "password", password)
        if recovery_phrase and not isinstance(recovery_phrase, str):
            raise TypeError("Expected argument 'recovery_phrase' to be a str")
        pulumi.set(__self__, "recovery_phrase", recovery_phrase)
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
        if wallet and not isinstance(wallet, dict):
            raise TypeError("Expected argument 'wallet' to be a dict")
        pulumi.set(__self__, "wallet", wallet)

    @property
    @pulumi.getter
    def category(self) -> Optional[str]:
        return pulumi.get(self, "category")

    @property
    @pulumi.getter
    def fields(self) -> Optional[Sequence['outputs.GetField']]:
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def notes(self) -> Optional[str]:
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter
    def password(self) -> Optional[str]:
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="recoveryPhrase")
    def recovery_phrase(self) -> Optional[str]:
        return pulumi.get(self, "recovery_phrase")

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

    @property
    @pulumi.getter
    def wallet(self) -> Optional['_cryptowallet.outputs.Wallet']:
        return pulumi.get(self, "wallet")


class AwaitableGetCryptoWalletResult(GetCryptoWalletResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCryptoWalletResult(
            category=self.category,
            fields=self.fields,
            id=self.id,
            notes=self.notes,
            password=self.password,
            recovery_phrase=self.recovery_phrase,
            sections=self.sections,
            tags=self.tags,
            title=self.title,
            uuid=self.uuid,
            vault=self.vault,
            wallet=self.wallet)


def get_crypto_wallet(title: Optional[str] = None,
                      uuid: Optional[str] = None,
                      vault: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCryptoWalletResult:
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
    __ret__ = pulumi.runtime.invoke('onepassword:index:GetCryptoWallet', __args__, opts=opts, typ=GetCryptoWalletResult).value

    return AwaitableGetCryptoWalletResult(
        category=__ret__.category,
        fields=__ret__.fields,
        id=__ret__.id,
        notes=__ret__.notes,
        password=__ret__.password,
        recovery_phrase=__ret__.recovery_phrase,
        sections=__ret__.sections,
        tags=__ret__.tags,
        title=__ret__.title,
        uuid=__ret__.uuid,
        vault=__ret__.vault,
        wallet=__ret__.wallet)


@_utilities.lift_output_func(get_crypto_wallet)
def get_crypto_wallet_output(title: Optional[pulumi.Input[Optional[str]]] = None,
                             uuid: Optional[pulumi.Input[Optional[str]]] = None,
                             vault: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCryptoWalletResult]:
    """
    Use this data source to access information about an existing resource.

    :param str title: The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
    :param str uuid: The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
    :param str vault: The UUID of the vault the item is in.
    """
    ...
