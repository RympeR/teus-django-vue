<template>
  <b-row>
    <b-col>
      <div class="mb-4">
        <b-button
          :to="{ name: 'proposition-create' }"
          variant="primary"
          size="md"
        >
          Добавить
        </b-button>
      </div>
      <b-table-simple hover outlined responsive :fields="fields">
        <b-thead head-variant="light">
          <b-tr>
            <b-th v-for="field in fields" :key="field.key">
              <template v-if="field.key === 'user'">
                {{ field.label }}
                <input
                  v-model="filters[field.key]"
                  :placeholder="field.label"
                />
              </template>
              <template v-else-if="field.key === 'line'">
                {{ field.label }}
                <input
                  v-model="filters[field.key]"
                  :placeholder="field.label"
                />
              </template>
              <template v-else-if="field.key === 'city'">
                {{ field.label }}
                <input
                  v-model="filters[field.key]"
                  :placeholder="field.label"
                />
              </template>
              <template v-else-if="field.key === 'container'">
                {{ field.label }}
                <input
                  v-model="filters[field.key]"
                  :placeholder="field.label"
                />
              </template>
              <template v-else-if="field.key === 'amount'">
                {{ field.label }}
                <input
                  v-model="filters[field.key]"
                  :placeholder="field.label"
                />
              </template>
              <template v-else-if="field.key === 'date'">
                {{ field.label }}
                <input
                  v-model="filters[field.key]"
                  :placeholder="field.label"
                />
              </template>
              <template v-else-if="field.key === 'actions'"> </template>
              <template v-else>
                {{ field.label }}
              </template>
            </b-th>
          </b-tr>
        </b-thead>
        <b-tbody>
          <b-tr v-for="item in filtered" :key="item.id">
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
                <b-link
                  :to="{
                    name: 'line-update',
                    params: { id: item[field.key].id },
                  }"
                  >{{ item[field.key].name }}</b-link
                >
              </template>
              <template v-else-if="field.key === 'city'">
                <b-link
                  :to="{
                    name: 'city-update',
                    params: { id: item[field.key].id },
                  }"
                  >{{ item[field.key].name }}</b-link
                >
              </template>
              <template v-else-if="field.key === 'container'">
                <b-link
                  :to="{
                    name: 'container-update',
                    params: { id: item[field.key].id },
                  }"
                  >{{ item[field.key].name }}</b-link
                >
              </template>
              <template v-else-if="field.key === 'amount'">
                {{ item[field.key].amount }}
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

      <!-- <b-table hover outlined head-variant="light"
                :items="user_requests.list"
                :fields="fields"
                :filter="filter"
            >
            
                <template #cell(index)="data">
                    <b>{{ data.index + 1 }}</b>
                </template>
                <template v-slot:cell(actions)="data">
                    <div class="table__actions">
                        <b-button class="btn_edit" :to="{name: 'requests-update', params: {id: data.item.id}}"></b-button>
                        <b-button class="btn_delete" @click="deleteUserRequest(data.item.id)"/>
                    </div>
                </template>
            </b-table> -->
    </b-col>
  </b-row>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  name: "UserPropositiontList",
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
      filters: {
        id: "",
        user: "",
        line: "",
        city: "",
        container: "",
        amount: "",
        date: "",
      },
    };
  },
  computed: {
    ...mapState(["user_propositions"]),
    filtered() {
      const filtered = this.user_propositions.list.filter((item) => {
        return Object.keys(this.filters).every((key) =>
          String(item[key].filter).includes(this.filters[key])
        );
      });
      return filtered.length > 0
        ? filtered
        : [
            {
              id: "",
              user: "",
              line: "",
              city: "",
              container: "",
              amount: "",
              date: "",
            },
          ];
    },
  },
  created() {
    this.$store.state.breadcrumbs = [
      { text: "Главная", to: { name: "home" } },
      { text: "Заяки", to: { name: "proposition" } },
    ];

    this.getUserRequests().then((list) => {
      console.log(list);
    });
  },
  methods: {
    ...mapActions({
      saveUserRequest: "user_propositions/saveItem",
      deleteUserRequest: "user_propositions/deleteItem",
      getUserRequests: "user_propositions/getList",
    }),
  },
};
</script>

<style scoped></style>
