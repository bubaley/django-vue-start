<template>
    <v-layout class="ma-0" v-if="currentUser">
        <v-flex xs10 offset-xs1 md6 offset-md3 class="py-5">
            <v-card class="pa-3">
                <v-layout class="ma-0" align-center>
                    <div>Почта</div>
                    <div class="pl-2 font-weight-bold">{{currentUser.email}}</div>
                </v-layout>
                <v-layout class="ma-0" align-center>
                    <div>Имя пользователя</div>
                    <div class="pl-2 font-weight-bold">{{currentUser.username}}</div>
                </v-layout>
                <v-btn class="mt-3 text-none" color="primary" v-if="$store.getters.currentUser" @click="logout">Выйти</v-btn>
            </v-card>
            <tags></tags>
        </v-flex>
    </v-layout>
</template>

<script>
    import {mapGetters} from "vuex";
    import Tags from "./Tags";

    export default {
        name: "User",
        components: {
            Tags
        },
        computed: {
            ...mapGetters([
                'currentUser'
            ])
        },
        methods: {
            logout() {
                this.$store.dispatch('logout').then(() => {
                    this.$router.push({
                        name: 'login'
                    }).catch(e => {})
                })

            }
        }
    }
</script>

<style scoped>

</style>