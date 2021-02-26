<template>
    <b-row>
        <b-col>
            <b-table hover outlined head-variant="light"
                :items="users" 
                :fields="fields"
                :filter="filter"
                >
                <template #cell(index)="data">
                    <b>{{ data.index + 1 }}</b>
                </template>
                <template v-slot:cell(image)="data">
                    <table-thumbnail v-if="data.item.image"
                        :id="data.item.id"
                        :src="data.item.image"
                    />
                </template>
                <template v-slot:cell(actions)="data">
                    <div class="table__actions">
                        <b-button class="btn_edit" :to="{name: 'student-update', params: {id: data.item.id}}"></b-button>
                        <!--<btn-turn :turn="true"/>-->
                        <b-button class="btn_delete" @click="deleteUser(data.item.id)"/>
                    </div>
                </template>
            </b-table>
        </b-col>

    </b-row>
</template>

<script>
import UserMixin from '@/mixins/user/UserMixin'

export default {
    name: "UserList",
    mixins: [UserMixin],
    data () {
        return {
            fields: [
                { key: 'index', label: '#'},
                { key: 'id', label: 'ID', sortable: true},
                { key: 'phone', label: 'Телефон', sortable: true},
                { key: 'last_name', label: 'Фамилия', sortable: true},
                { key: 'first_name', label: 'Имя'},
                { key: 'image', label: 'Аватар'},
                { key: 'actions', label: ''},
            ],
            activePage: 1,
            filter: {
                organisation: null
            },
        }
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
        this.getUsers()
    },
}
</script>

<style scoped>

</style>
