// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "./types";
import * as utilities from "./utilities";

export function getSocialSecurityNumber(args: GetSocialSecurityNumberArgs, opts?: pulumi.InvokeOptions): Promise<GetSocialSecurityNumberResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("onepassword:index:GetSocialSecurityNumber", {
        "title": args.title,
        "uuid": args.uuid,
        "vault": args.vault,
    }, opts);
}

export interface GetSocialSecurityNumberArgs {
    /**
     * The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
     */
    title?: string;
    /**
     * The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
     */
    uuid?: string;
    /**
     * The UUID of the vault the item is in.
     */
    vault: string;
}

export interface GetSocialSecurityNumberResult {
    readonly category?: enums.Category | string;
    readonly fields?: outputs.GetField[];
    readonly id?: string;
    readonly name?: string;
    readonly notes?: string;
    readonly number?: string;
    readonly sections?: outputs.GetSection[];
    /**
     * An array of strings of the tags assigned to the item.
     */
    readonly tags?: string[];
    /**
     * The title of the item.
     */
    readonly title?: string;
    /**
     * The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
     */
    readonly uuid?: string;
    /**
     * The UUID of the vault the item is in.
     */
    readonly vault?: string;
}

export function getSocialSecurityNumberOutput(args: GetSocialSecurityNumberOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetSocialSecurityNumberResult> {
    return pulumi.output(args).apply(a => getSocialSecurityNumber(a, opts))
}

export interface GetSocialSecurityNumberOutputArgs {
    /**
     * The title of the item to retrieve. This field will be populated with the title of the item if the item it looked up by its UUID.
     */
    title?: pulumi.Input<string>;
    /**
     * The UUID of the item to retrieve. This field will be populated with the UUID of the item if the item it looked up by its title.
     */
    uuid?: pulumi.Input<string>;
    /**
     * The UUID of the vault the item is in.
     */
    vault: pulumi.Input<string>;
}
