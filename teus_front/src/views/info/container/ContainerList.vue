<template>
    <b-row>
        <b-col>
            <div class="mb-4">
                <b-button :to="{name: 'container-create'}" variant="primary" size="md">
                    Добавить
                </b-button>
            </div>
            <b-table hover outlined head-variant="light"
                :items="containers.list"
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
                <template v-slot:cell(image)="data">
                    <table-thumbnail v-if="data.item.image"
                        :id="data.item.id"
                        :src="data.item.image"
                    />
                </template>
                <template v-slot:cell(actions)="data">
                    <div class="table__actions">
                        <b-button class="btn_edit" :to="{name: 'container-update', params: {id: data.item.id}}"></b-button>
                        <!--<btn-turn :turn="true"/>-->
                        <b-button class="btn_delete" @click="deleteItem(data.item.id)"/>
                    </div>
                </template>
            </b-table>
        </b-col>
    </b-row>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
    name: "ContainerList",

    data () {
        return {
            fields: [
                { key: 'index', label: '#'},
                { key: 'id', label: 'ID'},
                { key: 'name', label: 'Название', sortable: true},
                { key: 'image', label: 'Иконка'},
                { key: 'actions', label: ''},

            ],
            activePage: 1,
            filter: {
                level: null
            },
        }
    },
    computed: {
        ...mapState(['containers']),
    },
    methods: {
        ...mapActions('containers', ['saveItem', 'deleteItem', 'getList'])
    },
    created() {
        this.$store.state.breadcrumbs = [
            {text: 'Главная', to: {name: 'home'}},
            {text: 'Контейнеры', to: {name: 'containers'}},
        ];
        this.$store.dispatch('containers/getList')
            .then(list => {
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
