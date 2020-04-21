<template>
    <v-layout column class="ma-0 py-2">
        <v-layout class="ma-0 pa-2 mb-2" align-center>
            <v-select
                    class="ma-0 pa-0 mr-4"
                    clearable
                    style="max-width: 200px"
                    dense hide-details
                    v-model="$store.state.items.todo.tagFilter"
                    :items="$store.state.items.tag.list"
                    item-text="title"
                    item-value="id"
                    label="Теги"
                    outlined
            ></v-select>
            <v-text-field style="max-width: 300px" class="ma-0 pa-0" dense outlined hide-details label="Наименование"
                          v-model="search"></v-text-field>
            <v-spacer></v-spacer>
            <v-btn @click="openItem(null)" class="text-none" color="primary" rounded text>Добавить</v-btn>
        </v-layout>
        <v-layout column class="ma-0" v-for="(el, index) in $store.state.items.todo.list" :key="index">
            <v-divider class="my-2"></v-divider>
            <v-layout column class="ma-0">
                <v-layout class="ma-0 pa-1" justify-space-between>
                    <v-layout column class="ma-0">
                        <div @click="openItem(el)" class="font-weight-bold primary--text pl-2" style="cursor: pointer">
                            {{el.title}}
                        </div>
                        <v-layout class="ma-0" row>
                            <v-chip @click="$store.state.items.todo.tagFilter = tag.id" class="pa-2 ma-1"
                                    :color="tag.color"
                                    small v-for="(tag, index) in el.tags" :key="index">
                                <div class="white--text">{{tag.title}}</div>
                            </v-chip>
                        </v-layout>
                    </v-layout>
                    <div style="height: inherit">
                        <v-layout column align-end>
                            <v-layout class="ma-0" align-center justify-end>
                                <div class="mr-1 font-weight-bold body-2"
                                     :class="el.completed ? 'primary--text' : 'yellow--text text--darken-4'">{{
                                    el.completed ?
                                    'Выполнено' : 'Ожидает'}}
                                </div>
                                <v-checkbox @change="changeCompleted(el)" v-model="el.completed" hide-details
                                            class="ma-0 pa-0"></v-checkbox>
                            </v-layout>
                            <v-layout class="ma-0 pr-3 mt-1" align-center justify-end>
                                <div class="body-2">{{el.date}}</div>
                            </v-layout>
                        </v-layout>
                    </div>
                </v-layout>


            </v-layout>
        </v-layout>

        <v-dialog max-width="500" v-model="dialog">
            <v-card class="pa-2" v-if="todo">
                <v-text-field class="mt-3" dense outlined hide-details label="Наименование"
                              v-model="todo.title"></v-text-field>
                <v-textarea class="mt-4" dense outlined hide-details label="Описание"
                            v-model="todo.description"></v-textarea>
                <v-layout class="ma-0 mt-4">
                    <date-picker v-model="todo.date" outlined dense class="mt-4 pa-0" label="Дата"
                                 hide-details></date-picker>
                </v-layout>
                <v-select
                        dense hide-details class="mt-4"
                        v-model="todo.tags"
                        small-chips
                        :items="$store.state.items.tag.list"
                        chips
                        item-text="title"
                        item-value="id"
                        label="Теги"
                        return-object
                        multiple
                        outlined
                ></v-select>
                <v-layout class="ma-0" align-center>
                    <v-layout class="ma-0 mt-3" align-center>
                        <v-btn @click="saveItem" class="text-none" color="primary" rounded text>Сохранить</v-btn>
                        <v-spacer></v-spacer>
                        <v-btn @click="deleteItem" v-if="todo.id" class="text-none" color="red" rounded text>Удалить
                        </v-btn>
                    </v-layout>
                </v-layout>
            </v-card>
        </v-dialog>

    </v-layout>
</template>

<script>


    import {mapState} from "vuex";
    import DatePicker from "../components/DatePicker";

    export default {
        name: 'Home',
        components: {
            DatePicker
        },
        data: () => ({
            dialog: false,
            timeout: null,
            search: '',
            url: '/api/v1/todos/'
        }),
        created() {
            this.loadTodos()
        },
        methods: {
            loadTodos() {
                this.$store.dispatch('loadItem', {
                    url: this.url,
                    item: 'todo.list',
                    params: {
                        tagFilter: this.$store.state.items.todo.tagFilter,
                        search: this.search
                    }
                })
            },
            openItem(el) {
                if (el) {
                    this.$store.dispatch('loadItem', {
                        url: this.url,
                        item: 'todo.item',
                        id: el.id
                    }).then(() => {
                        this.dialog = true
                    })
                } else {
                    this.$store.state.items.todo.item = {...this.$store.state.items.todo.default}
                    this.dialog = true
                }
            },
            saveItem() {
                let value = {...this.todo}
                if (!value.description) value.description = null
                this.$store.dispatch(this.todo.id ? 'updateItem' : 'createItem', {
                    url: this.url,
                    value: value
                }).then(data => {
                    this.loadTodos()
                    this.dialog = false
                })
            },
            deleteItem() {
                this.$store.dispatch('deleteItem', {
                    url: this.url,
                    id: this.todo.id
                }).then(() => {
                    this.loadTodos()
                    this.dialog = false
                })
            },
            changeCompleted(el) {
                this.$store.dispatch('executeAction', {
                    url: this.url,
                    id: el.id,
                    action: 'change_completed'
                })
            }
        },
        computed: {
            ...mapState({
                todo: state => state.items.todo.item
            })
        },
        watch: {
            '$store.state.items.todo.tagFilter'() {
                this.loadTodos()
            },
            search() {
                if (this.timeout)
                    clearTimeout(this.timeout)
                setTimeout(() => {
                    this.loadTodos()
                }, 100)
            }
        }
    }
</script>
