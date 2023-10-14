// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Onepassword
{
    public static class GetCryptoWallet
    {
        public static Task<GetCryptoWalletResult> InvokeAsync(GetCryptoWalletArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetCryptoWalletResult>("onepassword:index:GetCryptoWallet", args ?? new GetCryptoWalletArgs(), options.WithDefaults());

        public static Output<GetCryptoWalletResult> Invoke(GetCryptoWalletInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetCryptoWalletResult>("onepassword:index:GetCryptoWallet", args ?? new GetCryptoWalletInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetCryptoWalletArgs : Pulumi.InvokeArgs
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

        public GetCryptoWalletArgs()
        {
        }
    }

    public sealed class GetCryptoWalletInvokeArgs : Pulumi.InvokeArgs
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

        public GetCryptoWalletInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetCryptoWalletResult
    {
        public readonly string? Category;
        public readonly ImmutableArray<Outputs.GetField> Fields;
        public readonly string? Id;
        public readonly string? Notes;
        public readonly string? Password;
        public readonly string? RecoveryPhrase;
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
        public readonly Pulumi.Onepassword.CryptoWallet.Outputs.Wallet? Wallet;

        [OutputConstructor]
        private GetCryptoWalletResult(
            string? category,

            ImmutableArray<Outputs.GetField> fields,

            string? id,

            string? notes,

            string? password,

            string? recoveryPhrase,

            ImmutableArray<Outputs.GetSection> sections,

            ImmutableArray<string> tags,

            string? title,

            string? uuid,

            string? vault,

            Pulumi.Onepassword.CryptoWallet.Outputs.Wallet? wallet)
        {
            Category = category;
            Fields = fields;
            Id = id;
            Notes = notes;
            Password = password;
            RecoveryPhrase = recoveryPhrase;
            Sections = sections;
            Tags = tags;
            Title = title;
            Uuid = uuid;
            Vault = vault;
            Wallet = wallet;
        }
    }
}
