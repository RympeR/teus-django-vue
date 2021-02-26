<template>
    <div id="breadcrumb" v-if="$store.state.breadcrumbs.length">
        <b-breadcrumb :items="$store.state.breadcrumbs"/>
    </div>
</template>

<script>

export default {
    name: "Breadcrumb",
}
</script>

<style lang="scss">
@import '~@/assets/scss/mixins';
#breadcrumb .breadcrumb {
    font-size: 32px;
    margin-bottom: 0;
    padding-top: 0;
    padding-left: 0;
    background-color: transparent;
    
    .breadcrumb-item {
        &:first-child {
            display: none;
        }
        
        & + .breadcrumb-item {
            padding-left: 0;
            &::before {
                display: none;
            }
        }
        
        &:nth-child(n + 3) {
            position: relative;
            margin-left: 45px;
            padding-left: 0.5rem;
            ::before {
                position: absolute;
                content: ' → ';
                left: -30px;
                color: #000;
            }
        }
        
        &.active {
            color: #000;
        }
    }
    
    a {
        @include link;
    }
}
</style>