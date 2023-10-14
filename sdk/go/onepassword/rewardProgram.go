// Code generated by Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package onepassword

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi-onepassword/sdk/go/onepassword/rewardprogram"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type RewardProgram struct {
	pulumi.CustomResourceState

	Category        pulumi.StringOutput                    `pulumi:"category"`
	CompanyName     pulumi.StringPtrOutput                 `pulumi:"companyName"`
	Fields          GetFieldArrayOutput                    `pulumi:"fields"`
	Id              pulumi.StringOutput                    `pulumi:"id"`
	MemberId        pulumi.StringPtrOutput                 `pulumi:"memberId"`
	MemberName      pulumi.StringPtrOutput                 `pulumi:"memberName"`
	MoreInformation rewardprogram.MoreInformationPtrOutput `pulumi:"moreInformation"`
	Notes           pulumi.StringPtrOutput                 `pulumi:"notes"`
	Pin             pulumi.StringPtrOutput                 `pulumi:"pin"`
	Sections        GetSectionArrayOutput                  `pulumi:"sections"`
	// An array of strings of the tags assigned to the item.
	Tags pulumi.StringArrayOutput `pulumi:"tags"`
	// The title of the item.
	Title pulumi.StringOutput `pulumi:"title"`
	// The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
	Uuid pulumi.StringOutput `pulumi:"uuid"`
	// The UUID of the vault the item is in.
	Vault pulumi.StringOutput `pulumi:"vault"`
}

// NewRewardProgram registers a new resource with the given unique name, arguments, and options.
func NewRewardProgram(ctx *pulumi.Context,
	name string, args *RewardProgramArgs, opts ...pulumi.ResourceOption) (*RewardProgram, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Title == nil {
		return nil, errors.New("invalid value for required argument 'Title'")
	}
	if args.Vault == nil {
		return nil, errors.New("invalid value for required argument 'Vault'")
	}
	var resource RewardProgram
	err := ctx.RegisterResource("onepassword:index:RewardProgram", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRewardProgram gets an existing RewardProgram resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRewardProgram(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RewardProgramState, opts ...pulumi.ResourceOption) (*RewardProgram, error) {
	var resource RewardProgram
	err := ctx.ReadResource("onepassword:index:RewardProgram", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering RewardProgram resources.
type rewardProgramState struct {
}

type RewardProgramState struct {
}

func (RewardProgramState) ElementType() reflect.Type {
	return reflect.TypeOf((*rewardProgramState)(nil)).Elem()
}

type rewardProgramArgs struct {
	CompanyName     *string                        `pulumi:"companyName"`
	Fields          []Field                        `pulumi:"fields"`
	MemberId        *string                        `pulumi:"memberId"`
	MemberName      *string                        `pulumi:"memberName"`
	MoreInformation *rewardprogram.MoreInformation `pulumi:"moreInformation"`
	Notes           *string                        `pulumi:"notes"`
	Pin             *string                        `pulumi:"pin"`
	Sections        []Section                      `pulumi:"sections"`
	// An array of strings of the tags assigned to the item.
	Tags []string `pulumi:"tags"`
	// The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
	Title string `pulumi:"title"`
	// The UUID of the vault the item is in.
	Vault string `pulumi:"vault"`
}

// The set of arguments for constructing a RewardProgram resource.
type RewardProgramArgs struct {
	CompanyName     pulumi.StringPtrInput
	Fields          FieldArrayInput
	MemberId        pulumi.StringPtrInput
	MemberName      pulumi.StringPtrInput
	MoreInformation rewardprogram.MoreInformationPtrInput
	Notes           pulumi.StringPtrInput
	Pin             pulumi.StringPtrInput
	Sections        SectionArrayInput
	// An array of strings of the tags assigned to the item.
	Tags pulumi.StringArrayInput
	// The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
	Title pulumi.StringInput
	// The UUID of the vault the item is in.
	Vault pulumi.StringInput
}

func (RewardProgramArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*rewardProgramArgs)(nil)).Elem()
}

type RewardProgramInput interface {
	pulumi.Input

	ToRewardProgramOutput() RewardProgramOutput
	ToRewardProgramOutputWithContext(ctx context.Context) RewardProgramOutput
}

func (*RewardProgram) ElementType() reflect.Type {
	return reflect.TypeOf((**RewardProgram)(nil)).Elem()
}

func (i *RewardProgram) ToRewardProgramOutput() RewardProgramOutput {
	return i.ToRewardProgramOutputWithContext(context.Background())
}

func (i *RewardProgram) ToRewardProgramOutputWithContext(ctx context.Context) RewardProgramOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RewardProgramOutput)
}

