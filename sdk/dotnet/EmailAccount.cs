// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Onepassword
{
    [OnepasswordResourceType("onepassword:index:EmailAccount")]
    public partial class EmailAccount : Pulumi.CustomResource
    {
        [Output("authMethod")]
        public Output<string?> AuthMethod { get; private set; } = null!;

        [Output("category")]
        public Output<string> Category { get; private set; } = null!;

        [Output("contactInformation")]
        public Output<Pulumi.Onepassword.EmailAccount.Outputs.ContactInformation?> ContactInformation { get; private set; } = null!;

        [Output("fields")]
        public Output<ImmutableArray<Outputs.GetField>> Fields { get; private set; } = null!;

        [Output("id")]
        public Output<string> Id { get; private set; } = null!;

        [Output("notes")]
        public Output<string?> Notes { get; private set; } = null!;

        [Output("password")]
        public Output<string?> Password { get; private set; } = null!;

        [Output("portNumber")]
        public Output<string?> PortNumber { get; private set; } = null!;

        [Output("sections")]
        public Output<ImmutableArray<Outputs.GetSection>> Sections { get; private set; } = null!;

        [Output("security")]
        public Output<string?> Security { get; private set; } = null!;

        [Output("server")]
        public Output<string?> Server { get; private set; } = null!;

        [Output("smtp")]
        public Output<Pulumi.Onepassword.EmailAccount.Outputs.Smtp?> Smtp { get; private set; } = null!;

        /// <summary>
        /// An array of strings of the tags assigned to the item.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<string>> Tags { get; private set; } = null!;

        /// <summary>
        /// The title of the item.
        /// </summary>
        [Output("title")]
        public Output<string> Title { get; private set; } = null!;

        [Output("type")]
        public Output<string?> Type { get; private set; } = null!;

        [Output("username")]
        public Output<string?> Username { get; private set; } = null!;

        /// <summary>
        /// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
        /// </summary>
        [Output("uuid")]
        public Output<string> Uuid { get; private set; } = null!;

        /// <summary>
        /// The UUID of the vault the item is in.
        /// </summary>
        [Output("vault")]
        public Output<string> Vault { get; private set; } = null!;


        /// <summary>
        /// Create a EmailAccount resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public EmailAccount(string name, EmailAccountArgs args, CustomResourceOptions? options = null)
            : base("onepassword:index:EmailAccount", name, args ?? new EmailAccountArgs(), MakeResourceOptions(options, ""))
        {
        }

        private EmailAccount(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("onepassword:index:EmailAccount", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing EmailAccount resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static EmailAccount Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new EmailAccount(name, id, options);
        }
    }

    public sealed class EmailAccountArgs : Pulumi.ResourceArgs
    {
        [Input("authMethod")]
        public Input<string>? AuthMethod { get; set; }

        [Input("contactInformation")]
        public Input<Pulumi.Onepassword.EmailAccount.Inputs.ContactInformationArgs>? ContactInformation { get; set; }

        [Input("fields")]
        private InputList<Inputs.FieldArgs>? _fields;
        public InputList<Inputs.FieldArgs> Fields
        {
            get => _fields ?? (_fields = new InputList<Inputs.FieldArgs>());
            set => _fields = value;
        }

        [Input("notes")]
        public Input<string>? Notes { get; set; }

        [Input("password")]
        public Input<string>? Password { get; set; }

        [Input("portNumber")]
        public Input<string>? PortNumber { get; set; }

        [Input("sections")]
        private InputList<Inputs.SectionArgs>? _sections;
        public InputList<Inputs.SectionArgs> Sections
        {
            get => _sections ?? (_sections = new InputList<Inputs.SectionArgs>());
            set => _sections = value;
        }

        [Input("security")]
        public Input<string>? Security { get; set; }

        [Input("server")]
        public Input<string>? Server { get; set; }

        [Input("smtp")]
        public Input<Pulumi.Onepassword.EmailAccount.Inputs.SmtpArgs>? Smtp { get; set; }

        [Input("tags")]
        private InputList<string>? _tags;

        /// <summary>
        /// An array of strings of the tags assigned to the item.
        /// </summary>
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
        /// </summary>
        [Input("title", required: true)]
        public Input<string> Title { get; set; } = null!;

        [Input("type")]
        public Input<string>? Type { get; set; }

        [Input("username")]
        public Input<string>? Username { get; set; }

        /// <summary>
        /// The UUID of the vault the item is in.
        /// </summary>
        [Input("vault", required: true)]
        public Input<string> Vault { get; set; } = null!;

        public EmailAccountArgs()
        {
        }
    }
}
