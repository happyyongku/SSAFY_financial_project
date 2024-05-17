<template>
    <div>
        <h1>bank</h1>
        <div v-for="bank in bankList" :key="bank.id">
            <p>{{ bank.kor_co_nm }}</p>
            <p>{{ bank.fin_co_no}}</p>
        </div>
    </div>
</template>

<script setup>
    defineProps({
        bankList:Array
    })
</script>

<style scoped>

</style>