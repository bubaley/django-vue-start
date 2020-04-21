<template>
    <v-app>
        <v-app-bar
                app
                color="primary"
                dark
        >
            <div style="cursor: pointer" @click="$router.push({name: 'home'}).catch(() => {})" class="font-weight-bold pa-2">TODO</div>
            <v-spacer></v-spacer>
            <v-btn dark
                   icon
                   v-if="$store.getters.currentUser"
                   class="mr-2" @click="$router.push({name: 'profile'}).catch(() => {})">
                <v-icon>mdi-account</v-icon>
            </v-btn>
        </v-app-bar>

        <v-content>
            <router-view></router-view>
        </v-content>

        <v-snackbar
                v-model="$store.getters.snackbar.value"
                top
                right
                :color="$store.getters.snackbar.color"
                multi-line
                :timeout="4000"
        >
            {{ $store.getters.snackbar.text }}
            <v-btn
                    small
                    icon
                    dark
                    @click="$store.getters.snackbar.value = false"
            >
                <v-icon>mdi-close</v-icon>
            </v-btn>
        </v-snackbar>
    </v-app>
</template>

<script>
    export default {
        name: 'App',

        data: () => ({}),
        created() {
            this.$store.dispatch('getUser').then(() => {
                this.$store.dispatch('loadItem', {
                    url: '/api/v1/tags/',
                    item: 'tag.list'
                })
            }).catch(() => {
                this.$router.push({
                    name: 'login'
                }).catch(e => {
                })
            })
        },
        methods: {}
    };
</script>
