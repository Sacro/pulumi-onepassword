# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import medicalrecord as _medicalrecord
from . import outputs
from ._enums import *

__all__ = [
    'GetMedicalRecordResult',
    'AwaitableGetMedicalRecordResult',
    'get_medical_record',
    'get_medical_record_output',
]

@pulumi.output_type
class GetMedicalRecordResult:
    def __init__(__self__, category=None, date=None, fields=None, healthcare_professional=None, id=None, location=None, medication=None, notes=None, patient=None, reason_for_visit=None, sections=None, tags=None, title=None, uuid=None, vault=None):
        if category and not isinstance(category, dict):
            raise TypeError("Expected argument 'category' to be a dict")
        pulumi.set(__self__, "category", category)
        if date and not isinstance(date, str):
            raise TypeError("Expected argument 'date' to be a str")
        pulumi.set(__self__, "date", date)
        if fields and not isinstance(fields, list):
            raise TypeError("Expected argument 'fields' to be a list")
        pulumi.set(__self__, "fields", fields)
        if healthcare_professional and not isinstance(healthcare_professional, str):
            raise TypeError("Expected argument 'healthcare_professional' to be a str")
        pulumi.set(__self__, "healthcare_professional", healthcare_professional)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if medication and not isinstance(medication, dict):
            raise TypeError("Expected argument 'medication' to be a dict")
        pulumi.set(__self__, "medication", medication)
        if notes and not isinstance(notes, str):
            raise TypeError("Expected argument 'notes' to be a str")
        pulumi.set(__self__, "notes", notes)
        if patient and not isinstance(patient, str):
            raise TypeError("Expected argument 'patient' to be a str")
        pulumi.set(__self__, "patient", patient)
        if reason_for_visit and not isinstance(reason_for_visit, str):
            raise TypeError("Expected argument 'reason_for_visit' to be a str")
        pulumi.set(__self__, "reason_for_visit", reason_for_visit)
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
    @pulumi.getter
    def date(self) -> Optional[str]:
        return pulumi.get(self, "date")

    @property
    @pulumi.getter
    def fields(self) -> Optional[Sequence['outputs.GetField']]:
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter(name="healthcareProfessional")
    def healthcare_professional(self) -> Optional[str]:
        return pulumi.get(self, "healthcare_professional")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def medication(self) -> Optional['_medicalrecord.outputs.Medication']:
        return pulumi.get(self, "medication")

    @property
    @pulumi.getter
    def notes(self) -> Optional[str]:
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter
    def patient(self) -> Optional[str]:
        return pulumi.get(self, "patient")

    @property
    @pulumi.getter(name="reasonForVisit")
    def reason_for_visit(self) -> Optional[str]:
        return pulumi.get(self, "reason_for_visit")

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


class AwaitableGetMedicalRecordResult(GetMedicalRecordResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMedicalRecordResult(
            category=self.category,
            date=self.date,
            fields=self.fields,
            healthcare_professional=self.healthcare_professional,
            id=self.id,
            location=self.location,
            medication=self.medication,
            notes=self.notes,
            patient=self.patient,
            reason_for_visit=self.reason_for_visit,
            sections=self.sections,
            tags=self.tags,
            title=self.title,
            uuid=self.uuid,
            vault=self.vault)


def get_medical_record(title: Optional[str] = None,
                       uuid: Optional[str] = None,
                       vault: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMedicalRecordResult:
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
    __ret__ = pulumi.runtime.invoke('onepassword:index:GetMedicalRecord', __args__, opts=opts, typ=GetMedicalRecordResult).value

    return AwaitableGetMedicalRecordResult(
        category=__ret__.category,
        date=__ret__.date,
        fields=__ret__.fields,
        healthcare_professional=__ret__.healthcare_professional,
        id=__ret__.id,
        location=__ret__.location,
        medication=__ret__.medication,
        notes=__ret__.notes,
        patient=__ret__.patient,
        reason_for_visit=__ret__.reason_for_visit,
        sections=__ret__.sections,
        tags=__ret__.tags,
        title=__ret__.title,
        uuid=__ret__.uuid,
        vault=__ret__.vault)


@_utilities.lift_output_func(get_medical_record)
def get_medical_record_output(title: Optional[pulumi.Input[Optional[str]]] = None,
                              uuid: Optional[pulumi.Input[Optional[str]]] = None,
                              vault: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMedicalRecordResult]:
    """
    Use this data source to access information about an existing resource.

    :param str title: The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
    :param str uuid: The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
    :param str vault: The UUID of the vault the item is in.
    """
    ...
