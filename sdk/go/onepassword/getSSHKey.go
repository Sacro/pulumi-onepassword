// Code generated by Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package onepassword

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func GetSSHKey(ctx *pulumi.Context, args *GetSSHKeyArgs, opts ...pulumi.InvokeOption) (*GetSSHKeyResult, error) {
	var rv GetSSHKeyResult
	err := ctx.Invoke("onepassword:index:GetSSHKey", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type GetSSHKeyArgs struct {
	// The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
	Title *string `pulumi:"title"`
	// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
	Uuid *string `pulumi:"uuid"`
	// The UUID of the vault the item is in.
	Vault string `pulumi:"vault"`
}

type GetSSHKeyResult struct {
	Category   *string               `pulumi:"category"`
	Fields     map[string]GetField   `pulumi:"fields"`
	Notes      *string               `pulumi:"notes"`
	PrivateKey *string               `pulumi:"privateKey"`
	Sections   map[string]GetSection `pulumi:"sections"`
	// An array of strings of the tags assigned to the item.
	Tags []string `pulumi:"tags"`
	// The title of the item.
	Title *string `pulumi:"title"`
	// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
	Uuid *string `pulumi:"uuid"`
	// The UUID of the vault the item is in.
	Vault *string `pulumi:"vault"`
}

func GetSSHKeyOutput(ctx *pulumi.Context, args GetSSHKeyOutputArgs, opts ...pulumi.InvokeOption) GetSSHKeyResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetSSHKeyResult, error) {
			args := v.(GetSSHKeyArgs)
			r, err := GetSSHKey(ctx, &args, opts...)
			var s GetSSHKeyResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetSSHKeyResultOutput)
}

type GetSSHKeyOutputArgs struct {
	// The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
	Title pulumi.StringPtrInput `pulumi:"title"`
	// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
	Uuid pulumi.StringPtrInput `pulumi:"uuid"`
	// The UUID of the vault the item is in.
	Vault pulumi.StringInput `pulumi:"vault"`
}

func (GetSSHKeyOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetSSHKeyArgs)(nil)).Elem()
}

type GetSSHKeyResultOutput struct{ *pulumi.OutputState }

func (GetSSHKeyResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetSSHKeyResult)(nil)).Elem()
}

func (o GetSSHKeyResultOutput) ToGetSSHKeyResultOutput() GetSSHKeyResultOutput {
	return o
}

func (o GetSSHKeyResultOutput) ToGetSSHKeyResultOutputWithContext(ctx context.Context) GetSSHKeyResultOutput {
	return o
}

func (o GetSSHKeyResultOutput) Category() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetSSHKeyResult) *string { return v.Category }).(pulumi.StringPtrOutput)
}

func (o GetSSHKeyResultOutput) Fields() GetFieldMapOutput {
	return o.ApplyT(func(v GetSSHKeyResult) map[string]GetField { return v.Fields }).(GetFieldMapOutput)
}

func (o GetSSHKeyResultOutput) Notes() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetSSHKeyResult) *string { return v.Notes }).(pulumi.StringPtrOutput)
}

func (o GetSSHKeyResultOutput) PrivateKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetSSHKeyResult) *string { return v.PrivateKey }).(pulumi.StringPtrOutput)
}

func (o GetSSHKeyResultOutput) Sections() GetSectionMapOutput {
	return o.ApplyT(func(v GetSSHKeyResult) map[string]GetSection { return v.Sections }).(GetSectionMapOutput)
}

// An array of strings of the tags assigned to the item.
func (o GetSSHKeyResultOutput) Tags() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetSSHKeyResult) []string { return v.Tags }).(pulumi.StringArrayOutput)
}

// The title of the item.
func (o GetSSHKeyResultOutput) Title() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetSSHKeyResult) *string { return v.Title }).(pulumi.StringPtrOutput)
}

// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
func (o GetSSHKeyResultOutput) Uuid() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetSSHKeyResult) *string { return v.Uuid }).(pulumi.StringPtrOutput)
}

// The UUID of the vault the item is in.
func (o GetSSHKeyResultOutput) Vault() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetSSHKeyResult) *string { return v.Vault }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GetSSHKeyResultOutput{})
}
