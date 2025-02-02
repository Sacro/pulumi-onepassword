// Code generated by Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package onepassword

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/Sacro/pulumi-onepassword/sdk/go/onepassword/cryptowallet"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type CryptoWalletItem struct {
	pulumi.CustomResourceState

	Attachments    OutFieldMapOutput      `pulumi:"attachments"`
	Category       pulumi.StringOutput    `pulumi:"category"`
	Fields         OutFieldMapOutput      `pulumi:"fields"`
	Notes          pulumi.StringPtrOutput `pulumi:"notes"`
	Password       pulumi.StringPtrOutput `pulumi:"password"`
	RecoveryPhrase pulumi.StringPtrOutput `pulumi:"recoveryPhrase"`
	References     OutFieldMapOutput      `pulumi:"references"`
	Sections       OutSectionMapOutput    `pulumi:"sections"`
	// An array of strings of the tags assigned to the item.
	Tags pulumi.StringArrayOutput `pulumi:"tags"`
	// The title of the item.
	Title pulumi.StringOutput `pulumi:"title"`
	// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
	Uuid pulumi.StringOutput `pulumi:"uuid"`
	// The UUID of the vault the item is in.
	Vault  pulumi.StringOutput                 `pulumi:"vault"`
	Wallet cryptowallet.WalletSectionPtrOutput `pulumi:"wallet"`
}

// NewCryptoWalletItem registers a new resource with the given unique name, arguments, and options.
func NewCryptoWalletItem(ctx *pulumi.Context,
	name string, args *CryptoWalletItemArgs, opts ...pulumi.ResourceOption) (*CryptoWalletItem, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Vault == nil {
		return nil, errors.New("invalid value for required argument 'Vault'")
	}
	args.Category = pulumi.StringPtr("Crypto Wallet")
	if args.Password != nil {
		args.Password = pulumi.ToSecret(args.Password).(pulumi.StringPtrOutput)
	}
	if args.RecoveryPhrase != nil {
		args.RecoveryPhrase = pulumi.ToSecret(args.RecoveryPhrase).(pulumi.StringPtrOutput)
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"attachments",
		"fields",
		"password",
		"recoveryPhrase",
		"references",
		"sections",
	})
	opts = append(opts, secrets)
	var resource CryptoWalletItem
	err := ctx.RegisterResource("one-password-native:index:CryptoWalletItem", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCryptoWalletItem gets an existing CryptoWalletItem resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCryptoWalletItem(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CryptoWalletItemState, opts ...pulumi.ResourceOption) (*CryptoWalletItem, error) {
	var resource CryptoWalletItem
	err := ctx.ReadResource("one-password-native:index:CryptoWalletItem", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering CryptoWalletItem resources.
type cryptoWalletItemState struct {
	// The UUID of the vault the item is in.
	Vault *string `pulumi:"vault"`
}

type CryptoWalletItemState struct {
	// The UUID of the vault the item is in.
	Vault pulumi.StringInput
}

func (CryptoWalletItemState) ElementType() reflect.Type {
	return reflect.TypeOf((*cryptoWalletItemState)(nil)).Elem()
}

type cryptoWalletItemArgs struct {
	Attachments map[string]pulumi.AssetOrArchive `pulumi:"attachments"`
	// The category of the vault the item is in.
	Category       *string            `pulumi:"category"`
	Fields         map[string]Field   `pulumi:"fields"`
	Notes          *string            `pulumi:"notes"`
	Password       *string            `pulumi:"password"`
	RecoveryPhrase *string            `pulumi:"recoveryPhrase"`
	Sections       map[string]Section `pulumi:"sections"`
	// An array of strings of the tags assigned to the item.
	Tags []string `pulumi:"tags"`
	// The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
	Title *string `pulumi:"title"`
	// The UUID of the vault the item is in.
	Vault  string                      `pulumi:"vault"`
	Wallet *cryptowallet.WalletSection `pulumi:"wallet"`
}

// The set of arguments for constructing a CryptoWalletItem resource.
type CryptoWalletItemArgs struct {
	Attachments pulumi.AssetOrArchiveMapInput
	// The category of the vault the item is in.
	Category       pulumi.StringPtrInput
	Fields         FieldMapInput
	Notes          pulumi.StringPtrInput
	Password       pulumi.StringPtrInput
	RecoveryPhrase pulumi.StringPtrInput
	Sections       SectionMapInput
	// An array of strings of the tags assigned to the item.
	Tags pulumi.StringArrayInput
	// The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
	Title pulumi.StringPtrInput
	// The UUID of the vault the item is in.
	Vault  pulumi.StringInput
	Wallet cryptowallet.WalletSectionPtrInput
}

func (CryptoWalletItemArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*cryptoWalletItemArgs)(nil)).Elem()
}

func (r *CryptoWalletItem) GetAttachment(ctx *pulumi.Context, args *CryptoWalletItemGetAttachmentArgs) (CryptoWalletItemGetAttachmentResultOutput, error) {
	out, err := ctx.Call("one-password-native:index:CryptoWalletItem/attachment", args, CryptoWalletItemGetAttachmentResultOutput{}, r)
	if err != nil {
		return CryptoWalletItemGetAttachmentResultOutput{}, err
	}
	return out.(CryptoWalletItemGetAttachmentResultOutput), nil
}

type cryptoWalletItemGetAttachmentArgs struct {
	// The name or uuid of the attachment to get
	Name string `pulumi:"name"`
}

// The set of arguments for the GetAttachment method of the CryptoWalletItem resource.
type CryptoWalletItemGetAttachmentArgs struct {
	// The name or uuid of the attachment to get
	Name pulumi.StringInput
}

func (CryptoWalletItemGetAttachmentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*cryptoWalletItemGetAttachmentArgs)(nil)).Elem()
}

