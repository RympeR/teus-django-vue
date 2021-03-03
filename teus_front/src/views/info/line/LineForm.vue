<template>
    <b-form @submit="goSave($event)">
        <b-tabs content-class="mt-3">
            <b-tab title="Основное" active>
                <div class="form__item">
                    <span class="form__label">Название</span>
                    <div class="form__control">
                        <div class="row">
                            <div class="col-12">
                                <b-form-input class="short"
                                    type="text"
                                    required
                                    placeholder="ru"
                                    v-model="lines.item.name"
                                />
                            </div>
                        </div>
                    </div>
                </div>
            </b-tab>
        </b-tabs>
        <div class="form__item form__item_submit">
            <div class="form__control">
                <b-button type="submit" variant="primary">Сохранить</b-button>
            </div>
        </div>
    </b-form>
</template>

<script>
// import LineMixin from '@/mixins/info/LineMixin';
// import 'quill/dist/quill.core.css'
// import 'quill/dist/quill.snow.css'
// import 'quill/dist/quill.bubble.css'

// import { quillEditor } from 'vue-quill-editor'

import { mapState, mapActions } from 'vuex'

export default {
    name: 'LineForm',
    // mixins: [LineMixin],
    components: {
        
    },
    data () {
        return {
            id: null,
            alert: false
        }
    },
    computed: {
        ...mapState(['lines']),
        
    },
    created() {
        this.id = this.$route.params.id;
        if (this.id){
            this.$store.state.breadcrumbs = [
                {text: 'Главная', to: {name: 'home'}},
                {text: 'Линия', to: {name: 'lines'}},
                {text: 'Редактировать', to: {name: 'line-update', params: {id: this.id}}}
            ];
        }else{
            this.$store.state.breadcrumbs = [
                {text: 'Главная', to: {name: 'home'}},
                {text: 'Линия', to: {name: 'lines'}},
                {text: 'Создать', to: {name: 'line-create'}}
            ];
        }
        if (this.$route.params.id) {
            this.$store.dispatch('lines/getItem', this.$route.params.id)
                .then(item => {
                    console.log(item)
                })
                .catch(error => {
                    console.log(error)
                });
        }
    },
    methods: {
        ...mapActions('lines', ['saveItem', 'deleteItem']),
        goSave($event){
            $event.preventDefault();
            let data = Object.assign({}, this.lines.item);
            console.log(this.$route.params.id)
            data.id = this.$route.params.id
            this.$store.dispatch('lines/saveItem',data)
                .then(item => {
                    console.log(item)
                })
                .catch(error => {
                    console.log(error)
                });
        },
    },
}
</script>

<style scoped>

</style>
