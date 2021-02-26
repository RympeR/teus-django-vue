<template>
    <b-form @submit="goSave($event)">
        <div class="form__item">
            <span class="form__label">Текущий пароль</span>
            <div class="form__control">
                <b-form-input class="short"
                    type="text"
                    v-model="changePassword.current_password"
                />
            </div>
        </div>
        <div class="form__item">
            <span class="form__label">Новый пароль</span>
            <div class="form__control">
                <b-form-input class="short"
                    type="text"
                    v-model="changePassword.password"
                />
            </div>
        </div>
        <div class="form__item">
            <span class="form__label">Подтвердите новый пароль</span>
            <div class="form__control">
                <b-form-input class="short"
                    type="text"
                    v-model="changePassword.password_confirm"
                />
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
            changePassword: {
                current_password: null,
                password: null,
                password_confirm: null,
            }
        }
    },
    created() {
        this.$store.state.breadcrumbs = [
            {text: 'Главная', to: {name: 'home'}},
            {text: 'Изменить пароль', to: {name: 'change-password'}},
        ];
    },
    methods: {
        goSave($event) {
            $event.preventDefault();
            let self = this;

            let formData = new FormData();
            let obj = this.changePassword;
            Object.keys(obj).map(function(key) {
                if (obj[key])
                    formData.append(key, obj[key]);
            });
            this.$store.dispatch('token')
                .then((token) => {
                    this.$axios
                        .put(
                            process.env.VUE_APP_HOST + '/api/user/change-password/',
                            formData,
                            {
                                headers: {
                                    Authorization: token,
                                    'Content-Type': 'multipart/form-data',
                                },

                            }
                        )
                        .then(function (response) {
                            self.templateShowSuccess(response);
                            self.changePassword = {
                                current_password: null,
                                password: null,
                                password_confirm: null,
                            }
                        })
                        .catch(function (response) {
                            console.log(response);
                            self.templateShowError(response);
                        })
                })
                .catch(response => {
                    console.log(response)
                })
        },
    },
}
</script>

<style scoped>

</style>
