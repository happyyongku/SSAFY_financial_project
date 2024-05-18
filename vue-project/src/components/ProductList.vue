<template>
    <div>
        <p v-for="product in productList">{{ product }}</p>
    </div>
</template>

<script setup>
    defineProps({
        productList:Array
    })
</script>

<style scoped>

</style>