<template>
  <b-row>
    <b-col>
      <div class="mb-4">
        <b-button @cick="resetFilters" variant="primary" size="md">
          Очистить фильтры
        </b-button>
      </div>
      <b-table-simple
        :per-page="perPage"
        :current-page="currentPage"
        hover
        outlined
        responsive
        :fields="fields"
      >
        <b-thead head-variant="light">
          <b-tr>
            <b-th v-for="field in fields" :key="field.key">
              <template v-if="field.key === 'user'">
                {{ field.label }}
                <input
                  :placeholder="field.label"
                  @input="getFilteredRequests(search)"
                  v-model="search.user_name"
                />
              </template>
              <template v-else-if="field.key === 'line'">
                {{ field.label }}
                <input
                  :placeholder="field.label"
                  @input="getFilteredRequests(search)"
                  v-model="search.line_name"
                />
              </template>
              <template v-else-if="field.key === 'city'">
                {{ field.label }}
                <input
                  v-model="search.city_name"
                  @input="getFilteredRequests(search)"
                  :placeholder="field.label"
                />
              </template>
              <template v-else-if="field.key === 'container'">
                {{ field.label }}
                <input
                  v-model="search.container_name"
                  @input="getFilteredRequests(search)"
                  :placeholder="field.label"
                />
              </template>
              <template v-else-if="field.key === 'amount'">
                {{ field.label }}
                <input
                  v-model="search.amount"
                  @input="getFilteredRequests(search)"
                  :placeholder="field.label"
                />
              </template>
              <template v-else-if="field.key === 'date'">
                {{ field.label }}
                <b-form-datepicker
                  locale="ru"
                  placeholder="от"
                  :dateFormatOptions="{
                    day: 'numeric',
                    month: 'short',
                    year: 'numeric',
                  }"
                  @input="getFilteredRequests(search)"
                  size="sm"
                  v-model="search.request_date"
                  class="mb-2"
                ></b-form-datepicker>
              </template>
              <template v-else-if="field.key === 'actions'"> </template>
              <template v-else>
                {{ field.label }}
              </template>
            </b-th>
          </b-tr>
        </b-thead>
        <b-tbody>
          <b-tr v-for="item in lists" :key="item.id">
            <b-td v-for="field in fields" :key="field.key">
              <template v-if="field.key === 'user'">
                <b-link
                  :to="{
                    name: 'student-update',
                    params: { id: item[field.key].id },
                  }"
                  >{{ item[field.key].phone }}</b-link
                >
              </template>
              <template v-else-if="field.key === 'line'">
                {{ item[field.key].name }}
              </template>
              <template v-else-if="field.key === 'city'">
                {{ item[field.key].name }}
              </template>
              <template v-else-if="field.key === 'container'">
                {{ item[field.key].name }}
              </template>
              <template v-else-if="field.key === 'amount'">
                {{ item.amount.amount }}
              </template>
              <template v-else-if="field.key === 'date'">
                {{ item[field.key].date }}
              </template>
              <template v-else-if="field.key === 'actions'">
                <div class="table__actions">
                  <b-button
                    class="btn_edit"
                    :to="{ name: 'requests-update', params: { id: item.id } }"
                  ></b-button>
                  <b-button
                    class="btn_delete"
                    @click="deleteUserRequest(item.id)"
                  />
                </div>
              </template>
              <template v-else>
                {{ item[field.key] }}
              </template>
            </b-td>
          </b-tr>
        </b-tbody>
      </b-table-simple>
      <b-pagination
        v-model="currentPage"
        :total-rows="rows"
        :per-page="perPage"
        first-text="First"
        prev-text="Prev"
        next-text="Next"
        last-text="Last"
        aria-controls="item-table"
      ></b-pagination>
    </b-col>
  </b-row>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  name: "UserRequestsList",
  data() {
    return {
      fields: [
        { key: "index", label: "#" },
        { key: "id", label: "ID" },
        { key: "user", label: "Пользователь" },
        { key: "line", label: "Линия" },
        { key: "city", label: "Город" },
        { key: "container", label: "Контейнер" },
        { key: "amount", label: "Кол-во" },
        { key: "date", label: "Дата" },

        { key: "actions", label: "" },
      ],
      activePage: 1,
      search: {
        user_name: "",
        line_name: "",
        city_name: "",
        container_name: "",
        amount: "",
        request_date: "",
      },
      perPage: 1,
      currentPage: 1,
    };
  },
  computed: {
    ...mapState(["user_requests"]),
    rows() {
      return this.user_requests.list.length;
    },
    lists() {
      const items = this.user_requests.list;
      return items.slice(
        (this.currentPage - 1) * this.perPage,
        this.currentPage * this.perPage
      );
    },
  },

  created() {
    this.$store.state.breadcrumbs = [
      { text: "Главная", to: { name: "home" } },
      { text: "Запросы", to: { name: "requests" } },
    ];

    this.getUserRequests().then((list) => {
      console.log(list);
    });
  },
  methods: {
    ...mapActions({
      saveUserRequest: "user_requests/saveItem",
      deleteUserRequest: "user_requests/deleteItem",
      getUserRequests: "user_requests/getList",
      getFilteredRequests: "user_requests/getFilteredItems",
    }),
	resetFilters(){

	},
  },
};
</script>

<style scoped></style>
