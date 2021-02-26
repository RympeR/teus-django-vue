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
                                          v-model="container.name"
                            />
                        </div>
                    </div>
                </div>
            </div>

            <div class="form__item">
                <span class="form__label">Изображение</span>
                <div class="form__control">
                    <template v-if="image">
                        <div class="img__thumbnail">
                            <div class="img__thumbnail-img">
                                <b-img :id="`field-${container.id}`"
                                       :src="image" width="80"
                                       v-b-modal="'modal__thumbnail' + container.id"
                                />
                            </div>
                            <b-modal :id="'modal__thumbnail' + container.id" scrollable hide-footer centered class="modal-dialog-auto">
                                <b-img :src="image" fluid/>
                            </b-modal>
                            <b-button type="button" class="media-delete" variant="link" @click="deleteImg">Удалить</b-button>
                        </div>
                    </template>
                    <template v-else>
                        <b-form-file
                            :id="`field-${container.image}`"
                            v-model="container.image"
                            plain
                        />
                    </template>
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
import ContainerMixin from '@/mixins/info/ContainerMixin';
// import 'quill/dist/quill.core.css'
// import 'quill/dist/quill.snow.css'
// import 'quill/dist/quill.bubble.css'

// import { quillEditor } from 'vue-quill-editor'


export default {
    name: 'ContainerForm',
    mixins: [ContainerMixin],
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
                {text: 'Контейнер', to: {name: 'containers'}},
                {text: 'Редактировать', to: {name: 'container-update', params: {id: this.id}}}
            ];
        }else{
            this.$store.state.breadcrumbs = [
                {text: 'Главная', to: {name: 'home'}},
                {text: 'Контейнер', to: {name: 'containers'}},
                {text: 'Создать', to: {name: 'container-create'}}
            ];
        }
        if (this.$route.params.id)
            this.getContainer(this.$route.params.id)
    },
    methods: {
        processFile(event) {
            console.log('Event: ', event);
            this.container.image = event[0]
        },
        goSave($event){
            $event.preventDefault();
            let data = Object.assign({}, this.container);
            this.saveContainer(data, this.$route.params.id);
            this.alert = true;
        },
        deleteImg() {
            let confirmDelete = confirm('Удалить фото?');
            if (confirmDelete) {
                this.image = null;
                this.container.image = [];
            }
        },
    },
}
</script>

<style scoped>

</style>
