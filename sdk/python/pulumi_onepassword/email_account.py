# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import emailaccount as _emailaccount
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['EmailAccountArgs', 'EmailAccount']

@pulumi.input_type
class EmailAccountArgs:
    def __init__(__self__, *,
                 title: pulumi.Input[str],
                 vault: pulumi.Input[str],
                 auth_method: Optional[pulumi.Input[str]] = None,
                 contact_information: Optional[pulumi.Input['_emailaccount.ContactInformationArgs']] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input['FieldArgs']]]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 port_number: Optional[pulumi.Input[str]] = None,
                 sections: Optional[pulumi.Input[Sequence[pulumi.Input['SectionArgs']]]] = None,
                 security: Optional[pulumi.Input[str]] = None,
                 server: Optional[pulumi.Input[str]] = None,
                 smtp: Optional[pulumi.Input['_emailaccount.SmtpArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a EmailAccount resource.
        :param pulumi.Input[str] title: The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
        :param pulumi.Input[str] vault: The UUID of the vault the item is in.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: An array of strings of the tags assigned to the item.
        """
        pulumi.set(__self__, "title", title)
        pulumi.set(__self__, "vault", vault)
        if auth_method is not None:
            pulumi.set(__self__, "auth_method", auth_method)
        if contact_information is not None:
            pulumi.set(__self__, "contact_information", contact_information)
        if fields is not None:
            pulumi.set(__self__, "fields", fields)
        if notes is not None:
            pulumi.set(__self__, "notes", notes)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if port_number is not None:
            pulumi.set(__self__, "port_number", port_number)
        if sections is not None:
            pulumi.set(__self__, "sections", sections)
        if security is not None:
            pulumi.set(__self__, "security", security)
        if server is not None:
            pulumi.set(__self__, "server", server)
        if smtp is not None:
            pulumi.set(__self__, "smtp", smtp)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        """
        The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

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
    @pulumi.getter(name="authMethod")
    def auth_method(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "auth_method")

    @auth_method.setter
    def auth_method(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auth_method", value)

    @property
    @pulumi.getter(name="contactInformation")
    def contact_information(self) -> Optional[pulumi.Input['_emailaccount.ContactInformationArgs']]:
        return pulumi.get(self, "contact_information")

    @contact_information.setter
    def contact_information(self, value: Optional[pulumi.Input['_emailaccount.ContactInformationArgs']]):
        pulumi.set(self, "contact_information", value)

    @property
    @pulumi.getter
    def fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FieldArgs']]]]:
        return pulumi.get(self, "fields")

    @fields.setter
    def fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FieldArgs']]]]):
        pulumi.set(self, "fields", value)

    @property
    @pulumi.getter
    def notes(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "notes")

    @notes.setter
    def notes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notes", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="portNumber")
    def port_number(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "port_number")

    @port_number.setter
    def port_number(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "port_number", value)

    @property
    @pulumi.getter
    def sections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SectionArgs']]]]:
        return pulumi.get(self, "sections")

    @sections.setter
    def sections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SectionArgs']]]]):
        pulumi.set(self, "sections", value)

    @property
    @pulumi.getter
    def security(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "security")

    @security.setter
    def security(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "security", value)

    @property
    @pulumi.getter
    def server(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "server")

    @server.setter
    def server(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server", value)

    @property
    @pulumi.getter
    def smtp(self) -> Optional[pulumi.Input['_emailaccount.SmtpArgs']]:
        return pulumi.get(self, "smtp")

    @smtp.setter
    def smtp(self, value: Optional[pulumi.Input['_emailaccount.SmtpArgs']]):
        pulumi.set(self, "smtp", value)

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
    def type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


class EmailAccount(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_method: Optional[pulumi.Input[str]] = None,
                 contact_information: Optional[pulumi.Input[pulumi.InputType['_emailaccount.ContactInformationArgs']]] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FieldArgs']]]]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 port_number: Optional[pulumi.Input[str]] = None,
                 sections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SectionArgs']]]]] = None,
                 security: Optional[pulumi.Input[str]] = None,
                 server: Optional[pulumi.Input[str]] = None,
                 smtp: Optional[pulumi.Input[pulumi.InputType['_emailaccount.SmtpArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 vault: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a EmailAccount resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: An array of strings of the tags assigned to the item.
        :param pulumi.Input[str] title: The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
        :param pulumi.Input[str] vault: The UUID of the vault the item is in.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EmailAccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a EmailAccount resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param EmailAccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EmailAccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_method: Optional[pulumi.Input[str]] = None,
                 contact_information: Optional[pulumi.Input[pulumi.InputType['_emailaccount.ContactInformationArgs']]] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FieldArgs']]]]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 port_number: Optional[pulumi.Input[str]] = None,
                 sections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SectionArgs']]]]] = None,
                 security: Optional[pulumi.Input[str]] = None,
                 server: Optional[pulumi.Input[str]] = None,
                 smtp: Optional[pulumi.Input[pulumi.InputType['_emailaccount.SmtpArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
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
            __props__ = EmailAccountArgs.__new__(EmailAccountArgs)

            __props__.__dict__["auth_method"] = auth_method
            __props__.__dict__["contact_information"] = contact_information
            __props__.__dict__["fields"] = fields
            __props__.__dict__["notes"] = notes
            __props__.__dict__["password"] = password
            __props__.__dict__["port_number"] = port_number
            __props__.__dict__["sections"] = sections
            __props__.__dict__["security"] = security
            __props__.__dict__["server"] = server
            __props__.__dict__["smtp"] = smtp
            __props__.__dict__["tags"] = tags
            if title is None and not opts.urn:
                raise TypeError("Missing required property 'title'")
            __props__.__dict__["title"] = title
            __props__.__dict__["type"] = type
            __props__.__dict__["username"] = username
            if vault is None and not opts.urn:
                raise TypeError("Missing required property 'vault'")
            __props__.__dict__["vault"] = vault
            __props__.__dict__["category"] = None
            __props__.__dict__["id"] = None
            __props__.__dict__["uuid"] = None
        super(EmailAccount, __self__).__init__(
            'onepassword:index:EmailAccount',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'EmailAccount':
        """
        Get an existing EmailAccount resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EmailAccountArgs.__new__(EmailAccountArgs)

        __props__.__dict__["auth_method"] = None
        __props__.__dict__["category"] = None
        __props__.__dict__["contact_information"] = None
        __props__.__dict__["fields"] = None
        __props__.__dict__["id"] = None
        __props__.__dict__["notes"] = None
        __props__.__dict__["password"] = None
        __props__.__dict__["port_number"] = None
        __props__.__dict__["sections"] = None
        __props__.__dict__["security"] = None
        __props__.__dict__["server"] = None
        __props__.__dict__["smtp"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["title"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["username"] = None
        __props__.__dict__["uuid"] = None
        __props__.__dict__["vault"] = None
        return EmailAccount(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authMethod")
    def auth_method(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "auth_method")

    @property
    @pulumi.getter
    def category(self) -> pulumi.Output[str]:
        return pulumi.get(self, "category")

    @property
    @pulumi.getter(name="contactInformation")
    def contact_information(self) -> pulumi.Output[Optional['_emailaccount.outputs.ContactInformation']]:
        return pulumi.get(self, "contact_information")

    @property
    @pulumi.getter
    def fields(self) -> pulumi.Output[Optional[Sequence['outputs.GetField']]]:
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter
    def id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def notes(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="portNumber")
    def port_number(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "port_number")

    @property
    @pulumi.getter
    def sections(self) -> pulumi.Output[Optional[Sequence['outputs.GetSection']]]:
        return pulumi.get(self, "sections")

    @property
    @pulumi.getter
    def security(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "security")

    @property
    @pulumi.getter
    def server(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "server")

    @property
    @pulumi.getter
    def smtp(self) -> pulumi.Output[Optional['_emailaccount.outputs.Smtp']]:
        return pulumi.get(self, "smtp")

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
    def type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "username")

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