// The resolved reference value
type CryptoWalletItemGetAttachmentResult struct {
	// the value of the attachment
	Value string `pulumi:"value"`
}

type CryptoWalletItemGetAttachmentResultOutput struct{ *pulumi.OutputState }

func (CryptoWalletItemGetAttachmentResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*CryptoWalletItemGetAttachmentResult)(nil)).Elem()
}

// the value of the attachment
func (o CryptoWalletItemGetAttachmentResultOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v CryptoWalletItemGetAttachmentResult) string { return v.Value }).(pulumi.StringOutput)
}

type CryptoWalletItemInput interface {
	pulumi.Input

	ToCryptoWalletItemOutput() CryptoWalletItemOutput
	ToCryptoWalletItemOutputWithContext(ctx context.Context) CryptoWalletItemOutput
}

func (*CryptoWalletItem) ElementType() reflect.Type {
	return reflect.TypeOf((**CryptoWalletItem)(nil)).Elem()
}

func (i *CryptoWalletItem) ToCryptoWalletItemOutput() CryptoWalletItemOutput {
	return i.ToCryptoWalletItemOutputWithContext(context.Background())
}

func (i *CryptoWalletItem) ToCryptoWalletItemOutputWithContext(ctx context.Context) CryptoWalletItemOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CryptoWalletItemOutput)
}

// CryptoWalletItemArrayInput is an input type that accepts CryptoWalletItemArray and CryptoWalletItemArrayOutput values.
// You can construct a concrete instance of `CryptoWalletItemArrayInput` via:
//
//	CryptoWalletItemArray{ CryptoWalletItemArgs{...} }
type CryptoWalletItemArrayInput interface {
	pulumi.Input

	ToCryptoWalletItemArrayOutput() CryptoWalletItemArrayOutput
	ToCryptoWalletItemArrayOutputWithContext(context.Context) CryptoWalletItemArrayOutput
}

type CryptoWalletItemArray []CryptoWalletItemInput

func (CryptoWalletItemArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*CryptoWalletItem)(nil)).Elem()
}

func (i CryptoWalletItemArray) ToCryptoWalletItemArrayOutput() CryptoWalletItemArrayOutput {
	return i.ToCryptoWalletItemArrayOutputWithContext(context.Background())
}

