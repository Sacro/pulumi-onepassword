// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Onepassword
{
    public static class GetRewardProgram
    {
        public static Task<GetRewardProgramResult> InvokeAsync(GetRewardProgramArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetRewardProgramResult>("onepassword:index:GetRewardProgram", args ?? new GetRewardProgramArgs(), options.WithDefaults());

        public static Output<GetRewardProgramResult> Invoke(GetRewardProgramInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetRewardProgramResult>("onepassword:index:GetRewardProgram", args ?? new GetRewardProgramInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetRewardProgramArgs : Pulumi.InvokeArgs
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

        public GetRewardProgramArgs()
        {
        }
    }

    public sealed class GetRewardProgramInvokeArgs : Pulumi.InvokeArgs
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

        public GetRewardProgramInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetRewardProgramResult
    {
        public readonly string? Category;
        public readonly string? CompanyName;
        public readonly ImmutableArray<Outputs.GetField> Fields;
        public readonly string? Id;
        public readonly string? MemberId;
        public readonly string? MemberName;
        public readonly Pulumi.Onepassword.RewardProgram.Outputs.MoreInformation? MoreInformation;
        public readonly string? Notes;
        public readonly string? Pin;
        public readonly ImmutableArray<Outputs.GetSection> Sections;
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
        private GetRewardProgramResult(
            string? category,

            string? companyName,

            ImmutableArray<Outputs.GetField> fields,

            string? id,

            string? memberId,

            string? memberName,

            Pulumi.Onepassword.RewardProgram.Outputs.MoreInformation? moreInformation,

            string? notes,

            string? pin,

            ImmutableArray<Outputs.GetSection> sections,

            ImmutableArray<string> tags,

            string? title,

            string? uuid,

            string? vault)
        {
            Category = category;
            CompanyName = companyName;
            Fields = fields;
            Id = id;
            MemberId = memberId;
            MemberName = memberName;
            MoreInformation = moreInformation;
            Notes = notes;
            Pin = pin;
            Sections = sections;
            Tags = tags;
            Title = title;
            Uuid = uuid;
            Vault = vault;
        }
    }
}
