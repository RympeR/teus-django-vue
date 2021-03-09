<template>
    <b-form @submit="goSave">
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

import { mapState } from 'vuex'

export default {
    name: 'LineForm',
    components: {
        
    },
    data () {
        return {
            id: this.$route.params.id,
            alert: false
        }
    },
    computed: {
        ...mapState(['lines']),
    },
    created() {
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
        goSave(e){
            e.preventDefault();
            let data = Object.assign({}, this.lines.item);
            data.id = this.id
            this.$store.dispatch('lines/saveItem', data)
                .then(item => {
                    console.log(item)
                    this.templateShowSuccess();
                    if(!data.id)
                        this.goBack();
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
