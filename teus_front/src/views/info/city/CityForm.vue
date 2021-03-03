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
                                          v-model="cities.item.name"
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
    name: 'CityForm',
    components: {
        
    },
    data () {
        return {
            id: null,
            alert: false
        }
    },
    computed: {
        ...mapState(['cities']),
    },
    created() {
        this.id = this.$route.params.id;
        if (this.id){
            this.$store.state.breadcrumbs = [
                {text: 'Главная', to: {name: 'home'}},
                {text: 'Город', to: {name: 'cities'}},
                {text: 'Редактировать', to: {name: 'city-update', params: {id: this.id}}}
            ];
        }else{
            this.$store.state.breadcrumbs = [
                {text: 'Главная', to: {name: 'home'}},
                {text: 'Город', to: {name: 'cities'}},
                {text: 'Создать', to: {name: 'city-create'}}
            ];
        }
        if (this.$route.params.id) {
            this.$store.dispatch('cities/getItem', this.$route.params.id)
                .then(item => {
                    console.log(item)
                })
                .catch(error => {
                    console.log(error)
                });
        }
    },
    methods: {
        goSave($event){
            $event.preventDefault();
            let data = Object.assign({}, this.cities.item);
            data.id = this.$route.params.id
            this.$store.dispatch('cities/saveItem',data)
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