func (i CryptoWalletItemArray) ToCryptoWalletItemArrayOutputWithContext(ctx context.Context) CryptoWalletItemArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CryptoWalletItemArrayOutput)
}

// CryptoWalletItemMapInput is an input type that accepts CryptoWalletItemMap and CryptoWalletItemMapOutput values.
// You can construct a concrete instance of `CryptoWalletItemMapInput` via:
//
//	CryptoWalletItemMap{ "key": CryptoWalletItemArgs{...} }
type CryptoWalletItemMapInput interface {
	pulumi.Input

	ToCryptoWalletItemMapOutput() CryptoWalletItemMapOutput
	ToCryptoWalletItemMapOutputWithContext(context.Context) CryptoWalletItemMapOutput
}

type CryptoWalletItemMap map[string]CryptoWalletItemInput

func (CryptoWalletItemMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*CryptoWalletItem)(nil)).Elem()
}

func (i CryptoWalletItemMap) ToCryptoWalletItemMapOutput() CryptoWalletItemMapOutput {
	return i.ToCryptoWalletItemMapOutputWithContext(context.Background())
}

func (i CryptoWalletItemMap) ToCryptoWalletItemMapOutputWithContext(ctx context.Context) CryptoWalletItemMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CryptoWalletItemMapOutput)
}

type CryptoWalletItemOutput struct{ *pulumi.OutputState }

func (CryptoWalletItemOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**CryptoWalletItem)(nil)).Elem()
}

func (o CryptoWalletItemOutput) ToCryptoWalletItemOutput() CryptoWalletItemOutput {
	return o
}

func (o CryptoWalletItemOutput) ToCryptoWalletItemOutputWithContext(ctx context.Context) CryptoWalletItemOutput {
	return o
}

type CryptoWalletItemArrayOutput struct{ *pulumi.OutputState }

func (CryptoWalletItemArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*CryptoWalletItem)(nil)).Elem()
}

func (o CryptoWalletItemArrayOutput) ToCryptoWalletItemArrayOutput() CryptoWalletItemArrayOutput {
	return o
}

func (o CryptoWalletItemArrayOutput) ToCryptoWalletItemArrayOutputWithContext(ctx context.Context) CryptoWalletItemArrayOutput {
	return o
}

func (o CryptoWalletItemArrayOutput) Index(i pulumi.IntInput) CryptoWalletItemOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *CryptoWalletItem {
		return vs[0].([]*CryptoWalletItem)[vs[1].(int)]
	}).(CryptoWalletItemOutput)
}

type CryptoWalletItemMapOutput struct{ *pulumi.OutputState }

func (CryptoWalletItemMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*CryptoWalletItem)(nil)).Elem()
}

func (o CryptoWalletItemMapOutput) ToCryptoWalletItemMapOutput() CryptoWalletItemMapOutput {
	return o
}

func (o CryptoWalletItemMapOutput) ToCryptoWalletItemMapOutputWithContext(ctx context.Context) CryptoWalletItemMapOutput {
	return o
}

func (o CryptoWalletItemMapOutput) MapIndex(k pulumi.StringInput) CryptoWalletItemOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *CryptoWalletItem {
		return vs[0].(map[string]*CryptoWalletItem)[vs[1].(string)]
	}).(CryptoWalletItemOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CryptoWalletItemInput)(nil)).Elem(), &CryptoWalletItem{})
	pulumi.RegisterInputType(reflect.TypeOf((*CryptoWalletItemArrayInput)(nil)).Elem(), CryptoWalletItemArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*CryptoWalletItemMapInput)(nil)).Elem(), CryptoWalletItemMap{})
	pulumi.RegisterOutputType(CryptoWalletItemOutput{})
	pulumi.RegisterOutputType(CryptoWalletItemGetAttachmentResultOutput{})
	pulumi.RegisterOutputType(CryptoWalletItemArrayOutput{})
	pulumi.RegisterOutputType(CryptoWalletItemMapOutput{})
}
