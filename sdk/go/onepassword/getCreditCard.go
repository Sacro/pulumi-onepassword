// Code generated by Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package onepassword

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-onepassword/sdk/go/onepassword/creditcard"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func GetCreditCard(ctx *pulumi.Context, args *GetCreditCardArgs, opts ...pulumi.InvokeOption) (*GetCreditCardResult, error) {
	var rv GetCreditCardResult
	err := ctx.Invoke("onepassword:index:GetCreditCard", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type GetCreditCardArgs struct {
	// The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
	Title *string `pulumi:"title"`
	// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
	Uuid *string `pulumi:"uuid"`
	// The UUID of the vault the item is in.
	Vault string `pulumi:"vault"`
}

type GetCreditCardResult struct {
	AdditionalDetails  *creditcard.AdditionalDetailsSection  `pulumi:"additionalDetails"`
	CardholderName     *string                               `pulumi:"cardholderName"`
	Category           *string                               `pulumi:"category"`
	ContactInformation *creditcard.ContactInformationSection `pulumi:"contactInformation"`
	ExpiryDate         *string                               `pulumi:"expiryDate"`
	Fields             map[string]GetField                   `pulumi:"fields"`
	Notes              *string                               `pulumi:"notes"`
	Number             *string                               `pulumi:"number"`
	Sections           map[string]GetSection                 `pulumi:"sections"`
	// An array of strings of the tags assigned to the item.
	Tags []string `pulumi:"tags"`
	// The title of the item.
	Title *string `pulumi:"title"`
	Type  *string `pulumi:"type"`
	// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
	Uuid      *string `pulumi:"uuid"`
	ValidFrom *string `pulumi:"validFrom"`
	// The UUID of the vault the item is in.
	Vault              *string `pulumi:"vault"`
	VerificationNumber *string `pulumi:"verificationNumber"`
}

func GetCreditCardOutput(ctx *pulumi.Context, args GetCreditCardOutputArgs, opts ...pulumi.InvokeOption) GetCreditCardResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetCreditCardResult, error) {
			args := v.(GetCreditCardArgs)
			r, err := GetCreditCard(ctx, &args, opts...)
			var s GetCreditCardResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetCreditCardResultOutput)
}

type GetCreditCardOutputArgs struct {
	// The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
	Title pulumi.StringPtrInput `pulumi:"title"`
	// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
	Uuid pulumi.StringPtrInput `pulumi:"uuid"`
	// The UUID of the vault the item is in.
	Vault pulumi.StringInput `pulumi:"vault"`
}

func (GetCreditCardOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetCreditCardArgs)(nil)).Elem()
}

type GetCreditCardResultOutput struct{ *pulumi.OutputState }

func (GetCreditCardResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetCreditCardResult)(nil)).Elem()
}

func (o GetCreditCardResultOutput) ToGetCreditCardResultOutput() GetCreditCardResultOutput {
	return o
}

func (o GetCreditCardResultOutput) ToGetCreditCardResultOutputWithContext(ctx context.Context) GetCreditCardResultOutput {
	return o
}

func (o GetCreditCardResultOutput) AdditionalDetails() creditcard.AdditionalDetailsSectionPtrOutput {
	return o.ApplyT(func(v GetCreditCardResult) *creditcard.AdditionalDetailsSection { return v.AdditionalDetails }).(creditcard.AdditionalDetailsSectionPtrOutput)
}

func (o GetCreditCardResultOutput) CardholderName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetCreditCardResult) *string { return v.CardholderName }).(pulumi.StringPtrOutput)
}

func (o GetCreditCardResultOutput) Category() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetCreditCardResult) *string { return v.Category }).(pulumi.StringPtrOutput)
}

func (o GetCreditCardResultOutput) ContactInformation() creditcard.ContactInformationSectionPtrOutput {
	return o.ApplyT(func(v GetCreditCardResult) *creditcard.ContactInformationSection { return v.ContactInformation }).(creditcard.ContactInformationSectionPtrOutput)
}

func (o GetCreditCardResultOutput) ExpiryDate() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetCreditCardResult) *string { return v.ExpiryDate }).(pulumi.StringPtrOutput)
}

func (o GetCreditCardResultOutput) Fields() GetFieldMapOutput {
	return o.ApplyT(func(v GetCreditCardResult) map[string]GetField { return v.Fields }).(GetFieldMapOutput)
}

func (o GetCreditCardResultOutput) Notes() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetCreditCardResult) *string { return v.Notes }).(pulumi.StringPtrOutput)
}

func (o GetCreditCardResultOutput) Number() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetCreditCardResult) *string { return v.Number }).(pulumi.StringPtrOutput)
}

func (o GetCreditCardResultOutput) Sections() GetSectionMapOutput {
	return o.ApplyT(func(v GetCreditCardResult) map[string]GetSection { return v.Sections }).(GetSectionMapOutput)
}

// An array of strings of the tags assigned to the item.
func (o GetCreditCardResultOutput) Tags() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetCreditCardResult) []string { return v.Tags }).(pulumi.StringArrayOutput)
}

// The title of the item.
func (o GetCreditCardResultOutput) Title() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetCreditCardResult) *string { return v.Title }).(pulumi.StringPtrOutput)
}

func (o GetCreditCardResultOutput) Type() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetCreditCardResult) *string { return v.Type }).(pulumi.StringPtrOutput)
}

// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
func (o GetCreditCardResultOutput) Uuid() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetCreditCardResult) *string { return v.Uuid }).(pulumi.StringPtrOutput)
}

func (o GetCreditCardResultOutput) ValidFrom() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetCreditCardResult) *string { return v.ValidFrom }).(pulumi.StringPtrOutput)
}

// The UUID of the vault the item is in.
func (o GetCreditCardResultOutput) Vault() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetCreditCardResult) *string { return v.Vault }).(pulumi.StringPtrOutput)
}

func (o GetCreditCardResultOutput) VerificationNumber() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetCreditCardResult) *string { return v.VerificationNumber }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GetCreditCardResultOutput{})
}
