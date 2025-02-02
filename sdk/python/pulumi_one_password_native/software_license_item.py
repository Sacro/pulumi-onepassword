# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from . import softwarelicense as _softwarelicense
from ._enums import *
from ._inputs import *

__all__ = ['SoftwareLicenseItemArgs', 'SoftwareLicenseItem']

@pulumi.input_type
class SoftwareLicenseItemArgs:
    def __init__(__self__, *,
                 vault: pulumi.Input[str],
                 attachments: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]]]] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 customer: Optional[pulumi.Input['_softwarelicense.CustomerSectionArgs']] = None,
                 fields: Optional[pulumi.Input[Mapping[str, pulumi.Input['FieldArgs']]]] = None,
                 license_key: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 order: Optional[pulumi.Input['_softwarelicense.OrderSectionArgs']] = None,
                 publisher: Optional[pulumi.Input['_softwarelicense.PublisherSectionArgs']] = None,
                 sections: Optional[pulumi.Input[Mapping[str, pulumi.Input['SectionArgs']]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SoftwareLicenseItem resource.
        :param pulumi.Input[str] vault: The UUID of the vault the item is in.
        :param pulumi.Input[str] category: The category of the vault the item is in.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: An array of strings of the tags assigned to the item.
        :param pulumi.Input[str] title: The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
        """
        pulumi.set(__self__, "vault", vault)
        if attachments is not None:
            pulumi.set(__self__, "attachments", attachments)
        if category is not None:
            pulumi.set(__self__, "category", 'Software License')
        if customer is not None:
            pulumi.set(__self__, "customer", customer)
        if fields is not None:
            pulumi.set(__self__, "fields", fields)
        if license_key is not None:
            pulumi.set(__self__, "license_key", license_key)
        if notes is not None:
            pulumi.set(__self__, "notes", notes)
        if order is not None:
            pulumi.set(__self__, "order", order)
        if publisher is not None:
            pulumi.set(__self__, "publisher", publisher)
        if sections is not None:
            pulumi.set(__self__, "sections", sections)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if title is not None:
            pulumi.set(__self__, "title", title)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def vault(self) -> pulumi.Input[str]:
        """
        The UUID of the vault the item is in.
        """
        return pulumi.get(self, "vault")

    @vault.setter
    def vault(self, value: pulumi.Input[str]):
        pulumi.set(self, "vault", value)

    @property
    @pulumi.getter
    def attachments(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]]]]:
        return pulumi.get(self, "attachments")

    @attachments.setter
    def attachments(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]]]]):
        pulumi.set(self, "attachments", value)

    @property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[str]]:
        """
        The category of the vault the item is in.
        """
        return pulumi.get(self, "category")

    @category.setter
    def category(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "category", value)

    @property
    @pulumi.getter
    def customer(self) -> Optional[pulumi.Input['_softwarelicense.CustomerSectionArgs']]:
        return pulumi.get(self, "customer")

    @customer.setter
    def customer(self, value: Optional[pulumi.Input['_softwarelicense.CustomerSectionArgs']]):
        pulumi.set(self, "customer", value)

    @property
    @pulumi.getter
    def fields(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['FieldArgs']]]]:
        return pulumi.get(self, "fields")

    @fields.setter
    def fields(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['FieldArgs']]]]):
        pulumi.set(self, "fields", value)

    @property
    @pulumi.getter(name="licenseKey")
    def license_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "license_key")

    @license_key.setter
    def license_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "license_key", value)

    @property
    @pulumi.getter
    def notes(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "notes")

    @notes.setter
    def notes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notes", value)

    @property
    @pulumi.getter
    def order(self) -> Optional[pulumi.Input['_softwarelicense.OrderSectionArgs']]:
        return pulumi.get(self, "order")

    @order.setter
    def order(self, value: Optional[pulumi.Input['_softwarelicense.OrderSectionArgs']]):
        pulumi.set(self, "order", value)

    @property
    @pulumi.getter
    def publisher(self) -> Optional[pulumi.Input['_softwarelicense.PublisherSectionArgs']]:
        return pulumi.get(self, "publisher")

    @publisher.setter
    def publisher(self, value: Optional[pulumi.Input['_softwarelicense.PublisherSectionArgs']]):
        pulumi.set(self, "publisher", value)

    @property
    @pulumi.getter
    def sections(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['SectionArgs']]]]:
        return pulumi.get(self, "sections")

    @sections.setter
    def sections(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['SectionArgs']]]]):
        pulumi.set(self, "sections", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An array of strings of the tags assigned to the item.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        """
        The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


@pulumi.input_type
class _SoftwareLicenseItemState:
    def __init__(__self__, *,
                 vault: pulumi.Input[str]):
        """
        Input properties used for looking up and filtering SoftwareLicenseItem resources.
        :param pulumi.Input[str] vault: The UUID of the vault the item is in.
        """
        pulumi.set(__self__, "vault", vault)

    @property
    @pulumi.getter
    def vault(self) -> pulumi.Input[str]:
        """
        The UUID of the vault the item is in.
        """
        return pulumi.get(self, "vault")

    @vault.setter
    def vault(self, value: pulumi.Input[str]):
        pulumi.set(self, "vault", value)


class SoftwareLicenseItem(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attachments: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]]]] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 customer: Optional[pulumi.Input[pulumi.InputType['_softwarelicense.CustomerSectionArgs']]] = None,
                 fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['FieldArgs']]]]] = None,
                 license_key: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 order: Optional[pulumi.Input[pulumi.InputType['_softwarelicense.OrderSectionArgs']]] = None,
                 publisher: Optional[pulumi.Input[pulumi.InputType['_softwarelicense.PublisherSectionArgs']]] = None,
                 sections: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['SectionArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 vault: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a SoftwareLicenseItem resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] category: The category of the vault the item is in.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: An array of strings of the tags assigned to the item.
        :param pulumi.Input[str] title: The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
        :param pulumi.Input[str] vault: The UUID of the vault the item is in.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SoftwareLicenseItemArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a SoftwareLicenseItem resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param SoftwareLicenseItemArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SoftwareLicenseItemArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attachments: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]]]] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 customer: Optional[pulumi.Input[pulumi.InputType['_softwarelicense.CustomerSectionArgs']]] = None,
                 fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['FieldArgs']]]]] = None,
                 license_key: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 order: Optional[pulumi.Input[pulumi.InputType['_softwarelicense.OrderSectionArgs']]] = None,
                 publisher: Optional[pulumi.Input[pulumi.InputType['_softwarelicense.PublisherSectionArgs']]] = None,
                 sections: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['SectionArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 vault: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SoftwareLicenseItemArgs.__new__(SoftwareLicenseItemArgs)

            __props__.__dict__["attachments"] = attachments
            __props__.__dict__["category"] = 'Software License'
            __props__.__dict__["customer"] = customer
            __props__.__dict__["fields"] = fields
            __props__.__dict__["license_key"] = license_key
            __props__.__dict__["notes"] = notes
            __props__.__dict__["order"] = order
            __props__.__dict__["publisher"] = publisher
            __props__.__dict__["sections"] = sections
            __props__.__dict__["tags"] = tags
            __props__.__dict__["title"] = title
            if vault is None and not opts.urn:
                raise TypeError("Missing required property 'vault'")
            __props__.__dict__["vault"] = vault
            __props__.__dict__["version"] = version
            __props__.__dict__["references"] = None
            __props__.__dict__["uuid"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["attachments", "fields", "references", "sections"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(SoftwareLicenseItem, __self__).__init__(
            'one-password-native:index:SoftwareLicenseItem',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            vault: Optional[pulumi.Input[str]] = None) -> 'SoftwareLicenseItem':
        """
        Get an existing SoftwareLicenseItem resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] vault: The UUID of the vault the item is in.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SoftwareLicenseItemState.__new__(_SoftwareLicenseItemState)

        __props__.__dict__["vault"] = vault
        __props__.__dict__["attachments"] = None
        __props__.__dict__["category"] = None
        __props__.__dict__["customer"] = None
        __props__.__dict__["fields"] = None
        __props__.__dict__["license_key"] = None
        __props__.__dict__["notes"] = None
        __props__.__dict__["order"] = None
        __props__.__dict__["publisher"] = None
        __props__.__dict__["references"] = None
        __props__.__dict__["sections"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["title"] = None
        __props__.__dict__["uuid"] = None
        __props__.__dict__["version"] = None
        return SoftwareLicenseItem(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def attachments(self) -> pulumi.Output[Mapping[str, 'outputs.OutField']]:
        return pulumi.get(self, "attachments")

    @property
    @pulumi.getter
    def category(self) -> pulumi.Output[str]:
        return pulumi.get(self, "category")

    @property
    @pulumi.getter
    def customer(self) -> pulumi.Output[Optional['_softwarelicense.outputs.CustomerSection']]:
        return pulumi.get(self, "customer")

    @property
    @pulumi.getter
    def fields(self) -> pulumi.Output[Mapping[str, 'outputs.OutField']]:
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter(name="licenseKey")
    def license_key(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "license_key")

    @property
    @pulumi.getter
    def notes(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter
    def order(self) -> pulumi.Output[Optional['_softwarelicense.outputs.OrderSection']]:
        return pulumi.get(self, "order")

    @property
    @pulumi.getter
    def publisher(self) -> pulumi.Output[Optional['_softwarelicense.outputs.PublisherSection']]:
        return pulumi.get(self, "publisher")

    @property
    @pulumi.getter
    def references(self) -> pulumi.Output[Mapping[str, 'outputs.OutField']]:
        return pulumi.get(self, "references")

    @property
    @pulumi.getter
    def sections(self) -> pulumi.Output[Mapping[str, 'outputs.OutSection']]:
        return pulumi.get(self, "sections")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence[str]]:
        """
        An array of strings of the tags assigned to the item.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[str]:
        """
        The title of the item.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def uuid(self) -> pulumi.Output[str]:
        """
        The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
        """
        return pulumi.get(self, "uuid")

    @property
    @pulumi.getter
    def vault(self) -> pulumi.Output[str]:
        """
        The UUID of the vault the item is in.
        """
        return pulumi.get(self, "vault")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "version")

    @pulumi.output_type
    class GetAttachmentResult:
        """
        The resolved reference value
        """
        def __init__(__self__, value=None):
            if value and not isinstance(value, str):
                raise TypeError("Expected argument 'value' to be a str")
            pulumi.set(__self__, "value", value)

        @property
        @pulumi.getter
        def value(self) -> str:
            """
            the value of the attachment
            """
            return pulumi.get(self, "value")

    def get_attachment(__self__, *,
                       name: pulumi.Input[str]) -> pulumi.Output['SoftwareLicenseItem.GetAttachmentResult']:
        """

        :param pulumi.Input[str] name: The name or uuid of the attachment to get
        """
        __args__ = dict()
        __args__['__self__'] = __self__
        __args__['name'] = name
        return pulumi.runtime.call('one-password-native:index:SoftwareLicenseItem/attachment', __args__, res=__self__, typ=SoftwareLicenseItem.GetAttachmentResult)

