// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.OnePasswordNative.RewardProgram.Inputs
{

    public sealed class MoreInformationSectionArgs : Pulumi.ResourceArgs
    {
        [Input("customerServicePhone")]
        public Input<string>? CustomerServicePhone { get; set; }

        [Input("memberIdAdditional")]
        public Input<string>? MemberIdAdditional { get; set; }

        [Input("memberSince")]
        public Input<string>? MemberSince { get; set; }

        [Input("phoneForReservations")]
        public Input<string>? PhoneForReservations { get; set; }

        [Input("website")]
        public Input<string>? Website { get; set; }

        public MoreInformationSectionArgs()
        {
        }
    }
}
