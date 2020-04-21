<template>
    <v-menu
        ref="menu"
        v-model="menu"
        offset-y
        :close-on-content-click="false"
        transition="scale-transition"
        nudge-bottom="10"
        max-width="290px"
        min-width="290px"
    >
        <template v-slot:activator="{ on }">
            <v-text-field
                v-model="dateFormatted"
                @change="onChange"
                :label="label"
                readonly
                :disabled="disabled"
                :dense="dense"
                :single-line="small"
                v-on="on"
                hide-details
                :outlined="outlined"
                :rules="required ? [rules.required] : []"
            ></v-text-field>
        </template>
        <v-date-picker locale="ru-RU" :value="value" no-title
                       @input="updateData" :max="maxDate"
                       :min="minDate || '1950-01-01'" />
    </v-menu>
</template>

<script>
    export default {
        props: {
            width: {
                type: String,
                default: '100%'
            },
            value: String,
            label: String,
            placeholder: String,
            outlined: {
                type: Boolean,
                default: false
            },
            disabled: {
                type: Boolean,
                default: false
            },
            height: {
                type: String,
                default: null
            },
            required: {
                type: Boolean,
                default: false
            },
            minDate: {
                type: String,
                default: undefined
            },
            maxDate: {
                type: String,
                default: undefined
            },
            readonly: {
                type: Boolean,
                default: false
            },
            small: {
                type: Boolean,
                default: false
            },
            dense: {
                type: Boolean,
                default: false
            },
            clearable: {
                type: Boolean,
                default: false
            },
            color: {
                type: String,
                default: undefined
            }
        },
        name: "DatePickerComponent",

        data () {
            return {
                menu: false,
                dateFormatted: null,
                rules: {
                    required: value => !!value || 'Поле обязательно для заполнения',
                }
            }
        },
        methods: {
            formatDate(date) {
                if (!date) return null;

                const [year, month, day] = date.split('-');
                return `${day}.${month}.${year}`
            },
            updateData (val) {
                this.menu = false;
                this.$emit('input', val);
                this.dateFormatted = this.formatDate(val)
            },
            onChange(val) {
                if (!val) return null;

                const [year, month, day] = val.split('-');
                this.updateData(`${day}-${month}-${year}`)

            },
        },
        watch: {
            value(val) {
                this.dateFormatted = this.formatDate(this.value)
            },
        },
        created () {
            this.dateFormatted = this.formatDate(this.value);
        }
    }
</script>

<style scoped>

</style>
