// Code generated by Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package onepassword

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to get details of a vault by either its name or uuid.
func GetVault(ctx *pulumi.Context, args *GetVaultArgs, opts ...pulumi.InvokeOption) (*GetVaultResult, error) {
	var rv GetVaultResult
	err := ctx.Invoke("one-password-native:index:GetVault", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type GetVaultArgs struct {
	// The vault to get information of.  Can be either the name or the UUID.
	Vault string `pulumi:"vault"`
}

type GetVaultResult struct {
	// The name of the vault to retrieve. This field will be populated with the name of the vault if the vault it looked up by its UUID.
	Name *string `pulumi:"name"`
	// The UUID of the vault to retrieve. This field will be populated with the UUID of the vault if the vault it looked up by its name.
	Uuid *string `pulumi:"uuid"`
}

func GetVaultOutput(ctx *pulumi.Context, args GetVaultOutputArgs, opts ...pulumi.InvokeOption) GetVaultResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetVaultResult, error) {
			args := v.(GetVaultArgs)
			r, err := GetVault(ctx, &args, opts...)
			var s GetVaultResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetVaultResultOutput)
}

type GetVaultOutputArgs struct {
	// The vault to get information of.  Can be either the name or the UUID.
	Vault pulumi.StringInput `pulumi:"vault"`
}

func (GetVaultOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetVaultArgs)(nil)).Elem()
}

type GetVaultResultOutput struct{ *pulumi.OutputState }

func (GetVaultResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetVaultResult)(nil)).Elem()
}

func (o GetVaultResultOutput) ToGetVaultResultOutput() GetVaultResultOutput {
	return o
}

func (o GetVaultResultOutput) ToGetVaultResultOutputWithContext(ctx context.Context) GetVaultResultOutput {
	return o
}

// The name of the vault to retrieve. This field will be populated with the name of the vault if the vault it looked up by its UUID.
func (o GetVaultResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetVaultResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

// The UUID of the vault to retrieve. This field will be populated with the UUID of the vault if the vault it looked up by its name.
func (o GetVaultResultOutput) Uuid() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetVaultResult) *string { return v.Uuid }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GetVaultResultOutput{})
}
