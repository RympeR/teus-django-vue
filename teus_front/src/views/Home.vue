<template>
    <div class="home">     
        <h1>Привет, это админ-панель "Teus"</h1>
        <p>Для начала работы необходимо выбрать нужный раздел слева.</p>
        <p>Если у вас возникнут вопросы, вы всегда можете их задать по адресу: <a href="mailto:info@studio-maximus.com">info@studio-maximus.com</a></p>
    </div>
</template>

<script>
export default {
    name: "Home",
    created() {
        this.$store.state.breadcrumbs = [];
    }
}
</script>

<style lang="scss" scoped>
@import '~@/assets/scss/mixins';
.home {
    
}

h1 {
    font-size: 32px;
    padding: 0.75rem 0;
    margin-bottom: 1rem;
}

a {
    @include link;
}
</style>