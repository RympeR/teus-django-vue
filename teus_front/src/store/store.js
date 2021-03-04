import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import lines from './modules/lines'
import cities from './modules/cities'
import containers from './modules/containers'
import users from './modules/users'
import user_propositions from './modules/user_propositions'
import user_requests from './modules/user_requests'
import deals from './modules/deals'

Vue.use(Vuex);

export default new Vuex.Store({
    // namespaced: true,
    state: {
        status: '',
        token: localStorage.getItem('token') || null,
        profile: null,
        breadcrumbs: [
            {text: 'Главная', to: {name: 'home'}},
        ]
    },
    mutations: {
        auth_request(state) {
            state.status = 'loading'
        },
        auth_success(state, token) {
            state.status = 'success';
            state.token = token
        },
        auth_error(state) {
            state.status = 'error'
        },
        logout(state) {
            state.status = '';
            state.token = ''
        },
    },
    actions: {
        login({commit}, user){
            console.log(user)
            return new Promise((resolve, reject) => {
                commit('auth_request');
                axios.post('http://edunav-back.maximustest.ru/ru/api/user/admin-login/', {
                    email: user.email,
                    password: user.password
                })
                .then(response => {
                    console.log(response);
                    const token = response.data.auth_token;
                    localStorage.setItem('token', token);
                    commit('auth_success', token);
                    // axios.defaults.headers.common['Authorization'] = token
                    resolve(response)
                })
                .catch(response => {
                    console.log(response);
                    commit('auth_error');
                    localStorage.removeItem('token');
                    reject(response)
                })
            })
        },
        logout({commit}){
            return new Promise((resolve, reject) => {
                commit('logout');
                localStorage.removeItem('token');
                // delete axios.defaults.headers.common['Authorization']
                resolve();
                console.log(reject)
            })
        },
        token(){
            return new Promise((resolve) => {
                resolve('Token ' + this.state.token)
            })
        }
    },
    getters: {
        isLoggedIn: state => !!state.token,
        authStatus: state => state.status,
    },
    modules: {
        lines,
        cities,
        containers,
        users,
        user_propositions,
        user_requests,
        deals,
    }
})