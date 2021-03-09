<template>
    <b-row>
        <b-col>
            <div class="mb-4">
                <b-button :to="{name: 'line-create'}" variant="primary" size="md">
                    Добавить
                </b-button>
            </div>
            <b-table hover outlined head-variant="light"
                :items="lines.list"
                :fields="fields"
                :filter="filter"
            >
                <template #cell(index)="data">
                    <b>{{ data.index + 1 }}</b>
                </template>
                <template v-slot:cell(actions)="data">
                    <div class="table__actions">
                        <b-button class="btn_edit" :to="{name: 'line-update', params: {id: data.item.id}}"></b-button>
                        <b-button class="btn_delete" @click="deleteLine(data.item.id)"/>
                    </div>
                </template>
            </b-table>
        </b-col>
    </b-row>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
    name: "LineList",
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
        ...mapState(['lines']),
    },
    created() {
        this.$store.state.breadcrumbs = [
            {text: 'Главная', to: {name: 'home'}},
            {text: 'Линии', to: {name: 'lines'}},
        ];
        
        this.getLines().then(list => {
            console.log(list)
        })
        
        // this.$store.dispatch('lines/getList')
        //     .then(list => {
        //         console.log(list)
        //     })
        //     .catch(error => {
        //         console.log(error)
        //     });
    },
    methods: {
        ...mapActions(
            //'lines', ['saveItem', 'deleteItem', 'getList']),
            {
                saveLine: 'lines/saveItem',
                deleteLine: 'lines/deleteItem',
                getLines: 'lines/getList'
            }
        )
    },

}
</script>

<style scoped>

</style>
