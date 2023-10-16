// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Onepassword
{
    [OnepasswordResourceType("onepassword:index:MembershipItem")]
    public partial class MembershipItem : Pulumi.CustomResource
    {
        [Output("category")]
        public Output<string> Category { get; private set; } = null!;

        [Output("expiryDate")]
        public Output<string?> ExpiryDate { get; private set; } = null!;

        [Output("fields")]
        public Output<ImmutableDictionary<string, Outputs.GetField>?> Fields { get; private set; } = null!;

        [Output("group")]
        public Output<string?> Group { get; private set; } = null!;

        [Output("memberId")]
        public Output<string?> MemberId { get; private set; } = null!;

        [Output("memberName")]
        public Output<string?> MemberName { get; private set; } = null!;

        [Output("memberSince")]
        public Output<string?> MemberSince { get; private set; } = null!;

        [Output("notes")]
        public Output<string?> Notes { get; private set; } = null!;

        [Output("pin")]
        public Output<string?> Pin { get; private set; } = null!;

        [Output("sections")]
        public Output<ImmutableDictionary<string, Outputs.GetSection>?> Sections { get; private set; } = null!;

        /// <summary>
        /// An array of strings of the tags assigned to the item.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<string>> Tags { get; private set; } = null!;

        [Output("telephone")]
        public Output<string?> Telephone { get; private set; } = null!;

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

        [Output("website")]
        public Output<string?> Website { get; private set; } = null!;


        /// <summary>
        /// Create a MembershipItem resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public MembershipItem(string name, MembershipItemArgs args, CustomResourceOptions? options = null)
            : base("onepassword:index:MembershipItem", name, MakeArgs(args), MakeResourceOptions(options, ""))
        {
        }

        private MembershipItem(string name, Input<string> id, MembershipItemState? state = null, CustomResourceOptions? options = null)
            : base("onepassword:index:MembershipItem", name, state, MakeResourceOptions(options, id))
        {
        }

        private static MembershipItemArgs MakeArgs(MembershipItemArgs args)
        {
            args ??= new MembershipItemArgs();
            args.Category = "Membership";
            return args;
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                AdditionalSecretOutputs =
                {
                    "fields",
                    "sections",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing MembershipItem resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static MembershipItem Get(string name, Input<string> id, MembershipItemState? state = null, CustomResourceOptions? options = null)
        {
            return new MembershipItem(name, id, state, options);
        }
    }

    public sealed class MembershipItemArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The category of the vault the item is in.
        /// </summary>
        [Input("category")]
        public Input<string>? Category { get; set; }

        [Input("expiryDate")]
        public Input<string>? ExpiryDate { get; set; }

        [Input("fields")]
        private InputMap<Inputs.FieldArgs>? _fields;
        public InputMap<Inputs.FieldArgs> Fields
        {
            get => _fields ?? (_fields = new InputMap<Inputs.FieldArgs>());
            set => _fields = value;
        }

        [Input("group")]
        public Input<string>? Group { get; set; }

        [Input("memberId")]
        public Input<string>? MemberId { get; set; }

        [Input("memberName")]
        public Input<string>? MemberName { get; set; }

        [Input("memberSince")]
        public Input<string>? MemberSince { get; set; }

        [Input("notes")]
        public Input<string>? Notes { get; set; }

        [Input("pin")]
        public Input<string>? Pin { get; set; }

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

        [Input("telephone")]
        public Input<string>? Telephone { get; set; }

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

        [Input("website")]
        public Input<string>? Website { get; set; }

        public MembershipItemArgs()
        {
        }
    }

    public sealed class MembershipItemState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The UUID of the vault the item is in.
        /// </summary>
        [Input("vault", required: true)]
        public Input<string> Vault { get; set; } = null!;

        public MembershipItemState()
        {
        }
    }
}
