<template>
    <v-layout column class="ma-0 pa-2">
        <v-layout class="ma-0 py-2" align-center>
            <div class="font-weight-bold">Теги</div>
            <v-spacer></v-spacer>
            <v-btn @click="openItem(null)" class="text-none" text color="primary" rounded>Добавить</v-btn>
        </v-layout>
        <v-layout class="ma-0" align-center row>
            <v-chip @click="openItem(tag)" class="py-2 px-3 mx-1" :color="tag.color" small
                    v-for="(tag, index) in $store.state.items.tag.list" :key="index">
                <div class="white--text body-2">{{tag.title}}</div>
            </v-chip>
        </v-layout>

        <v-dialog max-width="300" v-model="dialog">
            <v-card class="" v-if="tag">
                <v-color-picker flat hide-inputs v-model="tag.color"></v-color-picker>
                <v-layout column class="ma-0 pa-2">
                    <v-text-field class="mx-3" outlined dense hide-details label="Наименование" v-model="tag.title"></v-text-field>
                    <v-layout class="ma-0 mt-3" align-center>
                        <v-btn @click="saveItem" class="text-none" color="primary" rounded text>Сохранить</v-btn>
                        <v-spacer></v-spacer>
                        <v-btn @click="deleteItem" v-if="tag.id" class="text-none" color="red" rounded text>Удалить</v-btn>
                    </v-layout>
                </v-layout>
            </v-card>
        </v-dialog>

    </v-layout>
</template>

<script>


    import {mapState} from "vuex";

    export default {
        name: 'Home',
        components: {},
        data: () => ({
            dialog: false,
            url: '/api/v1/tags/'
        }),
        created() {
            this.$store.dispatch('loadItem', {
                url: this.url,
                item: 'tag.list'
            }).then(res => console.log(res))
        },
        methods: {
            openItem(el) {
                if (el) {
                    this.$store.dispatch('loadItem', {
                        url: this.url,
                        item: 'tag.item',
                        id: el.id
                    }).then(() => {
                        this.dialog = true
                    })
                } else {
                    this.$store.state.items.tag.item = {...this.$store.state.items.tag.default}
                    this.dialog = true
                }
            },
            saveItem() {
                this.$store.dispatch(this.tag.id ? 'updateItem' : 'createItem', {
                    url: this.url,
                    value: this.tag
                }).then(data => {
                    if (this.tag.id) {
                        let index = this.$store.state.items.tag.list.findIndex(value => value.id === this.tag.id)
                        if (index > -1)
                            this.$store.state.items.tag.list.splice(index, 1, data)
                        this.dialog = false
                    } else {
                        this.$store.state.items.tag.list.push(data)
                        this.dialog = false
                    }
                })
            },
            deleteItem() {
                this.$store.dispatch('deleteItem', {
                    url: this.url,
                    id: this.tag.id
                }).then(() => {
                    let index = this.$store.state.items.tag.list.findIndex(value => value.id === this.tag.id)
                    if (index > -1)
                        this.$store.state.items.tag.list.splice(index, 1)
                    this.dialog = false

                })
            }
        },
        computed: {
            ...mapState({
                tag: state => state.items.tag.item
            })
        }
    }
</script>
