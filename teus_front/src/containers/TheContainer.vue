<template>
    <div class="layout">
        <TheHeader/>
        <b-container class="layout__container" fluid>
            <div class="layout__inner">
                <TheSidebar/>
                <div class="page">
                    <Breadcrumb/>
                    <div class="content">
                        <router-view/>
                    </div>
                </div>
            </div>
        </b-container>
        <TheFooter/>
    </div>
</template>

<script>
import TheSidebar from './TheSidebar'
import TheHeader from './TheHeader'
import TheFooter from './TheFooter'
import Breadcrumb from '@/components/Breadcrumb.vue'

export default {
    name: 'TheContainer',
    components: {
        TheSidebar,
        TheHeader,
        TheFooter,
        Breadcrumb,
    }
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.3s;
}

.fade-enter,
.fade-leave-to {
    opacity: 0;
}
</style>
