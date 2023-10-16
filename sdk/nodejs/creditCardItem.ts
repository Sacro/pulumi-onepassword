// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "./types";
import * as utilities from "./utilities";

export class CreditCardItem extends pulumi.CustomResource {
    /**
     * Get an existing CreditCardItem resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CreditCardItemState, opts?: pulumi.CustomResourceOptions): CreditCardItem {
        return new CreditCardItem(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'onepassword:index:CreditCardItem';

    /**
     * Returns true if the given object is an instance of CreditCardItem.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CreditCardItem {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CreditCardItem.__pulumiType;
    }

    public readonly additionalDetails!: pulumi.Output<outputs.creditCard.AdditionalDetailsSection | undefined>;
    public readonly cardholderName!: pulumi.Output<string | undefined>;
    public readonly category!: pulumi.Output<enums.Category | string>;
    public readonly contactInformation!: pulumi.Output<outputs.creditCard.ContactInformationSection | undefined>;
    public readonly expiryDate!: pulumi.Output<string | undefined>;
    public readonly fields!: pulumi.Output<{[key: string]: outputs.GetField} | undefined>;
    public readonly notes!: pulumi.Output<string | undefined>;
    public readonly number!: pulumi.Output<string | undefined>;
    public readonly sections!: pulumi.Output<{[key: string]: outputs.GetSection} | undefined>;
    /**
     * An array of strings of the tags assigned to the item.
     */
    public readonly tags!: pulumi.Output<string[]>;
    /**
     * The title of the item.
     */
    public readonly title!: pulumi.Output<string>;
    public readonly type!: pulumi.Output<string | undefined>;
    /**
     * The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
     */
    public /*out*/ readonly uuid!: pulumi.Output<string>;
    public readonly validFrom!: pulumi.Output<string | undefined>;
    /**
     * The UUID of the vault the item is in.
     */
    public readonly vault!: pulumi.Output<string>;
    public readonly verificationNumber!: pulumi.Output<string | undefined>;

    /**
     * Create a CreditCardItem resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CreditCardItemArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: CreditCardItemArgs | CreditCardItemState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as CreditCardItemState | undefined;
            resourceInputs["vault"] = state ? state.vault : undefined;
        } else {
            const args = argsOrState as CreditCardItemArgs | undefined;
            if ((!args || args.vault === undefined) && !opts.urn) {
                throw new Error("Missing required property 'vault'");
            }
            resourceInputs["additionalDetails"] = args ? args.additionalDetails : undefined;
            resourceInputs["cardholderName"] = args ? args.cardholderName : undefined;
            resourceInputs["category"] = "Credit Card";
            resourceInputs["contactInformation"] = args ? args.contactInformation : undefined;
            resourceInputs["expiryDate"] = args ? args.expiryDate : undefined;
            resourceInputs["fields"] = args ? args.fields : undefined;
            resourceInputs["notes"] = args ? args.notes : undefined;
            resourceInputs["number"] = args ? args.number : undefined;
            resourceInputs["sections"] = args ? args.sections : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["title"] = args ? args.title : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
            resourceInputs["validFrom"] = args ? args.validFrom : undefined;
            resourceInputs["vault"] = args ? args.vault : undefined;
            resourceInputs["verificationNumber"] = args ? args.verificationNumber : undefined;
            resourceInputs["uuid"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["fields", "sections"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(CreditCardItem.__pulumiType, name, resourceInputs, opts);
    }
}

export interface CreditCardItemState {
    /**
     * The UUID of the vault the item is in.
     */
    vault: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a CreditCardItem resource.
 */
export interface CreditCardItemArgs {
    additionalDetails?: pulumi.Input<inputs.creditCard.AdditionalDetailsSectionArgs>;
    cardholderName?: pulumi.Input<string>;
    /**
     * The category of the vault the item is in.
     */
    category?: pulumi.Input<"Credit Card">;
    contactInformation?: pulumi.Input<inputs.creditCard.ContactInformationSectionArgs>;
    expiryDate?: pulumi.Input<string>;
    fields?: pulumi.Input<{[key: string]: pulumi.Input<inputs.FieldArgs>}>;
    notes?: pulumi.Input<string>;
    number?: pulumi.Input<string>;
    sections?: pulumi.Input<{[key: string]: pulumi.Input<inputs.SectionArgs>}>;
    /**
     * An array of strings of the tags assigned to the item.
     */
    tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
     */
    title?: pulumi.Input<string>;
    type?: pulumi.Input<string>;
    validFrom?: pulumi.Input<string>;
    /**
     * The UUID of the vault the item is in.
     */
    vault: pulumi.Input<string>;
    verificationNumber?: pulumi.Input<string>;
}
