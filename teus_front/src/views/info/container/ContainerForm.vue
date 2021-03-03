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
                                v-model="containers.item.name"
                            />
                        </div>
                    </div>
                </div>
            </div>
            {{containers.item}}
            <div class="form__item">
                <span class="form__label">Изображение</span>
                <div class="form__control">
                    <template v-if="containers.item.image">
                        <div class="img__thumbnail">
                            <div class="img__thumbnail-img">
                                <b-img :id="`field-${containers.item.container_id}`"
                                       :src="containers.item.image" width="80"
                                       v-b-modal="'modal__thumbnail' + containers.item.container_id"
                                />
                            </div>
                            <b-modal :id="'modal__thumbnail' + containers.item.container_id" scrollable hide-footer centered class="modal-dialog-auto">
                                <b-img :src="containers.item.image" fluid/>
                            </b-modal>
                            <b-button type="button" class="media-delete" variant="link" @click="deleteImg">Удалить</b-button>
                        </div>
                    </template>
                    <template v-else>
                        <b-form-file
                            :id="`field-${containers.image}`"
                            v-model="containers.image"
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

import { mapState } from 'vuex'

export default {
    name: 'ContainerForm',
    components: {
        
    },
    data () {
        return {
            id: this.$route.params.id,
            alert: false
        }
    },

    created() {
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
        if (this.id) {
            this.$store.dispatch('containers/getItem', this.id)
                .then(item => {
                    console.log(item)
                })
                .catch(error => {
                    console.log(error)
                });
        }
    },
    computed: {
        ...mapState(['containers']),
    },
    methods: {
        processFile(event) {
            console.log('Event: ', event);
            this.containers.item.image = event[0]
        },
        goSave($event){
            $event.preventDefault();
            
            let data = Object.assign({}, this.containers.item);
            data.id = this.id
            data.image = this.containers.image;
            
            console.log(data);

            this.$store.dispatch('containers/saveItem', data)
                .then(item => {
                    console.log(item)
                })
                .catch(error => {
                    console.log(error)
                });
        },
        deleteImg() {
            let confirmDelete = confirm('Удалить фото?');
            if (confirmDelete) {
                this.containers.image = null;
                this.containers.item.image = [];
            }
        },
    },
}
</script>

<style scoped>

</style>
