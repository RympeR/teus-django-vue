import axios from 'axios'

const $axios = axios.create({
    baseURL: process.env.VUE_APP_HOST
});

export default $axios