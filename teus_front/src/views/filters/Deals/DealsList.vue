<template>
	<b-row>
		<b-col>
			<div class="mb-4">
				<b-button
					@click="resetFilters"
					variant="primary"
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
							<template v-if="field.key === 'first_user'">
								{{ field.label }}
								<input
									class="input"
									@input="getFilteredDeals(search)"
									v-model="search.first_user_name"
									list="user-list"
								/>
								<b-form-datalist
									id="user-list"
									:options="users_names"
								>
								</b-form-datalist>
							</template>
							<template v-else-if="field.key === 'sec_user'">
								{{ field.label }}
								<input
									class="input"
									@input="getFilteredDeals(search)"
									v-model="search.sec_user_name"
									list="user-sec-list"
								/>
								<b-form-datalist
									id="user-sec-list"
									:options="users_names"
								></b-form-datalist>
							</template>
							<template v-else-if="field.key === 'line'">
								{{ field.label }}
								<input
									class="input"
									:placeholder="field.label"
									@input="getFilteredDeals(search)"
									v-model="search.line_name"
									list="line-list"
								/>
								<b-form-datalist
									id="line-list"
									:options="lines_names"
								>
								</b-form-datalist>
							</template>
							<template v-else-if="field.key === 'city'">
								{{ field.label }}
								<input
									class="input"
									v-model="search.city_name"
									@input="getFilteredDeals(search)"
									:placeholder="field.label"
									list="city-list"
								/>
								<b-form-datalist
									id="city-list"
									:options="cities_names"
								>
								</b-form-datalist>
							</template>
							<template v-else-if="field.key === 'container'">
								{{ field.label }}
								<input
									class="input"
									v-model="search.container_name"
									@input="getFilteredDeals(search)"
									:placeholder="field.label"
									list="container-list"
								/>
								<b-form-datalist
									id="container-list"
									:options="containers_names"
								>
								</b-form-datalist>
							</template>
							<template v-else-if="field.key === 'amount'">
								{{ field.label }}
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
									@input="getFilteredPropositions(search)"
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
							<template v-if="field.key === 'first_user'">
								<b-link
									:to="{
										name: 'student-update',
										params: { id: item[field.key].id },
									}"
									>{{ item[field.key].phone }}</b-link
								>
							</template>
							<template v-else-if="field.key === 'sec_user'">
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
			<b-pagination
				v-model="currentPage"
				:total-rows="rows"
				:per-page="perPage"
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
				{ key: "first_user", label: "Пользователь предложение" },
				{ key: "sec_user", label: "Пользователь запрос" },
				{ key: "line", label: "Линия" },
				{ key: "city", label: "Город" },
				{ key: "container", label: "Контейнер" },
				{ key: "amount", label: "Кол-во" },
				{ key: "handshake", label: "Дата рукопожатия" },

				{ key: "actions", label: "" },
			],
			activePage: 1,
			search: {
				first_user_name: "",
				sec_user_name: "",
				line_name: "",
				city_name: "",
				container_name: "",
				amount: "",
				handshake: "",
				handshake_end: "",
			},
			perPage: 1,
			currentPage: 1,
			lines_names: [],
			cities_names: [],
			containers_names: [],
			users_names: [],
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
	created() {
		this.$store.state.breadcrumbs = [
			{ text: "Главная", to: { name: "home" } },
			{ text: "Сделки", to: { name: "deals" } },
		];

		this.getUserDeal().then((list) => {
			console.log(list);
		});
		this.getLines().then((list) => {
			console.log(list);
		});
		this.getContainers().then((list) => {
			console.log(list);
		});
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
		this.lines.list.forEach((e) => {
			this.lines_names.push(e.name);
		});
		this.users.list.forEach((e) => {
			this.users_names.push(e.first_name);
		});
		this.cities.list.forEach((e) => {
			this.cities_names.push(e.name);
		});
		this.containers.list.forEach((e) => {
			this.containers_names.push(e.name);
		});
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
