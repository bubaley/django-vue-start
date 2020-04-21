import Vue from 'vue'
import VueRouter from 'vue-router'
import Register from "../views/auth/Register";
import Login from "../views/auth/Login";
import Home from "../views/Home";
import User from "../views/User";

Vue.use(VueRouter)

const routes = [
    {
        path: '/register',
        name: 'register',
        component: Register
    },
    {
        path: '/login',
        name: 'login',
        component: Login
    },
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/profile',
      name: 'profile',
      component: User
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
