<template>
    <header class="header">
        <b-container class="layout__container" fluid>
            <b-row class="align-items-center">
                <b-col col md=4 lg=3>
                    <b-link class="logo" :to="{name: 'home'}">
                        <img src="@/assets/img/logo.svg" alt="">
                    </b-link>
                </b-col>
                <b-col col md=8 lg=9>
                    <div class="header__actions">
                        <!-- <a class="header__site" href="https://www.studio-maximus.com/" target="_blank">studio-maximus.com</a> -->
                        <!-- <span class="header__sepator">|</span> -->
                        <a class="header__logged" href='http://api-teus.maximusapp.com/apidocs/'>АПИ документация</a>
                        <span class="header__sepator">|</span>
                        <p class="header__logged">Вы вошли как: <span>Администратор</span></p>
                        <span class="header__sepator">|</span>
                        <button type="button" class="header__logout" @click="logout">
                            Выйти
                            <b-icon-box-arrow-in-right/>
                        </button>
                    </div>
                </b-col>
            </b-row>
        </b-container>
    </header>
</template>

<script>
export default {
    name: 'TheHeader',
    methods: {
        logout() {
            this.$store.dispatch('logout')
            .then(() => {
                this.$router.push('/login')
            })
        }
    }
}
</script>

<style lang="scss">
@import '~@/assets/scss/mixins';
.header {
    position: relative;
    padding: 15px 0;
    box-shadow: 0px 20px 100px -20px rgba($color: #bce1fe, $alpha: 0.5);
}

.logo {
    display: flex;
    align-items: flex-start;
    width: fit-content;
}

.header__actions {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    flex-wrap: wrap;
}

.header__site {
    @include link;
}

.header__logged {
    margin: 0;
    text-align: right;
    span {
        color: #28a745;
    }
}

.header__logout {
    @include reset-btn;
    @include link;
    outline: none;
}

.header__sepator {
    padding: 0 15px;
}
</style>