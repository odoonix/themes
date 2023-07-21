/** @odoo-module **/
import { Component } from "@odoo/owl";

export class AppsBar extends Component {}

Object.assign(AppsBar, {
    template: 'trip2persia_theme_backend.AppsBar',
    props: {
    	apps: Array,
    },
});

