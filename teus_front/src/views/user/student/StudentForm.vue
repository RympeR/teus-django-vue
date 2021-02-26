<template>
    <b-form @submit="goSave($event)">
        <div class="form__item">
            <span class="form__label">Номер телефона</span>
            <div class="form__control">
                <b-form-input class="short"
                    type="text"
                    v-model="user.phone"
                />
            </div>
        </div>
        <div class="form__item">
            <span class="form__label">Фамилия</span>
            <div class="form__control">
                <b-form-input class="short"
                    type="text"
                    v-model="user.last_name"
                />
            </div>
        </div>
        <div class="form__item">
            <span class="form__label">Имя</span>
            <div class="form__control">
                <b-form-input class="short"
                    type="text"
                    v-model="user.first_name"
                />
            </div>
        </div>

        <div class="form__item">
            <span class="form__label">Аватар</span>
            <div class="form__control">
                <template v-if="image">
                    <div class="img__thumbnail">
                        <div class="img__thumbnail-img">
                            <b-img :id="`field-${user.id}`"
                                :src="image" width="80"
                                v-b-modal="'modal__thumbnail' + user.id"
                            />
                        </div>
                        <b-modal :id="'modal__thumbnail' + user.id" scrollable hide-footer centered class="modal-dialog-auto">
                            <b-img :src="image" fluid/>
                        </b-modal>
                        <b-button type="button" class="media-delete" variant="link" @click="deleteImg">Удалить</b-button>
                    </div>
                </template>
                <template v-else>
                    <b-form-file
                        :id="`field-${user.image}`"
                        v-model="user.image"
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
import UserMixin from '@/mixins/user/UserMixin';

export default {
    name: 'UserForm',
    mixins: [UserMixin],
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
        if (this.$route.params.id)
            this.getUser(this.$route.params.id);
    },
    methods: {
        processFile(event) {
            this.user.image = event[0]
        },
        goSave($event){
            $event.preventDefault();
            let data = Object.assign({}, this.user);
            this.saveUser(data, this.$route.params.id);
            this.alert = true;
        },
        deleteImg() {
            let confirmDelete = confirm('Удалить фото?');
            if (confirmDelete) {
                this.image = null;
                this.user.image = [];
            }
        } 
    },
}
</script>

<style scoped>

</style>
