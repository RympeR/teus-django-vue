<template>
  <b-form @submit="goSave">
    <b-tabs content-class="mt-3">
      <b-tab title="Основное" active>
        <div class="form__item">
          <span class="form__label">Линия</span>
          <div class="form__control">
            <div class="row">
              <div class="col-6">
                <b-form-select
                  v-model="user_requests.item.line.id"
                  :options="lines.list"
                  class="mb-3"
                  value-field="id"
                  text-field="name"
                  disabled-field="notEnabled"
                ></b-form-select>
              </div>
            </div>
          </div>
        </div>
        <div class="form__item">
          <span class="form__label">Пользователь</span>
          <div class="form__control">
            <div class="row">
              <div class="col-6">
                <b-link
                  :to="{
                    name: 'student-update',
                    params: { id: user_requests.item.user.id },
                  }"
                  >{{ user_requests.item.user.name }},
                  {{ user_requests.item.user.phone }}</b-link
                >
              </div>
            </div>
          </div>
        </div>
        <div class="form__item">
          <span class="form__label">Город</span>
          <div class="form__control">
            <div class="row">
              
              <div class="col-6">
                {{city_names}}
              </div>
            </div>
          </div>
        </div>
        <div class="form__item">
          <span class="form__label">Контейнер</span>
          <div class="form__control">
            <div class="row">
              <div class="col-6">
                <b-form-select
                  v-model="user_requests.item.container.id"
                  :options="containers.list"
                  class="mb-3"
                  value-field="id"
                  text-field="name"
                  disabled-field="notEnabled"
                ></b-form-select>
              </div>
            </div>
          </div>
        </div>
        <div class="form__item">
          <span class="form__label">Количество</span>
          <div class="form__control">
            <div class="row">
              <div class="col-12">
                <b-form-input
                  class="short"
                  type="text"
                  required
                  placeholder="ru"
                  v-model="user_requests.item.amount"
                />
              </div>
            </div>
          </div>
        </div>
        <div class="form__item">
          <span class="form__label">Статус</span>
          <div class="form__control">
            <div class="row">
              <div class="col-12">
                {{user_requests.item.status}}
              </div>
            </div>
          </div>
        </div>
        <div class="form__item">
          <span class="form__label">Дата запроса</span>
          <div class="form__control">
            <div class="row">
              <div class="col-6">
                <b-form-datepicker
                  locale="ru"
                  :dateFormatOptions="{
                    day: 'numeric',
                    month: 'short',
                    year: 'numeric',
                  }"
                  size="sm"
                  v-model="user_requests.item.request_date"
                  class="mb-2"
                ></b-form-datepicker>
              </div>
            </div>
          </div>
        </div>
        <div class="form__item">
          <span class="form__label">Дата конца</span>
          <div class="form__control">
            <div class="row">
              <div class="col-6">
                <b-form-datepicker
                  locale="ru"
                  :dateFormatOptions="{
                    day: 'numeric',
                    month: 'short',
                    year: 'numeric',
                  }"
                  size="sm"
                  v-model="user_requests.item.end_date"
                  class="mb-2"
                ></b-form-datepicker>
              </div>
            </div>
          </div>
        </div>
      </b-tab>
    </b-tabs>
    <div class="form__item form__item_submit">
      <div class="form__control">
        <b-button type="submit" variant="primary">Сохранить</b-button>
      </div>
    </div>
  </b-form>
</template>

<script>
import { mapState, mapActions } from "vuex";
import Vue from "vue";

export default {
  name: "UserRequestForm",
  components: {},
  data() {
    return {
      id: this.$route.params.id,
      alert: false,
      city_names: [],
    };
  },
  computed: {
    ...mapState(["user_requests", "lines", "containers", "users", "cities"]),
  },
  created() {
    if (this.id) {
      this.$store.state.breadcrumbs = [
        { text: "Главная", to: { name: "home" } },
        { text: "Запрос", to: { name: "requests" } },
        {
          text: "Редактировать",
          to: { name: "requests-update", params: { id: this.id } },
        },
      ];
    } else {
      this.$store.state.breadcrumbs = [
        { text: "Главная", to: { name: "home" } },
        { text: "Запрос", to: { name: "requests" } },
        { text: "Создать", to: { name: "requests-create" } },
      ];
    }
    if (this.$route.params.id) {
      this.$store
        .dispatch("user_requests/getItem", this.$route.params.id)
        .then((item) => {
          console.log(item);
        })
        .catch((error) => {
          console.log(error);
        });
    }
    this.user_requests.item.city.forEach(el => {
      this.city_names.push(el.name)
    });
    this.city_names = this.city_names.join(', ')
    this.getLines().then((list) => {
      console.log(list);
    });
    this.getContainers().then((list) => {
      console.log(list);
    });
    // this.getUsers().then((list) => {
    //     console.log(list);
    // });
    this.getCities().then((list) => {
      console.log(list);
    });
    this.$store
      .dispatch("users/getList")
      .then((item) => {
        console.log(item);
      })
      .catch((error) => {
        console.log(error);
      });
  },
  methods: {
    ...mapActions({
      getLines: "lines/getList",
      getContainers: "containers/getList",
      getUsers: "users/getList",
      getCities: "cities/getList",
    }),
    goSave(e) {
      e.preventDefault();
      let data = Object.assign({}, this.user_requests.item);
      data.id = this.id;
      console.log(data);
      this.$store
        .dispatch("user_requests/saveItem", data)
        .then((item) => {
          console.log(item);
          Vue.templateShowSuccess();
          if (!data.id) Vue.goBack();
          else
            this.$store
              .dispatch("user_requests/getItem", this.$route.params.id)
              .then((item) => {
                console.log(item);
              })
              .catch((error) => {
                console.log(error);
              });
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped></style>
