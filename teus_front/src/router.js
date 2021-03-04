import Vue from 'vue'
import Router from 'vue-router'

import TheContainer from './containers/TheContainer.vue';
import Login from './components/Login.vue';
import ChangePassword from "./views/ChangePassword";
import Home from "./views/Home";

import StudentList from "./views/user/student/StudentList";
import StudentForm from "./views/user/student/StudentForm";

import LineList from "@/views/info/line/LineList";
import LineForm from "@/views/info/line/LineForm";

import CityList from "@/views/info/city/CityList";
import CityForm from "@/views/info/city/CityForm";

import ContainerList from "@/views/info/container/ContainerList";
import ContainerForm from "@/views/info/container/ContainerForm";

import UserRequestsList from "@/views/filters/UserRequest/UserRequestList"
import UserRequestForm from "@/views/filters/UserRequest/UserRequestForm"

import UserPropositionList from "@/views/filters/UserProposition/UserPropositiontList"
import UserPropositionForm from "@/views/filters/UserProposition/UserPropositionForm"

import DealsList from "@/views/filters/Deals/DealsList"
import DealsForm from "@/views/filters/Deals/DealsForm"


Vue.use(Router);

export default new Router({
	mode: 'history',
	// mode: 'hash',
	linkActiveClass: 'active',
	base: process.env.BASE_URL,
	routes: [
		{
			path: '/login',
			name: 'login',
			component: Login,
			meta: {
				requiresAuth: false
			},
		},
		{
			path: '/',
			name: 'main',
			component: TheContainer,
			redirect: 'home',
			meta: {
				requiresAuth: true
			},
			children: [
				{
					path: 'home',
					name: 'home',
					component: Home,
					meta: {
						requiresAuth: true
					},
				},
				{
					path: 'change-password',
					name: 'change-password',
					component: ChangePassword,
					meta: {
						requiresAuth: true
					},
				},
				{
					path: 'user/student',
					name: 'students',
					component: StudentList,
					meta: {
						requiresAuth: true
					},
				},
				{
					path: 'user/student/update/:id',
					name: 'student-update',
					component: StudentForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'user/student/create',
					name: 'student-create',
					component: StudentForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'city',
					name: 'cities',
					component: CityList,
					meta: {
						requiresAuth: true
					},
				},
				{
					path: 'city/update/:id',
					name: 'city-update',
					component: CityForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'city/create',
					name: 'city-create',
					component: CityForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'line',
					name: 'lines',
					component: LineList,
					meta: {
						requiresAuth: true
					},
				},
				{
					path: 'line/update/:id',
					name: 'line-update',
					component: LineForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'line/create',
					name: 'line-create',
					component: LineForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'container',
					name: 'containers',
					component: ContainerList,
					meta: {
						requiresAuth: true
					},
				},
				{
					path: 'container/update/:id',
					name: 'container-update',
					component: ContainerForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'container/create',
					name: 'container-create',
					component: ContainerForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'requests',
					name: 'requests',
					component: UserRequestsList,
					meta: {
						requiresAuth: true
					},
				},
				{
					path: 'requests/update/:id',
					name: 'requests-update',
					component: UserRequestForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'requests/create',
					name: 'requests-create',
					component: UserRequestForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'proposition',
					name: 'proposition',
					component: UserPropositionList,
					meta: {
						requiresAuth: true
					},
				},
				{
					path: 'proposition/update/:id',
					name: 'proposition-update',
					component: UserPropositionForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'proposition/create',
					name: 'proposition-create',
					component: UserPropositionForm,
					meta: {
						requiresAuth: true
					}
					
				},
				{
					path: 'deals',
					name: 'deals',
					component: DealsList,
					meta: {
						requiresAuth: true
					},
				},
				{
					path: 'deals/update/:id',
					name: 'deals-update',
					component: DealsForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'deals/create',
					name: 'deals-create',
					component: DealsForm,
					meta: {
						requiresAuth: true
					}
					
				},
			]
		},
	],
})
