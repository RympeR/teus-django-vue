<template>
    <b-button class="btn_turn" :class="[{ 'btn_turn-on': turn }]" @click="toggleOnOff"></b-button>
</template>

<script>
export default {
    props: {
        turn: Boolean
    },
    data: () => ({

    }),
    methods: {
        toggleOnOff() {
            this.turn = !this.turn;
        }
    }
}
</script>

<style lang="scss">

</style>