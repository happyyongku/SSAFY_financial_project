<template>
    <div>
        <h3>Select Bank {{ myItem }}</h3>
        <form @submit.prevent="$emit('bankSelect', myItem, selected)">
            <select id="select-bank" @change="selectChange($event)" v-model="selected">
                <option value="" disabled selected hidden>Select Bank</option>
                <option v-for="bank in bankList" :key="bank.id" :value="bank.id">{{ bank.kor_co_nm }}</option>
            </select>
            <input type="submit" value="선택">
        </form>
    </div>
</template>

<script setup>
    import { defineProps, ref } from 'vue';
    defineProps({
        bankList:Array,
        myItem:Number
    })
    const selected = ref(null)
    const selectChange = (event) => {
        selected.value = event.target.value
        console.log(selected.value)
    }

</script>

<style scoped>

</style>