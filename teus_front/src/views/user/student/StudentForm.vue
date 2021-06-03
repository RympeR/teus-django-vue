<template>
    <b-form @submit="goSave($event)">
        <div class="form__item">
            <span class="form__label">Номер телефона</span>
            <div class="form__control">
                    {{users.item.phone}}
            </div>
        </div>
        <div class="form__item">
            <span class="form__label">Компания</span>
            <div class="form__control">
                <b-form-input class="short"
                    type="text"
                    v-model="users.item.last_name"
                />
            </div>
        </div>
        <div class="form__item">
            <span class="form__label">Имя</span>
            <div class="form__control">
                <b-form-input class="short"
                    type="text"
                    required
                    v-model="users.item.first_name"
                />
            </div>
        </div>

        <div class="form__item">
            <span class="form__label">Аватар</span>
            <div class="form__control">
                <template v-if="users.item.image">
                    <div class="img__thumbnail">
                        <div class="img__thumbnail-img">
                            <b-img :id="`field-${users.item.id}`"
                                :src="users.item.image" width="80"
                                v-b-modal="'modal__thumbnail' + users.item.id"
                            />
                        </div>
                        <b-modal :id="'modal__thumbnail' + users.item.id" scrollable hide-footer centered class="modal-dialog-auto">
                            <b-img :src="users.item.image" fluid/>
                        </b-modal>
                        <b-button type="button" class="media-delete" variant="link" @click="deleteImg">Удалить</b-button>
                    </div>
                </template>
                <template v-else>
                    <b-form-file
                        :id="`field-${users.image}`"
                        v-model="users.image"
                        plain
                    />
                </template>
            </div>
        </div>

        <div class="form__item form__item_submit">
            <div class="form__control">
                <b-button type="submit" variant="primary">Сохранить</b-button>
            </div>
        </div>
    </b-form>
</template>

<script>
import { mapState } from 'vuex'
import Vue from "vue";

export default {
    name: 'UserForm',

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
                {text: 'Пользователи', to: {name: 'students'}},
                {text: 'Редактировать', to: {name: 'student-update', params: {id: this.id}}}
            ];
        }else{
            this.$store.state.breadcrumbs = [
                {text: 'Главная', to: {name: 'home'}},
                {text: 'Пользователи', to: {name: 'students'}},
                {text: 'Создать', to: {name: 'student-create'}}
            ];
        }
        if (this.id) {
            this.$store.dispatch('users/getItem', this.id)
                .then(item => {
                    console.log(item)
                })
                .catch(error => {
                    console.log(error)
                });
        }
    },
    computed: {
        ...mapState(['users']),
    },
    methods: {
        processFile(event) {
            this.user.item.image = event[0]
        },
        goSave($event){
            
            $event.preventDefault();
            let data = Object.assign({}, this.users.item);
            data.id = this.id
            data.image = this.users.image;

            this.$store.dispatch('users/saveItem', data)
                .then(item => {
                    console.log(item)
                    Vue.templateShowSuccess();
                    if(!data.id) Vue.goBack();
                    else this.$store.dispatch('users/getItem', this.id)
                            .then(item => {
                                console.log(item)
                            })
                            .catch(error => {
                                console.log(error)
                            });
                })
                .catch(error => {
                    console.log(error)
                });
        },
        deleteImg() {
            let confirmDelete = confirm('Удалить фото?');
            if (confirmDelete) {
                this.users.image = null;
                this.users.item.image = null;
            }
        } 
    },
}
</script>

<style scoped>

</style>
