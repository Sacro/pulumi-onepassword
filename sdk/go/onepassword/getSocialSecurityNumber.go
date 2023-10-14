// Code generated by Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package onepassword

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func LookupSocialSecurityNumber(ctx *pulumi.Context, args *LookupSocialSecurityNumberArgs, opts ...pulumi.InvokeOption) (*LookupSocialSecurityNumberResult, error) {
	var rv LookupSocialSecurityNumberResult
	err := ctx.Invoke("onepassword:index:GetSocialSecurityNumber", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupSocialSecurityNumberArgs struct {
	// The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
	Title *string `pulumi:"title"`
	// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
	Uuid *string `pulumi:"uuid"`
	// The UUID of the vault the item is in.
	Vault string `pulumi:"vault"`
}

type LookupSocialSecurityNumberResult struct {
	Category *string      `pulumi:"category"`
	Fields   []GetField   `pulumi:"fields"`
	Id       *string      `pulumi:"id"`
	Name     *string      `pulumi:"name"`
	Notes    *string      `pulumi:"notes"`
	Number   *string      `pulumi:"number"`
	Sections []GetSection `pulumi:"sections"`
	// An array of strings of the tags assigned to the item.
	Tags []string `pulumi:"tags"`
	// The title of the item.
	Title *string `pulumi:"title"`
	// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
	Uuid *string `pulumi:"uuid"`
	// The UUID of the vault the item is in.
	Vault *string `pulumi:"vault"`
}

func LookupSocialSecurityNumberOutput(ctx *pulumi.Context, args LookupSocialSecurityNumberOutputArgs, opts ...pulumi.InvokeOption) LookupSocialSecurityNumberResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupSocialSecurityNumberResult, error) {
			args := v.(LookupSocialSecurityNumberArgs)
			r, err := LookupSocialSecurityNumber(ctx, &args, opts...)
			var s LookupSocialSecurityNumberResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupSocialSecurityNumberResultOutput)
}

type LookupSocialSecurityNumberOutputArgs struct {
	// The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
	Title pulumi.StringPtrInput `pulumi:"title"`
	// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
	Uuid pulumi.StringPtrInput `pulumi:"uuid"`
	// The UUID of the vault the item is in.
	Vault pulumi.StringInput `pulumi:"vault"`
}

func (LookupSocialSecurityNumberOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSocialSecurityNumberArgs)(nil)).Elem()
}

type LookupSocialSecurityNumberResultOutput struct{ *pulumi.OutputState }

func (LookupSocialSecurityNumberResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSocialSecurityNumberResult)(nil)).Elem()
}

func (o LookupSocialSecurityNumberResultOutput) ToLookupSocialSecurityNumberResultOutput() LookupSocialSecurityNumberResultOutput {
	return o
}

func (o LookupSocialSecurityNumberResultOutput) ToLookupSocialSecurityNumberResultOutputWithContext(ctx context.Context) LookupSocialSecurityNumberResultOutput {
	return o
}

func (o LookupSocialSecurityNumberResultOutput) Category() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSocialSecurityNumberResult) *string { return v.Category }).(pulumi.StringPtrOutput)
}

func (o LookupSocialSecurityNumberResultOutput) Fields() GetFieldArrayOutput {
	return o.ApplyT(func(v LookupSocialSecurityNumberResult) []GetField { return v.Fields }).(GetFieldArrayOutput)
}

func (o LookupSocialSecurityNumberResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSocialSecurityNumberResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupSocialSecurityNumberResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSocialSecurityNumberResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupSocialSecurityNumberResultOutput) Notes() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSocialSecurityNumberResult) *string { return v.Notes }).(pulumi.StringPtrOutput)
}

func (o LookupSocialSecurityNumberResultOutput) Number() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSocialSecurityNumberResult) *string { return v.Number }).(pulumi.StringPtrOutput)
}

func (o LookupSocialSecurityNumberResultOutput) Sections() GetSectionArrayOutput {
	return o.ApplyT(func(v LookupSocialSecurityNumberResult) []GetSection { return v.Sections }).(GetSectionArrayOutput)
}

// An array of strings of the tags assigned to the item.
func (o LookupSocialSecurityNumberResultOutput) Tags() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupSocialSecurityNumberResult) []string { return v.Tags }).(pulumi.StringArrayOutput)
}

// The title of the item.
func (o LookupSocialSecurityNumberResultOutput) Title() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSocialSecurityNumberResult) *string { return v.Title }).(pulumi.StringPtrOutput)
}

// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
func (o LookupSocialSecurityNumberResultOutput) Uuid() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSocialSecurityNumberResult) *string { return v.Uuid }).(pulumi.StringPtrOutput)
}

// The UUID of the vault the item is in.
func (o LookupSocialSecurityNumberResultOutput) Vault() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSocialSecurityNumberResult) *string { return v.Vault }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupSocialSecurityNumberResultOutput{})
}