// RewardProgramArrayInput is an input type that accepts RewardProgramArray and RewardProgramArrayOutput values.
// You can construct a concrete instance of `RewardProgramArrayInput` via:
//
//	RewardProgramArray{ RewardProgramArgs{...} }
type RewardProgramArrayInput interface {
	pulumi.Input

	ToRewardProgramArrayOutput() RewardProgramArrayOutput
	ToRewardProgramArrayOutputWithContext(context.Context) RewardProgramArrayOutput
}

type RewardProgramArray []RewardProgramInput

func (RewardProgramArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*RewardProgram)(nil)).Elem()
}

func (i RewardProgramArray) ToRewardProgramArrayOutput() RewardProgramArrayOutput {
	return i.ToRewardProgramArrayOutputWithContext(context.Background())
}

func (i RewardProgramArray) ToRewardProgramArrayOutputWithContext(ctx context.Context) RewardProgramArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RewardProgramArrayOutput)
}

// RewardProgramMapInput is an input type that accepts RewardProgramMap and RewardProgramMapOutput values.
// You can construct a concrete instance of `RewardProgramMapInput` via:
//
//	RewardProgramMap{ "key": RewardProgramArgs{...} }
type RewardProgramMapInput interface {
	pulumi.Input

	ToRewardProgramMapOutput() RewardProgramMapOutput
	ToRewardProgramMapOutputWithContext(context.Context) RewardProgramMapOutput
}

type RewardProgramMap map[string]RewardProgramInput

func (RewardProgramMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*RewardProgram)(nil)).Elem()
}

func (i RewardProgramMap) ToRewardProgramMapOutput() RewardProgramMapOutput {
	return i.ToRewardProgramMapOutputWithContext(context.Background())
}

func (i RewardProgramMap) ToRewardProgramMapOutputWithContext(ctx context.Context) RewardProgramMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RewardProgramMapOutput)
}

type RewardProgramOutput struct{ *pulumi.OutputState }

func (RewardProgramOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**RewardProgram)(nil)).Elem()
}

func (o RewardProgramOutput) ToRewardProgramOutput() RewardProgramOutput {
	return o
}

func (o RewardProgramOutput) ToRewardProgramOutputWithContext(ctx context.Context) RewardProgramOutput {
	return o
}

type RewardProgramArrayOutput struct{ *pulumi.OutputState }

func (RewardProgramArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*RewardProgram)(nil)).Elem()
}

func (o RewardProgramArrayOutput) ToRewardProgramArrayOutput() RewardProgramArrayOutput {
	return o
}

func (o RewardProgramArrayOutput) ToRewardProgramArrayOutputWithContext(ctx context.Context) RewardProgramArrayOutput {
	return o
}

func (o RewardProgramArrayOutput) Index(i pulumi.IntInput) RewardProgramOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *RewardProgram {
		return vs[0].([]*RewardProgram)[vs[1].(int)]
	}).(RewardProgramOutput)
}

type RewardProgramMapOutput struct{ *pulumi.OutputState }

func (RewardProgramMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*RewardProgram)(nil)).Elem()
}

func (o RewardProgramMapOutput) ToRewardProgramMapOutput() RewardProgramMapOutput {
	return o
}

func (o RewardProgramMapOutput) ToRewardProgramMapOutputWithContext(ctx context.Context) RewardProgramMapOutput {
	return o
}

func (o RewardProgramMapOutput) MapIndex(k pulumi.StringInput) RewardProgramOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *RewardProgram {
		return vs[0].(map[string]*RewardProgram)[vs[1].(string)]
	}).(RewardProgramOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*RewardProgramInput)(nil)).Elem(), &RewardProgram{})
	pulumi.RegisterInputType(reflect.TypeOf((*RewardProgramArrayInput)(nil)).Elem(), RewardProgramArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*RewardProgramMapInput)(nil)).Elem(), RewardProgramMap{})
	pulumi.RegisterOutputType(RewardProgramOutput{})
	pulumi.RegisterOutputType(RewardProgramArrayOutput{})
	pulumi.RegisterOutputType(RewardProgramMapOutput{})
}
