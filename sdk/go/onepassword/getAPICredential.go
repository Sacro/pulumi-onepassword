// Code generated by Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package onepassword

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func GetAPICredential(ctx *pulumi.Context, args *GetAPICredentialArgs, opts ...pulumi.InvokeOption) (*GetAPICredentialResult, error) {
	var rv GetAPICredentialResult
	err := ctx.Invoke("one-password-native:index:GetAPICredential", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type GetAPICredentialArgs struct {
	// The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
	Title *string `pulumi:"title"`
	// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
	Uuid *string `pulumi:"uuid"`
	// The UUID of the vault the item is in.
	Vault string `pulumi:"vault"`
}

type GetAPICredentialResult struct {
	Attachments map[string]OutField   `pulumi:"attachments"`
	Category    string                `pulumi:"category"`
	Credential  *string               `pulumi:"credential"`
	Expires     *string               `pulumi:"expires"`
	Fields      map[string]OutField   `pulumi:"fields"`
	Filename    *string               `pulumi:"filename"`
	Hostname    *string               `pulumi:"hostname"`
	Notes       *string               `pulumi:"notes"`
	References  map[string]OutField   `pulumi:"references"`
	Sections    map[string]OutSection `pulumi:"sections"`
	// An array of strings of the tags assigned to the item.
	Tags []string `pulumi:"tags"`
	// The title of the item.
	Title    string  `pulumi:"title"`
	Type     *string `pulumi:"type"`
	Username *string `pulumi:"username"`
	// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
	Uuid      string  `pulumi:"uuid"`
	ValidFrom *string `pulumi:"validFrom"`
	// The UUID of the vault the item is in.
	Vault string `pulumi:"vault"`
}

func GetAPICredentialOutput(ctx *pulumi.Context, args GetAPICredentialOutputArgs, opts ...pulumi.InvokeOption) GetAPICredentialResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetAPICredentialResult, error) {
			args := v.(GetAPICredentialArgs)
			r, err := GetAPICredential(ctx, &args, opts...)
			var s GetAPICredentialResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetAPICredentialResultOutput)
}

type GetAPICredentialOutputArgs struct {
	// The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
	Title pulumi.StringPtrInput `pulumi:"title"`
	// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
	Uuid pulumi.StringPtrInput `pulumi:"uuid"`
	// The UUID of the vault the item is in.
	Vault pulumi.StringInput `pulumi:"vault"`
}

func (GetAPICredentialOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetAPICredentialArgs)(nil)).Elem()
}

type GetAPICredentialResultOutput struct{ *pulumi.OutputState }

func (GetAPICredentialResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetAPICredentialResult)(nil)).Elem()
}

func (o GetAPICredentialResultOutput) ToGetAPICredentialResultOutput() GetAPICredentialResultOutput {
	return o
}

func (o GetAPICredentialResultOutput) ToGetAPICredentialResultOutputWithContext(ctx context.Context) GetAPICredentialResultOutput {
	return o
}

func (o GetAPICredentialResultOutput) Attachments() OutFieldMapOutput {
	return o.ApplyT(func(v GetAPICredentialResult) map[string]OutField { return v.Attachments }).(OutFieldMapOutput)
}

func (o GetAPICredentialResultOutput) Category() pulumi.StringOutput {
	return o.ApplyT(func(v GetAPICredentialResult) string { return v.Category }).(pulumi.StringOutput)
}

func (o GetAPICredentialResultOutput) Credential() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetAPICredentialResult) *string { return v.Credential }).(pulumi.StringPtrOutput)
}

func (o GetAPICredentialResultOutput) Expires() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetAPICredentialResult) *string { return v.Expires }).(pulumi.StringPtrOutput)
}

func (o GetAPICredentialResultOutput) Fields() OutFieldMapOutput {
	return o.ApplyT(func(v GetAPICredentialResult) map[string]OutField { return v.Fields }).(OutFieldMapOutput)
}

func (o GetAPICredentialResultOutput) Filename() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetAPICredentialResult) *string { return v.Filename }).(pulumi.StringPtrOutput)
}

func (o GetAPICredentialResultOutput) Hostname() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetAPICredentialResult) *string { return v.Hostname }).(pulumi.StringPtrOutput)
}

func (o GetAPICredentialResultOutput) Notes() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetAPICredentialResult) *string { return v.Notes }).(pulumi.StringPtrOutput)
}

func (o GetAPICredentialResultOutput) References() OutFieldMapOutput {
	return o.ApplyT(func(v GetAPICredentialResult) map[string]OutField { return v.References }).(OutFieldMapOutput)
}

func (o GetAPICredentialResultOutput) Sections() OutSectionMapOutput {
	return o.ApplyT(func(v GetAPICredentialResult) map[string]OutSection { return v.Sections }).(OutSectionMapOutput)
}

// An array of strings of the tags assigned to the item.
func (o GetAPICredentialResultOutput) Tags() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetAPICredentialResult) []string { return v.Tags }).(pulumi.StringArrayOutput)
}

// The title of the item.
func (o GetAPICredentialResultOutput) Title() pulumi.StringOutput {
	return o.ApplyT(func(v GetAPICredentialResult) string { return v.Title }).(pulumi.StringOutput)
}

func (o GetAPICredentialResultOutput) Type() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetAPICredentialResult) *string { return v.Type }).(pulumi.StringPtrOutput)
}

func (o GetAPICredentialResultOutput) Username() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetAPICredentialResult) *string { return v.Username }).(pulumi.StringPtrOutput)
}

// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
func (o GetAPICredentialResultOutput) Uuid() pulumi.StringOutput {
	return o.ApplyT(func(v GetAPICredentialResult) string { return v.Uuid }).(pulumi.StringOutput)
}

func (o GetAPICredentialResultOutput) ValidFrom() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetAPICredentialResult) *string { return v.ValidFrom }).(pulumi.StringPtrOutput)
}

// The UUID of the vault the item is in.
func (o GetAPICredentialResultOutput) Vault() pulumi.StringOutput {
	return o.ApplyT(func(v GetAPICredentialResult) string { return v.Vault }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetAPICredentialResultOutput{})
}
