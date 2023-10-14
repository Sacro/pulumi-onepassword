// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Onepassword
{
    public static class GetSecretReference
    {
        public static Task<GetSecretReferenceResult> InvokeAsync(GetSecretReferenceArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetSecretReferenceResult>("onepassword:index:GetSecretReference", args ?? new GetSecretReferenceArgs(), options.WithDefaults());

        public static Output<GetSecretReferenceResult> Invoke(GetSecretReferenceInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetSecretReferenceResult>("onepassword:index:GetSecretReference", args ?? new GetSecretReferenceInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetSecretReferenceArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The 1Password secret reference path to the item.  eg: op://vault/item/[section]/field 
        /// </summary>
        [Input("reference", required: true)]
        public string Reference { get; set; } = null!;

        public GetSecretReferenceArgs()
        {
        }
    }

    public sealed class GetSecretReferenceInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The 1Password secret reference path to the item.  eg: op://vault/item/[section]/field 
        /// </summary>
        [Input("reference", required: true)]
        public Input<string> Reference { get; set; } = null!;

        public GetSecretReferenceInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetSecretReferenceResult
    {
        public readonly string? Value;

        [OutputConstructor]
        private GetSecretReferenceResult(string? value)
        {
            Value = value;
        }
    }
}
