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
                  v-model="user_propositions.item.line.id"
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
                    params: { id: user_propositions.item.user.id },
                  }"
                  >{{ user_propositions.item.user.name }},
                  {{ user_propositions.item.user.phone }}</b-link
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
                <b-form-select
                  v-model="user_propositions.item.city.id"
                  :options="cities.list"
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
          <span class="form__label">Контейнер</span>
          <div class="form__control">
            <div class="row">
              <div class="col-6">
                <b-form-select
                  v-model="user_propositions.item.container.id"
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
                  v-model="user_propositions.item.amount"
                />
              </div>
            </div>
          </div>
        </div>
        <div class="form__item">
          <span class="form__label">Дата начала</span>
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
                  v-model="user_propositions.item.start_date"
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

export default {
  name: "UserPropositionForm",
  components: {},
  data() {
    return {
      id: this.$route.params.id,
      alert: false,
    };
  },
  computed: {
    ...mapState([
      "user_propositions",
      "lines",
      "containers",
      "users",
      "cities",
    ]),
  },
  created() {
    if (this.id) {
      this.$store.state.breadcrumbs = [
        { text: "Главная", to: { name: "home" } },
        { text: "Предложения", to: { name: "propositions" } },
        {
          text: "Редактировать",
          to: { name: "propositions-update", params: { id: this.id } },
        },
      ];
    } else {
      this.$store.state.breadcrumbs = [
        { text: "Главная", to: { name: "home" } },
        { text: "Предложения", to: { name: "propositions" } },
        { text: "Создать", to: { name: "propositions-create" } },
      ];
    }
    if (this.$route.params.id) {
      this.$store
        .dispatch("user_propositions/getItem", this.$route.params.id)
        .then((item) => {
          console.log(item);
        })
        .catch((error) => {
          console.log(error);
        });
    }
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
      let data = Object.assign({}, this.user_propositions.item);
      data.id = this.id;
      this.$store
        .dispatch("user_propositions/saveItem", data)
        .then((item) => {
          console.log(item);
          this.templateShowSuccess();
          this.goBack();
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped></style>
