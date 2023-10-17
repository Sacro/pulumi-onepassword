// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Onepassword
{
    [OnepasswordResourceType("onepassword:index:ServerItem")]
    public partial class ServerItem : Pulumi.CustomResource
    {
        [Output("adminConsole")]
        public Output<Pulumi.Onepassword.Server.Outputs.AdminConsoleSection?> AdminConsole { get; private set; } = null!;

        [Output("category")]
        public Output<string> Category { get; private set; } = null!;

        [Output("fields")]
        public Output<ImmutableDictionary<string, Outputs.GetField>> Fields { get; private set; } = null!;

        [Output("hostingProvider")]
        public Output<Pulumi.Onepassword.Server.Outputs.HostingProviderSection?> HostingProvider { get; private set; } = null!;

        [Output("notes")]
        public Output<string?> Notes { get; private set; } = null!;

        [Output("password")]
        public Output<string?> Password { get; private set; } = null!;

        [Output("sections")]
        public Output<ImmutableDictionary<string, Outputs.GetSection>> Sections { get; private set; } = null!;

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

        [Output("url")]
        public Output<string?> Url { get; private set; } = null!;

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
        /// Create a ServerItem resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ServerItem(string name, ServerItemArgs args, CustomResourceOptions? options = null)
            : base("onepassword:index:ServerItem", name, MakeArgs(args), MakeResourceOptions(options, ""))
        {
        }

        private ServerItem(string name, Input<string> id, ServerItemState? state = null, CustomResourceOptions? options = null)
            : base("onepassword:index:ServerItem", name, state, MakeResourceOptions(options, id))
        {
        }

        private static ServerItemArgs MakeArgs(ServerItemArgs args)
        {
            args ??= new ServerItemArgs();
            args.Category = "Server";
            return args;
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                AdditionalSecretOutputs =
                {
                    "adminConsole",
                    "fields",
                    "password",
                    "sections",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ServerItem resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ServerItem Get(string name, Input<string> id, ServerItemState? state = null, CustomResourceOptions? options = null)
        {
            return new ServerItem(name, id, state, options);
        }
    }

    public sealed class ServerItemArgs : Pulumi.ResourceArgs
    {
        [Input("adminConsole")]
        public Input<Pulumi.Onepassword.Server.Inputs.AdminConsoleSectionArgs>? AdminConsole { get; set; }

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

        [Input("hostingProvider")]
        public Input<Pulumi.Onepassword.Server.Inputs.HostingProviderSectionArgs>? HostingProvider { get; set; }

        [Input("notes")]
        public Input<string>? Notes { get; set; }

        [Input("password")]
        private Input<string>? _password;
        public Input<string>? Password
        {
            get => _password;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _password = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

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

        [Input("url")]
        public Input<string>? Url { get; set; }

        [Input("username")]
        public Input<string>? Username { get; set; }

        /// <summary>
        /// The UUID of the vault the item is in.
        /// </summary>
        [Input("vault", required: true)]
        public Input<string> Vault { get; set; } = null!;

        public ServerItemArgs()
        {
        }
    }

    public sealed class ServerItemState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The UUID of the vault the item is in.
        /// </summary>
        [Input("vault", required: true)]
        public Input<string> Vault { get; set; } = null!;

        public ServerItemState()
        {
        }
    }
}
