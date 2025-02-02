// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.OnePasswordNative.EmailAccount.Outputs
{

    [OutputType]
    public sealed class ContactInformationSection
    {
        public readonly string? PhoneLocal;
        public readonly string? PhoneTollFree;
        public readonly string? Provider;
        public readonly string? ProvidersWebsite;

        [OutputConstructor]
        private ContactInformationSection(
            string? phoneLocal,

            string? phoneTollFree,

            string? provider,

            string? providersWebsite)
        {
            PhoneLocal = phoneLocal;
            PhoneTollFree = phoneTollFree;
            Provider = provider;
            ProvidersWebsite = providersWebsite;
        }
    }
}
