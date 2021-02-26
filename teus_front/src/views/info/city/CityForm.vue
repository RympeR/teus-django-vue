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
                                          v-model="city.name"
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
import CityMixin from '@/mixins/info/CityMixin';
// import 'quill/dist/quill.core.css'
// import 'quill/dist/quill.snow.css'
// import 'quill/dist/quill.bubble.css'

// import { quillEditor } from 'vue-quill-editor'


export default {
    name: 'CityForm',
    mixins: [CityMixin],
    components: {
        
    },
    data () {
        return {
            id: null,
            alert: false
        }
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
        if (this.$route.params.id)
            this.getCity(this.$route.params.id)
    },
    methods: {
        goSave($event){
            $event.preventDefault();
            let data = Object.assign({}, this.city);
            this.saveCity(data, this.$route.params.id);
            this.alert = true;
        },
    },
}
</script>

<style scoped>

</style>
