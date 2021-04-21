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
				id="item-table"
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
									class="input"
									:placeholder="field.label"
									@input="getFilteredPropositions(search)"
									v-model="search.user_name"
									list="user-list"
								/>
								<b-form-datalist
									id="user-list"
									:options="search_existing_list.users_names"
								></b-form-datalist>

							</template>
							<template v-else-if="field.key === 'phone'">
								{{ field.label }}
								<input
									class="input"
									:placeholder="field.label"
									@input="getFilteredPropositions(search)"
									v-model="search.user_phone"
								/>

							</template>

							<template v-else-if="field.key === 'line'">
								{{ field.label }}
								<input
									class="input"
									:placeholder="field.label"
									@input="getFilteredPropositions(search)"
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
								{{ field.label }}
								<input
									class="input"
									v-model="search.city_name"
									@input="getFilteredPropositions(search)"
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
								{{ field.label }}
								<input
									class="input"
									v-model="search.container_name"
									@input="getFilteredPropositions(search)"
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
								{{ field.label }}
								<input
									class="input"
									v-model="search.amount"
									@input="getFilteredPropositions(search)"
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
									@input="getFilteredPropositions(search)"
									size="sm"
									v-model="search.request_date"
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
									v-model="search.request_end_date"
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
							<template v-if="field.key === 'user'">
								<b-link
									:to="{
										name: 'student-update',
										params: { id: item[field.key].id },
									}"
									>{{ item[field.key].name }}</b-link
								>
							</template>
							<template v-else-if="field.key === 'phone'">
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
										:to="{
											name: 'proposition-update',
											params: { id: item.id },
										}"
									></b-button>
									<b-button
										class="btn_delete"
										@click="deleteUserProposition(item.id)"
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
			<template v-if="user_propositions.list.length > perPage">
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
	name: "UserPropositiontList",
	data() {
		return {
			fields: [
				{ key: "index", label: "#" },
				{ key: "id", label: "ID" },
				{ key: "user", label: "Пользователь" },
				{ key: "phone", label: "Телефон" },
				{ key: "line", label: "Линия" },
				{ key: "city", label: "Город" },
				{ key: "container", label: "Контейнер" },
				{ key: "amount", label: "Кол-во" , sortable: true},
				{ key: "date", label: "Дата" },
				{ key: "status", label: "Статус" },
				{ key: "actions", label: "" },
			],
			search: {
				user_name: "",
				user_phone: "",
				line_name: "",
				city_name: "",
				container_name: "",
				amount: "",
				request_date: "",
				request_end_date: "",
			},
			filtered: false,
			perPage: 20,
			currentPage: 1,
			search_existing_list:{
				lines:[],
				cities: [],
				users_names: [],
				containers: [],
				users_phones: [],
			}
		};
	},
	computed: {
		rows() {
			return this.user_propositions.list.length;
		},
		lists() {
			const items = this.user_propositions.list;
			return items.slice(
				(this.currentPage - 1) * this.perPage,
				this.currentPage * this.perPage
			);
		},
		...mapState([
			"user_propositions",
			"lines",
			"containers",
			"users",
			"cities",
		]),
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
			{ text: "Предложения", to: { name: "proposition" } },
		];

		await this.getUserPropositions().then((list) => {
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
		this.user_propositions.list.forEach((e) => {
			this.search_existing_list.lines.push(e.line.name)
			this.search_existing_list.cities.push(e.city.name)
			this.search_existing_list.containers.push(e.container.name)
			this.search_existing_list.users_names.push(e.user.name)
			this.search_existing_list.users_phones.push(e.phone.phone)
		});
		this.search_existing_list.lines = [...new Set(this.search_existing_list.lines)]
		this.search_existing_list.cities = [...new Set(this.search_existing_list.cities)]
		this.search_existing_list.containers = [...new Set(this.search_existing_list.containers)]
		this.search_existing_list.users_names = [...new Set(this.search_existing_list.users_names)]
		this.search_existing_list.users_phones = [...new Set(this.search_existing_list.users_phones)]
	},
	methods: {
		...mapActions({
			saveUserRequest: "user_propositions/saveItem",
			deleteUserProposition: "user_propositions/deleteItem",
			getUserPropositions: "user_propositions/getList",
			getFilteredPropositions: "user_propositions/getFilteredItems",
			getLines: "lines/getList",
			getContainers: "containers/getList",
			getUsers: "users/getList",
			getCities: "cities/getList",
		}),
		resetFilters() {
			this.filtered = false;
			this.search = {
				user_name: "",
				line_name: "",
				city_name: "",
				container_name: "",
				amount: "",
				request_date: "",
				request_end_date: "",
			};
			this.getUserPropositions().then((list) => {
				console.log(list);
			});
		},
	},
};
</script>

<style scoped></style>
