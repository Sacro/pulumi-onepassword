# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['DriverLicenseItemArgs', 'DriverLicenseItem']

@pulumi.input_type
class DriverLicenseItemArgs:
    def __init__(__self__, *,
                 vault: pulumi.Input[str],
                 address: Optional[pulumi.Input[str]] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 conditions_restrictions: Optional[pulumi.Input[str]] = None,
                 country: Optional[pulumi.Input[str]] = None,
                 date_of_birth: Optional[pulumi.Input[str]] = None,
                 expiry_date: Optional[pulumi.Input[str]] = None,
                 fields: Optional[pulumi.Input[Mapping[str, pulumi.Input['FieldArgs']]]] = None,
                 full_name: Optional[pulumi.Input[str]] = None,
                 gender: Optional[pulumi.Input[str]] = None,
                 height: Optional[pulumi.Input[str]] = None,
                 license_class: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 number: Optional[pulumi.Input[str]] = None,
                 sections: Optional[pulumi.Input[Mapping[str, pulumi.Input['SectionArgs']]]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 title: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DriverLicenseItem resource.
        :param pulumi.Input[str] vault: The UUID of the vault the item is in.
        :param pulumi.Input[str] category: The category of the vault the item is in.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: An array of strings of the tags assigned to the item.
        :param pulumi.Input[str] title: The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
        """
        pulumi.set(__self__, "vault", vault)
        if address is not None:
            pulumi.set(__self__, "address", address)
        if category is not None:
            pulumi.set(__self__, "category", 'Driver License')
        if conditions_restrictions is not None:
            pulumi.set(__self__, "conditions_restrictions", conditions_restrictions)
        if country is not None:
            pulumi.set(__self__, "country", country)
        if date_of_birth is not None:
            pulumi.set(__self__, "date_of_birth", date_of_birth)
        if expiry_date is not None:
            pulumi.set(__self__, "expiry_date", expiry_date)
        if fields is not None:
            pulumi.set(__self__, "fields", fields)
        if full_name is not None:
            pulumi.set(__self__, "full_name", full_name)
        if gender is not None:
            pulumi.set(__self__, "gender", gender)
        if height is not None:
            pulumi.set(__self__, "height", height)
        if license_class is not None:
            pulumi.set(__self__, "license_class", license_class)
        if notes is not None:
            pulumi.set(__self__, "notes", notes)
        if number is not None:
            pulumi.set(__self__, "number", number)
        if sections is not None:
            pulumi.set(__self__, "sections", sections)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if title is not None:
            pulumi.set(__self__, "title", title)

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
    def address(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "address")

    @address.setter
    def address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address", value)

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
    @pulumi.getter(name="conditionsRestrictions")
    def conditions_restrictions(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "conditions_restrictions")

    @conditions_restrictions.setter
    def conditions_restrictions(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "conditions_restrictions", value)

    @property
    @pulumi.getter
    def country(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "country")

    @country.setter
    def country(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "country", value)

    @property
    @pulumi.getter(name="dateOfBirth")
    def date_of_birth(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "date_of_birth")

    @date_of_birth.setter
    def date_of_birth(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "date_of_birth", value)

    @property
    @pulumi.getter(name="expiryDate")
    def expiry_date(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "expiry_date")

    @expiry_date.setter
    def expiry_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiry_date", value)

    @property
    @pulumi.getter
    def fields(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['FieldArgs']]]]:
        return pulumi.get(self, "fields")

    @fields.setter
    def fields(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['FieldArgs']]]]):
        pulumi.set(self, "fields", value)

    @property
    @pulumi.getter(name="fullName")
    def full_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "full_name")

    @full_name.setter
    def full_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "full_name", value)

    @property
    @pulumi.getter
    def gender(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "gender")

    @gender.setter
    def gender(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gender", value)

    @property
    @pulumi.getter
    def height(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "height")

    @height.setter
    def height(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "height", value)

    @property
    @pulumi.getter(name="licenseClass")
    def license_class(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "license_class")

    @license_class.setter
    def license_class(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "license_class", value)

    @property
    @pulumi.getter
    def notes(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "notes")

    @notes.setter
    def notes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notes", value)

    @property
    @pulumi.getter
    def number(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "number")

    @number.setter
    def number(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "number", value)

    @property
    @pulumi.getter
    def sections(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['SectionArgs']]]]:
        return pulumi.get(self, "sections")

    @sections.setter
    def sections(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['SectionArgs']]]]):
        pulumi.set(self, "sections", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

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


@pulumi.input_type
class _DriverLicenseItemState:
    def __init__(__self__, *,
                 vault: pulumi.Input[str]):
        """
        Input properties used for looking up and filtering DriverLicenseItem resources.
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


class DriverLicenseItem(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address: Optional[pulumi.Input[str]] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 conditions_restrictions: Optional[pulumi.Input[str]] = None,
                 country: Optional[pulumi.Input[str]] = None,
                 date_of_birth: Optional[pulumi.Input[str]] = None,
                 expiry_date: Optional[pulumi.Input[str]] = None,
                 fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['FieldArgs']]]]] = None,
                 full_name: Optional[pulumi.Input[str]] = None,
                 gender: Optional[pulumi.Input[str]] = None,
                 height: Optional[pulumi.Input[str]] = None,
                 license_class: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 number: Optional[pulumi.Input[str]] = None,
                 sections: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['SectionArgs']]]]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 vault: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a DriverLicenseItem resource with the given unique name, props, and options.
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
                 args: DriverLicenseItemArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a DriverLicenseItem resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param DriverLicenseItemArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DriverLicenseItemArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address: Optional[pulumi.Input[str]] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 conditions_restrictions: Optional[pulumi.Input[str]] = None,
                 country: Optional[pulumi.Input[str]] = None,
                 date_of_birth: Optional[pulumi.Input[str]] = None,
                 expiry_date: Optional[pulumi.Input[str]] = None,
                 fields: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['FieldArgs']]]]] = None,
                 full_name: Optional[pulumi.Input[str]] = None,
                 gender: Optional[pulumi.Input[str]] = None,
                 height: Optional[pulumi.Input[str]] = None,
                 license_class: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 number: Optional[pulumi.Input[str]] = None,
                 sections: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['SectionArgs']]]]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 vault: Optional[pulumi.Input[str]] = None,
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
            __props__ = DriverLicenseItemArgs.__new__(DriverLicenseItemArgs)

            __props__.__dict__["address"] = address
            __props__.__dict__["category"] = 'Driver License'
            __props__.__dict__["conditions_restrictions"] = conditions_restrictions
            __props__.__dict__["country"] = country
            __props__.__dict__["date_of_birth"] = date_of_birth
            __props__.__dict__["expiry_date"] = expiry_date
            __props__.__dict__["fields"] = fields
            __props__.__dict__["full_name"] = full_name
            __props__.__dict__["gender"] = gender
            __props__.__dict__["height"] = height
            __props__.__dict__["license_class"] = license_class
            __props__.__dict__["notes"] = notes
            __props__.__dict__["number"] = number
            __props__.__dict__["sections"] = sections
            __props__.__dict__["state"] = state
            __props__.__dict__["tags"] = tags
            __props__.__dict__["title"] = title
            if vault is None and not opts.urn:
                raise TypeError("Missing required property 'vault'")
            __props__.__dict__["vault"] = vault
            __props__.__dict__["uuid"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["fields", "sections"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(DriverLicenseItem, __self__).__init__(
            'onepassword:index:DriverLicenseItem',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            vault: Optional[pulumi.Input[str]] = None) -> 'DriverLicenseItem':
        """
        Get an existing DriverLicenseItem resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] vault: The UUID of the vault the item is in.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DriverLicenseItemState.__new__(_DriverLicenseItemState)

        __props__.__dict__["vault"] = vault
        __props__.__dict__["address"] = None
        __props__.__dict__["category"] = None
        __props__.__dict__["conditions_restrictions"] = None
        __props__.__dict__["country"] = None
        __props__.__dict__["date_of_birth"] = None
        __props__.__dict__["expiry_date"] = None
        __props__.__dict__["fields"] = None
        __props__.__dict__["full_name"] = None
        __props__.__dict__["gender"] = None
        __props__.__dict__["height"] = None
        __props__.__dict__["license_class"] = None
        __props__.__dict__["notes"] = None
        __props__.__dict__["number"] = None
        __props__.__dict__["sections"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["title"] = None
        __props__.__dict__["uuid"] = None
        return DriverLicenseItem(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def address(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "address")

    @property
    @pulumi.getter
    def category(self) -> pulumi.Output[str]:
        return pulumi.get(self, "category")

    @property
    @pulumi.getter(name="conditionsRestrictions")
    def conditions_restrictions(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "conditions_restrictions")

    @property
    @pulumi.getter
    def country(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "country")

    @property
    @pulumi.getter(name="dateOfBirth")
    def date_of_birth(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "date_of_birth")

    @property
    @pulumi.getter(name="expiryDate")
    def expiry_date(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "expiry_date")

    @property
    @pulumi.getter
    def fields(self) -> pulumi.Output[Optional[Mapping[str, 'outputs.GetField']]]:
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter(name="fullName")
    def full_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "full_name")

    @property
    @pulumi.getter
    def gender(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "gender")

    @property
    @pulumi.getter
    def height(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "height")

    @property
    @pulumi.getter(name="licenseClass")
    def license_class(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "license_class")

    @property
    @pulumi.getter
    def notes(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter
    def number(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "number")

    @property
    @pulumi.getter
    def sections(self) -> pulumi.Output[Optional[Mapping[str, 'outputs.GetSection']]]:
        return pulumi.get(self, "sections")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "state")

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

