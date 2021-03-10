import axios from 'axios'
import store from '../store'

const $axios = axios.create({
    baseURL: process.env.VUE_APP_HOST
});

if (store.state.token) {
    $axios.defaults.headers.common['Authorization'] = `${store.state.token}`;
}

export default $axios