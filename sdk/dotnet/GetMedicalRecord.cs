// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Onepassword
{
    public static class GetMedicalRecord
    {
        public static Task<GetMedicalRecordResult> InvokeAsync(GetMedicalRecordArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetMedicalRecordResult>("onepassword:index:GetMedicalRecord", args ?? new GetMedicalRecordArgs(), options.WithDefaults());

        public static Output<GetMedicalRecordResult> Invoke(GetMedicalRecordInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetMedicalRecordResult>("onepassword:index:GetMedicalRecord", args ?? new GetMedicalRecordInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetMedicalRecordArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
        /// </summary>
        [Input("title")]
        public string? Title { get; set; }

        /// <summary>
        /// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
        /// </summary>
        [Input("uuid")]
        public string? Uuid { get; set; }

        /// <summary>
        /// The UUID of the vault the item is in.
        /// </summary>
        [Input("vault", required: true)]
        public string Vault { get; set; } = null!;

        public GetMedicalRecordArgs()
        {
        }
    }

    public sealed class GetMedicalRecordInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
        /// </summary>
        [Input("title")]
        public Input<string>? Title { get; set; }

        /// <summary>
        /// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
        /// </summary>
        [Input("uuid")]
        public Input<string>? Uuid { get; set; }

        /// <summary>
        /// The UUID of the vault the item is in.
        /// </summary>
        [Input("vault", required: true)]
        public Input<string> Vault { get; set; } = null!;

        public GetMedicalRecordInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetMedicalRecordResult
    {
        public readonly string? Category;
        public readonly string? Date;
        public readonly ImmutableDictionary<string, Outputs.GetField>? Fields;
        public readonly string? HealthcareProfessional;
        public readonly string? Location;
        public readonly Pulumi.Onepassword.MedicalRecord.Outputs.MedicationSection? Medication;
        public readonly string? Notes;
        public readonly string? Patient;
        public readonly string? ReasonForVisit;
        public readonly ImmutableDictionary<string, Outputs.GetSection>? Sections;
        /// <summary>
        /// An array of strings of the tags assigned to the item.
        /// </summary>
        public readonly ImmutableArray<string> Tags;
        /// <summary>
        /// The title of the item.
        /// </summary>
        public readonly string? Title;
        /// <summary>
        /// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
        /// </summary>
        public readonly string? Uuid;
        /// <summary>
        /// The UUID of the vault the item is in.
        /// </summary>
        public readonly string? Vault;

        [OutputConstructor]
        private GetMedicalRecordResult(
            string? category,

            string? date,

            ImmutableDictionary<string, Outputs.GetField>? fields,

            string? healthcareProfessional,

            string? location,

            Pulumi.Onepassword.MedicalRecord.Outputs.MedicationSection? medication,

            string? notes,

            string? patient,

            string? reasonForVisit,

            ImmutableDictionary<string, Outputs.GetSection>? sections,

            ImmutableArray<string> tags,

            string? title,

            string? uuid,

            string? vault)
        {
            Category = category;
            Date = date;
            Fields = fields;
            HealthcareProfessional = healthcareProfessional;
            Location = location;
            Medication = medication;
            Notes = notes;
            Patient = patient;
            ReasonForVisit = reasonForVisit;
            Sections = sections;
            Tags = tags;
            Title = title;
            Uuid = uuid;
            Vault = vault;
        }
    }
}
