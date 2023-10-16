// Code generated by Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package onepassword

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-onepassword/sdk/go/onepassword/softwarelicense"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func GetSoftwareLicense(ctx *pulumi.Context, args *GetSoftwareLicenseArgs, opts ...pulumi.InvokeOption) (*GetSoftwareLicenseResult, error) {
	var rv GetSoftwareLicenseResult
	err := ctx.Invoke("onepassword:index:GetSoftwareLicense", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type GetSoftwareLicenseArgs struct {
	// The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
	Title *string `pulumi:"title"`
	// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
	Uuid *string `pulumi:"uuid"`
	// The UUID of the vault the item is in.
	Vault string `pulumi:"vault"`
}

type GetSoftwareLicenseResult struct {
	Category   *string                           `pulumi:"category"`
	Customer   *softwarelicense.CustomerSection  `pulumi:"customer"`
	Fields     map[string]GetField               `pulumi:"fields"`
	LicenseKey *string                           `pulumi:"licenseKey"`
	Notes      *string                           `pulumi:"notes"`
	Order      *softwarelicense.OrderSection     `pulumi:"order"`
	Publisher  *softwarelicense.PublisherSection `pulumi:"publisher"`
	Sections   map[string]GetSection             `pulumi:"sections"`
	// An array of strings of the tags assigned to the item.
	Tags []string `pulumi:"tags"`
	// The title of the item.
	Title *string `pulumi:"title"`
	// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
	Uuid *string `pulumi:"uuid"`
	// The UUID of the vault the item is in.
	Vault   *string `pulumi:"vault"`
	Version *string `pulumi:"version"`
}

func GetSoftwareLicenseOutput(ctx *pulumi.Context, args GetSoftwareLicenseOutputArgs, opts ...pulumi.InvokeOption) GetSoftwareLicenseResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetSoftwareLicenseResult, error) {
			args := v.(GetSoftwareLicenseArgs)
			r, err := GetSoftwareLicense(ctx, &args, opts...)
			var s GetSoftwareLicenseResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetSoftwareLicenseResultOutput)
}

type GetSoftwareLicenseOutputArgs struct {
	// The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
	Title pulumi.StringPtrInput `pulumi:"title"`
	// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
	Uuid pulumi.StringPtrInput `pulumi:"uuid"`
	// The UUID of the vault the item is in.
	Vault pulumi.StringInput `pulumi:"vault"`
}

func (GetSoftwareLicenseOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetSoftwareLicenseArgs)(nil)).Elem()
}

type GetSoftwareLicenseResultOutput struct{ *pulumi.OutputState }

func (GetSoftwareLicenseResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetSoftwareLicenseResult)(nil)).Elem()
}

func (o GetSoftwareLicenseResultOutput) ToGetSoftwareLicenseResultOutput() GetSoftwareLicenseResultOutput {
	return o
}

func (o GetSoftwareLicenseResultOutput) ToGetSoftwareLicenseResultOutputWithContext(ctx context.Context) GetSoftwareLicenseResultOutput {
	return o
}

func (o GetSoftwareLicenseResultOutput) Category() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetSoftwareLicenseResult) *string { return v.Category }).(pulumi.StringPtrOutput)
}

func (o GetSoftwareLicenseResultOutput) Customer() softwarelicense.CustomerSectionPtrOutput {
	return o.ApplyT(func(v GetSoftwareLicenseResult) *softwarelicense.CustomerSection { return v.Customer }).(softwarelicense.CustomerSectionPtrOutput)
}

func (o GetSoftwareLicenseResultOutput) Fields() GetFieldMapOutput {
	return o.ApplyT(func(v GetSoftwareLicenseResult) map[string]GetField { return v.Fields }).(GetFieldMapOutput)
}

func (o GetSoftwareLicenseResultOutput) LicenseKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetSoftwareLicenseResult) *string { return v.LicenseKey }).(pulumi.StringPtrOutput)
}

func (o GetSoftwareLicenseResultOutput) Notes() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetSoftwareLicenseResult) *string { return v.Notes }).(pulumi.StringPtrOutput)
}

func (o GetSoftwareLicenseResultOutput) Order() softwarelicense.OrderSectionPtrOutput {
	return o.ApplyT(func(v GetSoftwareLicenseResult) *softwarelicense.OrderSection { return v.Order }).(softwarelicense.OrderSectionPtrOutput)
}

func (o GetSoftwareLicenseResultOutput) Publisher() softwarelicense.PublisherSectionPtrOutput {
	return o.ApplyT(func(v GetSoftwareLicenseResult) *softwarelicense.PublisherSection { return v.Publisher }).(softwarelicense.PublisherSectionPtrOutput)
}

func (o GetSoftwareLicenseResultOutput) Sections() GetSectionMapOutput {
	return o.ApplyT(func(v GetSoftwareLicenseResult) map[string]GetSection { return v.Sections }).(GetSectionMapOutput)
}

// An array of strings of the tags assigned to the item.
func (o GetSoftwareLicenseResultOutput) Tags() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetSoftwareLicenseResult) []string { return v.Tags }).(pulumi.StringArrayOutput)
}

// The title of the item.
func (o GetSoftwareLicenseResultOutput) Title() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetSoftwareLicenseResult) *string { return v.Title }).(pulumi.StringPtrOutput)
}

// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
func (o GetSoftwareLicenseResultOutput) Uuid() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetSoftwareLicenseResult) *string { return v.Uuid }).(pulumi.StringPtrOutput)
}

// The UUID of the vault the item is in.
func (o GetSoftwareLicenseResultOutput) Vault() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetSoftwareLicenseResult) *string { return v.Vault }).(pulumi.StringPtrOutput)
}

func (o GetSoftwareLicenseResultOutput) Version() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetSoftwareLicenseResult) *string { return v.Version }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GetSoftwareLicenseResultOutput{})
}
