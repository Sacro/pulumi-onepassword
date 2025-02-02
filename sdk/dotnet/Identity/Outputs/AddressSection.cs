// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.OnePasswordNative.Identity.Outputs
{

    [OutputType]
    public sealed class AddressSection
    {
        public readonly string? Address;
        public readonly string? Business;
        public readonly string? Cell;
        public readonly string? DefaultPhone;
        public readonly string? Home;

        [OutputConstructor]
        private AddressSection(
            string? address,

            string? business,

            string? cell,

            string? defaultPhone,

            string? home)
        {
            Address = address;
            Business = business;
            Cell = cell;
            DefaultPhone = defaultPhone;
            Home = home;
        }
    }
}
