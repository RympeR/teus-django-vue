<template>
    <b-row>
        <b-col>
            <div class="mb-4">
				<b-button
					@click="resetFilters"
					variant="warning"
					v-show="filtered"
					size="md"
				>
					Очистить фильтры
				</b-button>
			</div>
            <b-table-simple
				hover
				outlined
				responsive
				:fields="fields"
			>
				<b-thead head-variant="light">
					<b-tr>
						<b-th v-for="field in fields" :key="field.key">
							<template v-if="field.key === 'phone'">
								<div class="stick-top">
									{{ field.label }}
									<input
										class="input"
										:placeholder="field.label"
										@input="getFilteredItems(search)"
										v-model="search.phone"
									/>
								</div>
							</template>
							<template v-else-if="field.key === 'last_name'">
								{{ field.label }}
								<input
									class="input"
									:placeholder="field.label"
									@input="getFilteredItems(search)"
									v-model="search.last_name"
									list="last_name-list"
								/>
								<b-form-datalist
									id="last_name-list"
									:options="search_existing_list.last_name"
								></b-form-datalist>

							</template>
							<template v-else-if="field.key === 'first_name'">
								<div class="stick-top">{{ field.label }}</div>
								<input
									class="input"
									:placeholder="field.label"
									@input="getFilteredItems(search)"
									v-model="search.first_name"
									list="line-list"
								/>
								<b-form-datalist
									id="line-list"
									:options="search_existing_list.first_name"
								>
								</b-form-datalist>
							</template>
							
							<template v-else-if="field.key === 'actions'">
							</template>
							<template v-else>
								{{ field.label }}
							</template>
						</b-th>
					</b-tr>
				</b-thead>
				<b-tbody>
					<b-tr v-for="item in users.list" :key="item.id">
						<b-td v-for="field in fields" :key="field.key">
							<template v-if="field.key === 'image'">
                                <template>
                                    <table-thumbnail v-if="item[field.key]"
										:id="item.id"
                                        :src="item[field.key]"
                                    />
                                </template>
							</template>
							<template v-else-if="field.key === 'actions'">
								<div class="table__actions">
									<b-button
										class="btn_edit"
										:to="{
											name: 'student-update',
											params: { id: item.id },
										}"
									></b-button>
									<b-button
										class="btn_delete"
										@click="deleteItem(item.id)"
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
        </b-col>

    </b-row>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
    name: "UserList",
    computed: {
        ...mapState(['users']),
    },
    methods: {
        ...mapActions('users', ['saveItem', 'deleteItem', 'getList', 'getFilteredItems']),
        resetFilters() {
			this.filtered = false;
			this.search= {
				first_name: "",
				last_name: "",
				phone: "",
			},
			this.getList().then(list => {
                console.log(list)
            })
		},
    },
    data () {
        return {
            fields: [
                { key: 'id', label: 'ID', sortable: true},
                { key: 'phone', label: 'Телефон', sortable: true},
                { key: 'last_name', label: 'Фамилия', sortable: true},
                { key: 'first_name', label: 'Имя'},
                { key: 'image', label: 'Аватар'},
                { key: 'actions', label: ''},
            ],
            filtered: false,
            activePage: 1,
            filter: {
                organisation: null
            },
            search: {
				first_name: "",
				last_name: "",
				phone: "",
			},
            search_existing_list:{
				first_name:[],
				last_name: [],
				phone: [],
			}
        }
    },
    watch: {
		search: {
			handler: function(a, b) {
				console.log(a + " " + b);
				for (let key in this.search) {
					if (this.search[key]) {
						this.filtered = true;
						break;
					}
				}
			},
			deep: true,
		},
	},
    created() {
        this.$store.state.breadcrumbs = [
            {text: 'Главная', to: {name: 'home'}},
            {text: 'Пользователи', to: {name: 'students'}},
        ];
        this.requestParams = {
            is_admin: false,
            is_staff: false
        };
        this.getList().then(list => {
            console.log(list)
        })
        this.users.list.forEach((e) => {
			this.search_existing_list.first_name.push(e.first_name)
			this.search_existing_list.last_name.push(e.last_name)
			this.search_existing_list.phone.push(e.phone)
		});
		this.search_existing_list.first_name = [...new Set(this.search_existing_list.first_name)]
		this.search_existing_list.last_name = [...new Set(this.search_existing_list.last_name)]
		this.search_existing_list.phone = [...new Set(this.search_existing_list.phone)]
    },
}
</script>

<style scoped>

</style>
