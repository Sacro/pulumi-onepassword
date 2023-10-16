// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Onepassword
{
    public static class GetPassword
    {
        public static Task<GetPasswordResult> InvokeAsync(GetPasswordArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetPasswordResult>("onepassword:index:GetPassword", args ?? new GetPasswordArgs(), options.WithDefaults());

        public static Output<GetPasswordResult> Invoke(GetPasswordInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetPasswordResult>("onepassword:index:GetPassword", args ?? new GetPasswordInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPasswordArgs : Pulumi.InvokeArgs
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

        public GetPasswordArgs()
        {
        }
    }

    public sealed class GetPasswordInvokeArgs : Pulumi.InvokeArgs
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

        public GetPasswordInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetPasswordResult
    {
        public readonly string? Category;
        public readonly ImmutableDictionary<string, Outputs.GetField>? Fields;
        public readonly string? Notes;
        public readonly string? Password;
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
        private GetPasswordResult(
            string? category,

            ImmutableDictionary<string, Outputs.GetField>? fields,

            string? notes,

            string? password,

            ImmutableDictionary<string, Outputs.GetSection>? sections,

            ImmutableArray<string> tags,

            string? title,

            string? uuid,

            string? vault)
        {
            Category = category;
            Fields = fields;
            Notes = notes;
            Password = password;
            Sections = sections;
            Tags = tags;
            Title = title;
            Uuid = uuid;
            Vault = vault;
        }
    }
}
