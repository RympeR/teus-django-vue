<template>
  <b-form @submit="goSave($event)">
    <div class="form__item">
      <span class="form__label">Текущий логин</span>
      {{changePassword.login}}
    </div>
    <div class="form__item">
      <span class="form__label">Текущий пароль</span>
      {{changePassword.password}}
    </div>
    <div class="form__item">
      <span class="form__label">Новый пароль</span>
      <div class="form__control">
        <b-form-input
          class="short"
          type="text"
          v-model="changePassword.new_password"
        />
      </div>
    </div>
    <div class="form__item">
      <span class="form__label">Подтвердите новый пароль</span>
      <div class="form__control">
        <b-form-input
          class="short"
          type="text"
          v-model="changePassword.password_confirm"
        />
      </div>
    </div>

    <div class="form__item form__item_submit">
      <div class="form__control">
        <b-button type="submit" variant="primary">Сохранить</b-button>
      </div>
    </div>
  </b-form>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'

export default {
  name: "UserForm",

  data() {
    return {
      id: null,
      changePassword: {
        login: null,
        password: null,
        new_password: null,
        password_confirm: null,
      },
      admin:{}
    };
  },
  created() {
    this.$store.state.breadcrumbs = [
      { text: "Главная", to: { name: "home" } },
      { text: "Изменить пароль", to: { name: "change-password" } },
    ];
    new Promise((resolve, reject) => {
            axios.get(`/api/user/admin/profile/`, {
              headers: {
                Authorization: 'tset'
              }
            })
                .then(response => {
                    console.log(response)
                    this.changePassword = response.data 
                    resolve(response.data)
                })
                .catch(response => {
                    reject(response.error);
                })
    })
  },
  methods: {

    goSave($event) {
      $event.preventDefault();
      let self = this;

      let formData = new FormData();
      let obj = this.changePassword;
      if (obj.new_password == obj.password_confirm) {
        Object.keys(obj).map(function(key) {
          if (obj[key]) formData.append(key, obj[key]);
        });
        console.log(obj)
        axios
          .put(
            "/api/user/change-password/",
            formData,
            {
              headers: {
                Authorization: "tset",
              },
            }
          )
          .then(function(response) {
            console.log(response)
            Vue.templateShowSuccess();
            self.changePassword = response.data
          })
          .catch(function(response) {
            console.log(response);
            Vue.templateShowError(response);
          });
      } else {
        alert('missed')
      }
    },
  },
};
</script>

<style scoped></style>
