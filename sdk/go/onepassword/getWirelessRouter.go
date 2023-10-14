// Code generated by Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package onepassword

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func LookupWirelessRouter(ctx *pulumi.Context, args *LookupWirelessRouterArgs, opts ...pulumi.InvokeOption) (*LookupWirelessRouterResult, error) {
	var rv LookupWirelessRouterResult
	err := ctx.Invoke("onepassword:index:GetWirelessRouter", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupWirelessRouterArgs struct {
	// The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
	Title *string `pulumi:"title"`
	// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
	Uuid *string `pulumi:"uuid"`
	// The UUID of the vault the item is in.
	Vault string `pulumi:"vault"`
}

type LookupWirelessRouterResult struct {
	AirPortId               *string      `pulumi:"airPortId"`
	AttachedStoragePassword *string      `pulumi:"attachedStoragePassword"`
	BaseStationName         *string      `pulumi:"baseStationName"`
	BaseStationPassword     *string      `pulumi:"baseStationPassword"`
	Category                *string      `pulumi:"category"`
	Fields                  []GetField   `pulumi:"fields"`
	Id                      *string      `pulumi:"id"`
	NetworkName             *string      `pulumi:"networkName"`
	Notes                   *string      `pulumi:"notes"`
	Sections                []GetSection `pulumi:"sections"`
	ServerIpAddress         *string      `pulumi:"serverIpAddress"`
	// An array of strings of the tags assigned to the item.
	Tags []string `pulumi:"tags"`
	// The title of the item.
	Title *string `pulumi:"title"`
	// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
	Uuid *string `pulumi:"uuid"`
	// The UUID of the vault the item is in.
	Vault                   *string `pulumi:"vault"`
	WirelessNetworkPassword *string `pulumi:"wirelessNetworkPassword"`
	WirelessSecurity        *string `pulumi:"wirelessSecurity"`
}

func LookupWirelessRouterOutput(ctx *pulumi.Context, args LookupWirelessRouterOutputArgs, opts ...pulumi.InvokeOption) LookupWirelessRouterResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupWirelessRouterResult, error) {
			args := v.(LookupWirelessRouterArgs)
			r, err := LookupWirelessRouter(ctx, &args, opts...)
			var s LookupWirelessRouterResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupWirelessRouterResultOutput)
}

type LookupWirelessRouterOutputArgs struct {
	// The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
	Title pulumi.StringPtrInput `pulumi:"title"`
	// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
	Uuid pulumi.StringPtrInput `pulumi:"uuid"`
	// The UUID of the vault the item is in.
	Vault pulumi.StringInput `pulumi:"vault"`
}

func (LookupWirelessRouterOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupWirelessRouterArgs)(nil)).Elem()
}

type LookupWirelessRouterResultOutput struct{ *pulumi.OutputState }

func (LookupWirelessRouterResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupWirelessRouterResult)(nil)).Elem()
}

func (o LookupWirelessRouterResultOutput) ToLookupWirelessRouterResultOutput() LookupWirelessRouterResultOutput {
	return o
}

func (o LookupWirelessRouterResultOutput) ToLookupWirelessRouterResultOutputWithContext(ctx context.Context) LookupWirelessRouterResultOutput {
	return o
}

func (o LookupWirelessRouterResultOutput) AirPortId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWirelessRouterResult) *string { return v.AirPortId }).(pulumi.StringPtrOutput)
}

func (o LookupWirelessRouterResultOutput) AttachedStoragePassword() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWirelessRouterResult) *string { return v.AttachedStoragePassword }).(pulumi.StringPtrOutput)
}

func (o LookupWirelessRouterResultOutput) BaseStationName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWirelessRouterResult) *string { return v.BaseStationName }).(pulumi.StringPtrOutput)
}

func (o LookupWirelessRouterResultOutput) BaseStationPassword() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWirelessRouterResult) *string { return v.BaseStationPassword }).(pulumi.StringPtrOutput)
}

func (o LookupWirelessRouterResultOutput) Category() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWirelessRouterResult) *string { return v.Category }).(pulumi.StringPtrOutput)
}

func (o LookupWirelessRouterResultOutput) Fields() GetFieldArrayOutput {
	return o.ApplyT(func(v LookupWirelessRouterResult) []GetField { return v.Fields }).(GetFieldArrayOutput)
}

func (o LookupWirelessRouterResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWirelessRouterResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupWirelessRouterResultOutput) NetworkName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWirelessRouterResult) *string { return v.NetworkName }).(pulumi.StringPtrOutput)
}

func (o LookupWirelessRouterResultOutput) Notes() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWirelessRouterResult) *string { return v.Notes }).(pulumi.StringPtrOutput)
}

func (o LookupWirelessRouterResultOutput) Sections() GetSectionArrayOutput {
	return o.ApplyT(func(v LookupWirelessRouterResult) []GetSection { return v.Sections }).(GetSectionArrayOutput)
}

func (o LookupWirelessRouterResultOutput) ServerIpAddress() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWirelessRouterResult) *string { return v.ServerIpAddress }).(pulumi.StringPtrOutput)
}

// An array of strings of the tags assigned to the item.
func (o LookupWirelessRouterResultOutput) Tags() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupWirelessRouterResult) []string { return v.Tags }).(pulumi.StringArrayOutput)
}

// The title of the item.
func (o LookupWirelessRouterResultOutput) Title() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWirelessRouterResult) *string { return v.Title }).(pulumi.StringPtrOutput)
}

// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
func (o LookupWirelessRouterResultOutput) Uuid() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWirelessRouterResult) *string { return v.Uuid }).(pulumi.StringPtrOutput)
}

// The UUID of the vault the item is in.
func (o LookupWirelessRouterResultOutput) Vault() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWirelessRouterResult) *string { return v.Vault }).(pulumi.StringPtrOutput)
}

func (o LookupWirelessRouterResultOutput) WirelessNetworkPassword() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWirelessRouterResult) *string { return v.WirelessNetworkPassword }).(pulumi.StringPtrOutput)
}

func (o LookupWirelessRouterResultOutput) WirelessSecurity() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWirelessRouterResult) *string { return v.WirelessSecurity }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupWirelessRouterResultOutput{})
}
