<template>
    <div class="login">
        <b-container>
            <div class="login__inner">
                <h1 class="login__title">Панель управления</h1>
                <b-form @submit="login($event)" class="login__form">
                    <b-form-group label-cols-sm="4"
                                  label="E-mail"
                    >
                        <b-form-input
                            v-model="email"
                            type="email"
                            required
                            placeholder="Введите ваш E-mail"
                        />
                    </b-form-group>

                    <b-form-group label-cols-sm="4"
                                  label="Пароль"
                    >
                        <b-form-input type="password" required
                                      v-model="password"
                                      placeholder="Введите ваш пароль"
                        />
                        <b-form-invalid-feedback :state="validation">
                            {{ validation_text }}
                        </b-form-invalid-feedback>
                    </b-form-group>
                    <b-form-group label-cols-sm="4">
                        <b-form-checkbox
                            v-model="remember">
                            Запомнить меня
                        </b-form-checkbox>
                    </b-form-group>

                    <b-form-group label-cols-sm="4">
                        <b-button type="submit" variant="primary">Войти</b-button>
                    </b-form-group>
                </b-form>
            </div>
        </b-container>
    </div>
</template>

<script>

export default {
    name: 'Login',
    data() {
        return {
            email: '',
            password: '',
            remember: false,
            validation: true,
            validation_text: 'Пароль не подходит! Хе-хе :)',
        }
    },
    methods: {
        login($event) {
            $event.preventDefault();
            let email = this.email;
            let password = this.password;
            this.$store.dispatch('login', {email, password})
                .then(() => {
                    console.log('login')
                    this.validation = true;
                    this.$router.push({name: 'home'})
                })
                .catch(response => {
                    console.log(response)
                    // self.validation_text = self.collectError(response);
                    this.loading = false;
                    this.validation = false;
                })
        },
    }
}
</script>

<style lang="scss">
.login {
    margin: auto 0;
}

.login__inner {
    max-width: 540px;
    margin: 30px auto;
    padding: 30px 60px;
    box-shadow: 0 20px 50px -10px #bce1fe;
}

.login__title {
    margin-bottom: 20px;
    font-size: 24px;
    text-align: center;
}

.login__form {

}

.login__copyright {
    margin: 30px 0 0;
    font-size: 14px;
    text-align: center;
}
</style>