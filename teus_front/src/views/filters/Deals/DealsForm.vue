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
                  v-model="deals.item.line.id"
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
          <span class="form__label">Пользователь запрос</span>
          <div class="form__control">
            <div class="row">
              <div class="col-6">
                <b-link
                  :to="{
                    name: 'student-update',
                    params: { id: deals.item.first_user.id },
                  }"
                  >{{ deals.item.first_user.name }},
                  {{ deals.item.first_user.phone }}</b-link
                >
              </div>
            </div>
          </div>
        </div>
        <div class="form__item">
          <span class="form__label">Пользователь предложение</span>
          <div class="form__control">
            <div class="row">
              <div class="col-6">
                <b-link
                  :to="{
                    name: 'student-update',
                    params: { id: deals.item.sec_user.id },
                  }"
                  >{{ deals.item.sec_user.name }},
                  {{ deals.item.sec_user.phone }}</b-link
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
                  v-model="deals.item.city.id"
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
                  v-model="deals.item.container.id"
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
                  v-model="deals.item.amount"
                />
              </div>
            </div>
          </div>
        </div>
        <div class="form__item">
          <span class="form__label">Дата время рукопожатия</span>
          <div class="form__control">
            <div class="row">
              <div class="col-6">
                {{ deals.item.handshake.handshake }}
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
  name: "DealsForm",
  components: {},
  data() {
    return {
      id: this.$route.params.id,
      alert: false,
      options: {
        format: "DD/MM/YYYY",
        useCurrent: false,
      },
    };
  },
  computed: {
    ...mapState(["deals", "lines", "containers", "users", "cities"]),
  },
  created() {
    if (this.id) {
      this.$store.state.breadcrumbs = [
        { text: "Главная", to: { name: "home" } },
        { text: "Сделка", to: { name: "deals" } },
        {
          text: "Редактировать",
          to: { name: "deals-update", params: { id: this.id } },
        },
      ];
    } else {
      this.$store.state.breadcrumbs = [
        { text: "Главная", to: { name: "home" } },
        { text: "Сделка", to: { name: "deals" } },
        { text: "Создать", to: { name: "deals-create" } },
      ];
    }
    if (this.$route.params.id) {
      this.$store
        .dispatch("deals/getItem", this.$route.params.id)
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
      let data = Object.assign({}, this.deals.item);
      data.id = this.id;
      this.$store
        .dispatch("deals/saveItem", data)
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
