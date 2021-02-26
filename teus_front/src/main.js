import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import store from './store'
import {BootstrapVue, BootstrapVueIcons} from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import CKEditor from '@ckeditor/ckeditor5-vue';
import VuePlyr from 'vue-plyr'
import wysiwyg from "vue-wysiwyg";

Vue.use(wysiwyg, {}); // config is optional. more below

// import { VueReCaptcha } from "vue-recaptcha-v3";
// Vue.use(VueReCaptcha, { siteKey: "6LfElv4ZAAAAABvyLHoYldVbc-588RAvG-yWAhhG" });
Vue.use(VuePlyr);
Vue.use( CKEditor );

import BtnTurn from "@/components/BtnTurn";
import TableThumbnail from "@/components/TableThumbnail";
Vue.component("btn-turn", BtnTurn);
Vue.component("table-thumbnail", TableThumbnail);

import CustomMixin from '@/mixins/CustomMixin'

Vue.mixin(CustomMixin);

Vue.prototype.$axios = axios.create({
  baseURL: process.env.VUE_APP_BASE_API
});

Vue.config.productionTip = false;
Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);

const moment = require('moment-timezone');
require('moment/locale/ru');
Vue.use(require('vue-moment'), {
  moment
});

Vue.prototype.$log = console.log.bind(console);

router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth) {
    if (store.state.token) {
      next();
    }else {
      next({'name': 'login'})
    }
  }else{
    next()
  }
  //next()
});

new Vue({
  store,
  router,
  render: h => h(App),
}).$mount('#app');
