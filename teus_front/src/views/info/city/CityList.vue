<template>
    <b-row>
        <b-col>
            <div class="mb-4">
                <b-button :to="{name: 'city-create'}" variant="primary" size="md">
                    Добавить
                </b-button>
            </div>
            <b-table hover outlined head-variant="light"
                :items="cities.list"
                :fields="fields"
                :filter="filter"
                >
                <template #cell(index)="data">
                    <b>{{ data.index + 1 }}</b>
                </template>
                <template v-slot:cell(actions)="data">
                    <div class="table__actions">
                        <b-button class="btn_edit" :to="{name: 'city-update', params: {id: data.item.id}}"></b-button>
                        <!--<btn-turn :turn="true"/>-->
                        <b-button class="btn_delete" @click="deleteCity(data.item.id)"/>
                    </div>
                </template>
            </b-table>
        </b-col>
    </b-row>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
    name: "CityList",
    data () {
        return {
            fields: [
                { key: 'index', label: '#'},
                { key: 'id', label: 'ID'},
                { key: 'name', label: 'Название', sortable: true},
                { key: 'actions', label: ''},

            ],
            activePage: 1,
            filter: {
                level: null
            },
        }
    },
    computed: {
        ...mapState(['cities']),
    },
    methods: {
        ...mapActions({
                saveCity: 'cities/saveItem',
                deleteCity: 'cities/deleteItem',
                getCities: 'cities/getList'
            })
    },
    created() {
        this.$store.state.breadcrumbs = [
            {text: 'Главная', to: {name: 'home'}},
            {text: 'Города', to: {name: 'cities'}},
        ];
        this.getCities().then(list => {
                console.log(list)
        })
        .catch(error => {
            console.log(error)
        });
    }
}
</script>

<style scoped>

</style>
