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
							<template v-if="field.key === 'first_user_name'">
								{{ field.label }}
								<input
									class="input"
									@input="getFilteredDeals(search)"
									v-model="search.first_user_name"
									list="user-list"
								/>
								<b-form-datalist
									id="user-list"
									:options="search_existing_list.first_users_names"
								>
								</b-form-datalist>
							</template>
							<template v-else-if="field.key === 'first_user_phone'">
								{{ field.label }}
								<input
									class="input"
									@input="getFilteredDeals(search)"
									v-model="search.first_user_phone"
								/>

							</template>
							<template v-else-if="field.key === 'sec_user_name'">
								{{ field.label }}
								<input
									class="input"
									@input="getFilteredDeals(search)"
									v-model="search.sec_user_name"
									list="user-s-n-list"
								/>
								<b-form-datalist
									id="user-s-n-list"
									:options="search_existing_list.first_users_names"
								></b-form-datalist>
							</template>
							<template v-else-if="field.key === 'sec_user_phone'">
								{{ field.label }}
								<input
									class="input"
									@input="getFilteredDeals(search)"
									v-model="search.sec_user_phone"
								/>
							</template>
							<template v-else-if="field.key === 'line'">
								<div class="stick-top">{{ field.label }}</div>
								<input
									class="input"
									:placeholder="field.label"
									@input="getFilteredDeals(search)"
									v-model="search.line_name"
									list="line-list"
								/>
								<b-form-datalist
									id="line-list"
									:options="search_existing_list.lines"
								>
								</b-form-datalist>
							</template>
							<template v-else-if="field.key === 'city'">
								<div class="stick-top">{{ field.label }}</div>
								<input
									class="input"
									v-model="search.city_name"
									@input="getFilteredDeals(search)"
									:placeholder="field.label"
									list="city-list"
								/>
								<b-form-datalist
									id="city-list"
									:options="search_existing_list.cities"
								>
								</b-form-datalist>
							</template>
							<template v-else-if="field.key === 'container'">
								<div class="stick-top">{{ field.label }}</div>
								<input
									class="input"
									v-model="search.container_name"
									@input="getFilteredDeals(search)"
									:placeholder="field.label"
									list="container-list"
								/>
								<b-form-datalist
									id="container-list"
									:options="search_existing_list.containers"
								>
								</b-form-datalist>
							</template>
							<template v-else-if="field.key === 'amount'">
								<div class="stick-top">{{ field.label }}</div>
								<input
									class="input"
									v-model="search.amount"
									@input="getFilteredDeals(search)"
									:placeholder="field.label"
								/>
							</template>
							<template v-else-if="field.key === 'handshake'">
								{{ field.label }}
								<b-form-datepicker
									locale="ru"
									placeholder="от"
									:dateFormatOptions="{
										day: 'numeric',
										month: 'short',
										year: 'numeric',
									}"
									@input="getFilteredDeals(search)"
									size="sm"
									v-model="search.handshake"
									class="mb-2"
								></b-form-datepicker>
								<b-form-datepicker
									locale="ru"
									placeholder="до"
									:dateFormatOptions="{
										day: 'numeric',
										month: 'short',
										year: 'numeric',
									}"
									@input="getFilteredDeals(search)"
									size="sm"
									v-model="search.handshake_end"
									class="mb-2"
								></b-form-datepicker>
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
					<b-tr v-for="item in lists" :key="item.id">
						<b-td v-for="field in fields" :key="field.key">
							<template v-if="field.key === 'first_user_name'">
								<b-link
									:to="{
										name: 'student-update',
										params: { id: item[field.key].id },
									}"
									>{{ item[field.key].name }}</b-link
								>
							</template>
							<template v-else-if="field.key === 'first_user_phone'">
								<b-link
									:to="{
										name: 'student-update',
										params: { id: item[field.key].id },
									}"
									>{{ item[field.key].phone }}</b-link
								>
							</template>
							<template v-else-if="field.key === 'sec_user_name'">
								<b-link
									:to="{
										name: 'student-update',
										params: { id: item[field.key].id },
									}"
									>{{ item[field.key].name }}</b-link
								>
							</template>
							<template v-else-if="field.key === 'sec_user_phone'">
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
							<template v-else-if="field.key === 'handshake'">
								{{ item[field.key] }}
							</template>
							<template v-else-if="field.key === 'actions'">
								<div class="table__actions">
									<b-button
										class="btn_edit"
										:to="{
											name: 'deals-update',
											params: { id: item.id },
										}"
									></b-button>
									<b-button
										class="btn_delete"
										@click="deleteUserDeal(item.id)"
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
			<template v-if="deals.list.length > perPage">
				<b-pagination
					v-model="currentPage"
					:total-rows="rows"
					:per-page="perPage"
				></b-pagination>
			</template>
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
				{ key: "first_user_name", label: "Предложение имя" },
				{ key: "first_user_phone", label: "Предложение телефон" },
				{ key: "sec_user_name", label: "Запрос имя" },
				{ key: "sec_user_phone", label: "Запрос телефон" },
				{ key: "line", label: "Линия" },
				{ key: "city", label: "Город" },
				{ key: "container", label: "Контейнер" },
				{ key: "amount", label: "Кол-во", sortable: true },
				{ key: "handshake", label: "Дата рукопожатия" },

				{ key: "actions", label: "" },
			],
			activePage: 1,
			search: {
				first_user_name: "",
				sec_user_name: "",
				first_user_phone: "",
				sec_user_phone: "",
				line_name: "",
				city_name: "",
				container_name: "",
				amount: "",
				handshake: "",
				handshake_end: "",
			},
			filtered: false,
			perPage: 20,
			currentPage: 1,
			search_existing_list:{
				lines:[],
				cities: [],
				first_users_names: [],
				first_users_phones: [],
				containers: [],
			}
		};
	},
	computed: {
		...mapState(["deals", "lines", "containers", "users", "cities"]),
		rows() {
			return this.deals.list.length;
		},
		lists() {
			const items = this.deals.list;
			return items.slice(
				(this.currentPage - 1) * this.perPage,
				this.currentPage * this.perPage
			);
		},
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
	async created() {
		this.$store.state.breadcrumbs = [
			{ text: "Главная", to: { name: "home" } },
			{ text: "Сделки", to: { name: "deals" } },
		];

		await this.getUserDeal().then((list) => {
			console.log(list);
		});
		await this.getLines().then((list) => {
			console.log(list);
		});
		await this.getContainers().then((list) => {
			console.log(list);
		});
		await this.getCities().then((list) => {
			console.log(list);
		});
		await this.$store
			.dispatch("users/getList")
			.then((item) => {
				console.log(item);
			})
			.catch((error) => {
				console.log(error);
			});
		this.deals.list.forEach((el) => {
			console.log(el)
			this.search_existing_list.lines.push(el.line.name)
			this.search_existing_list.cities.push(el.city.name)
			this.search_existing_list.containers.push(el.container.name)
			this.search_existing_list.first_users_names.push(el.first_user.name)
			this.search_existing_list.first_users_phones.push(el.first_user.phone)
		});
		console.log('----')
		console.log(this.deals.list)
		console.log('----')
		this.search_existing_list.lines = [...new Set(this.search_existing_list.lines)]
		this.search_existing_list.cities = [...new Set(this.search_existing_list.cities)]
		this.search_existing_list.containers = [...new Set(this.search_existing_list.containers)]
		this.search_existing_list.first_users_names = [...new Set(this.search_existing_list.first_users_names)]
		this.search_existing_list.first_users_phones = [...new Set(this.search_existing_list.first_users_phones)]
	},
	methods: {
		...mapActions({
			saveUserDeal: "deals/saveItem",
			deleteUserDeal: "deals/deleteItem",
			getUserDeal: "deals/getList",
			getFilteredDeals: "deals/getFilteredItems",
			getLines: "lines/getList",
			getContainers: "containers/getList",
			getUsers: "users/getList",
			getCities: "cities/getList",
		}),
		resetFilters() {
			this.filtered = false;
			this.search = {
				first_user_name: "",
				sec_user_name: "",
				first_user_phone: "",
				sec_user_phone: "",
				line_name: "",
				city_name: "",
				container_name: "",
				amount: "",
				handshake: "",
				handshake_end: "",
			};
			this.getUserDeal().then((list) => {
				console.log(list);
			});
		},
	},
};
</script>

<style scoped></style>
