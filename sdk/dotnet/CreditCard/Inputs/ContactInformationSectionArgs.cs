// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.OnePasswordNative.CreditCard.Inputs
{

    public sealed class ContactInformationSectionArgs : Pulumi.ResourceArgs
    {
        [Input("issuingBank")]
        public Input<string>? IssuingBank { get; set; }

        [Input("phoneIntl")]
        public Input<string>? PhoneIntl { get; set; }

        [Input("phoneLocal")]
        public Input<string>? PhoneLocal { get; set; }

        [Input("phoneTollFree")]
        public Input<string>? PhoneTollFree { get; set; }

        [Input("website")]
        public Input<string>? Website { get; set; }

        public ContactInformationSectionArgs()
        {
        }
    }
}
