// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Onepassword
{
    [OnepasswordResourceType("onepassword:index:IdentityItem")]
    public partial class IdentityItem : Pulumi.CustomResource
    {
        [Output("address")]
        public Output<Pulumi.Onepassword.Identity.Outputs.AddressSection?> Address { get; private set; } = null!;

        [Output("category")]
        public Output<string> Category { get; private set; } = null!;

        [Output("fields")]
        public Output<ImmutableDictionary<string, Outputs.GetField>?> Fields { get; private set; } = null!;

        [Output("identification")]
        public Output<Pulumi.Onepassword.Identity.Outputs.IdentificationSection?> Identification { get; private set; } = null!;

        [Output("internetDetails")]
        public Output<Pulumi.Onepassword.Identity.Outputs.InternetDetailsSection?> InternetDetails { get; private set; } = null!;

        [Output("notes")]
        public Output<string?> Notes { get; private set; } = null!;

        [Output("sections")]
        public Output<ImmutableDictionary<string, Outputs.GetSection>?> Sections { get; private set; } = null!;

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
        /// Create a IdentityItem resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public IdentityItem(string name, IdentityItemArgs args, CustomResourceOptions? options = null)
            : base("onepassword:index:IdentityItem", name, MakeArgs(args), MakeResourceOptions(options, ""))
        {
        }

        private IdentityItem(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("onepassword:index:IdentityItem", name, null, MakeResourceOptions(options, id))
        {
        }

        private static IdentityItemArgs MakeArgs(IdentityItemArgs args)
        {
            args ??= new IdentityItemArgs();
            args.Category = "Identity";
            return args;
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
        /// Get an existing IdentityItem resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static IdentityItem Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new IdentityItem(name, id, options);
        }
    }

    public sealed class IdentityItemArgs : Pulumi.ResourceArgs
    {
        [Input("address")]
        public Input<Pulumi.Onepassword.Identity.Inputs.AddressSectionArgs>? Address { get; set; }

        /// <summary>
        /// The category of the vault the item is in.
        /// </summary>
        [Input("category")]
        public Input<string>? Category { get; set; }

        [Input("fields")]
        private InputMap<Inputs.FieldArgs>? _fields;
        public InputMap<Inputs.FieldArgs> Fields
        {
            get => _fields ?? (_fields = new InputMap<Inputs.FieldArgs>());
            set => _fields = value;
        }

        [Input("identification")]
        public Input<Pulumi.Onepassword.Identity.Inputs.IdentificationSectionArgs>? Identification { get; set; }

        [Input("internetDetails")]
        public Input<Pulumi.Onepassword.Identity.Inputs.InternetDetailsSectionArgs>? InternetDetails { get; set; }

        [Input("notes")]
        public Input<string>? Notes { get; set; }

        [Input("sections")]
        private InputMap<Inputs.SectionArgs>? _sections;
        public InputMap<Inputs.SectionArgs> Sections
        {
            get => _sections ?? (_sections = new InputMap<Inputs.SectionArgs>());
            set => _sections = value;
        }

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
        [Input("title")]
        public Input<string>? Title { get; set; }

        /// <summary>
        /// The UUID of the vault the item is in.
        /// </summary>
        [Input("vault", required: true)]
        public Input<string> Vault { get; set; } = null!;

        public IdentityItemArgs()
        {
        }
    }
}
