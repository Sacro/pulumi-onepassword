// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.OnePasswordNative
{
    public static class GetPassport
    {
        public static Task<GetPassportResult> InvokeAsync(GetPassportArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetPassportResult>("one-password-native:index:GetPassport", args ?? new GetPassportArgs(), options.WithDefaults());

        public static Output<GetPassportResult> Invoke(GetPassportInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetPassportResult>("one-password-native:index:GetPassport", args ?? new GetPassportInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPassportArgs : Pulumi.InvokeArgs
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

        public GetPassportArgs()
        {
        }
    }

    public sealed class GetPassportInvokeArgs : Pulumi.InvokeArgs
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

        public GetPassportInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetPassportResult
    {
        public readonly ImmutableDictionary<string, Outputs.OutField> Attachments;
        public readonly string Category;
        public readonly string? DateOfBirth;
        public readonly string? ExpiryDate;
        public readonly ImmutableDictionary<string, Outputs.OutField> Fields;
        public readonly string? FullName;
        public readonly string? Gender;
        public readonly string? IssuedOn;
        public readonly string? IssuingAuthority;
        public readonly string? IssuingCountry;
        public readonly string? Nationality;
        public readonly string? Notes;
        public readonly string? Number;
        public readonly string? PlaceOfBirth;
        public readonly ImmutableDictionary<string, Outputs.OutField> References;
        public readonly ImmutableDictionary<string, Outputs.OutSection> Sections;
        /// <summary>
        /// An array of strings of the tags assigned to the item.
        /// </summary>
        public readonly ImmutableArray<string> Tags;
        /// <summary>
        /// The title of the item.
        /// </summary>
        public readonly string Title;
        public readonly string? Type;
        /// <summary>
        /// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
        /// </summary>
        public readonly string Uuid;
        /// <summary>
        /// The UUID of the vault the item is in.
        /// </summary>
        public readonly string Vault;

        [OutputConstructor]
        private GetPassportResult(
            ImmutableDictionary<string, Outputs.OutField> attachments,

            string category,

            string? dateOfBirth,

            string? expiryDate,

            ImmutableDictionary<string, Outputs.OutField> fields,

            string? fullName,

            string? gender,

            string? issuedOn,

            string? issuingAuthority,

            string? issuingCountry,

            string? nationality,

            string? notes,

            string? number,

            string? placeOfBirth,

            ImmutableDictionary<string, Outputs.OutField> references,

            ImmutableDictionary<string, Outputs.OutSection> sections,

            ImmutableArray<string> tags,

            string title,

            string? type,

            string uuid,

            string vault)
        {
            Attachments = attachments;
            Category = category;
            DateOfBirth = dateOfBirth;
            ExpiryDate = expiryDate;
            Fields = fields;
            FullName = fullName;
            Gender = gender;
            IssuedOn = issuedOn;
            IssuingAuthority = issuingAuthority;
            IssuingCountry = issuingCountry;
            Nationality = nationality;
            Notes = notes;
            Number = number;
            PlaceOfBirth = placeOfBirth;
            References = references;
            Sections = sections;
            Tags = tags;
            Title = title;
            Type = type;
            Uuid = uuid;
            Vault = vault;
        }
    }
}
