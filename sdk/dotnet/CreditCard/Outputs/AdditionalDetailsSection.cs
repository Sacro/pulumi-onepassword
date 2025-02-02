// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.OnePasswordNative.CreditCard.Outputs
{

    [OutputType]
    public sealed class AdditionalDetailsSection
    {
        public readonly string? CashWithdrawalLimit;
        public readonly string? CreditLimit;
        public readonly string? InterestRate;
        public readonly string? IssueNumber;
        public readonly string? Pin;

        [OutputConstructor]
        private AdditionalDetailsSection(
            string? cashWithdrawalLimit,

            string? creditLimit,

            string? interestRate,

            string? issueNumber,

            string? pin)
        {
            CashWithdrawalLimit = cashWithdrawalLimit;
            CreditLimit = creditLimit;
            InterestRate = interestRate;
            IssueNumber = issueNumber;
            Pin = pin;
        }
    }
}
