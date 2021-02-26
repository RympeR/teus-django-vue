<template>
    <div>
        <b-img :src="src" :alt="title" width="40" 
            class="table__thumbnail"
            v-b-modal="'modal__thumbnail' + id"
        />
        <b-modal :id="'modal__thumbnail' + id" scrollable hide-footer centered dialog-class="modal-dialog-auto" 
            :title="title"
        >
            <b-img :src="src" :alt="title"/>
        </b-modal>
    </div>
</template>

<script>
export default {
    name: "TableImg",
    props: {
        id: Number,
        src: String,
        title: String
    }
}
</script>

<style lang="scss" scoped>

</style>
