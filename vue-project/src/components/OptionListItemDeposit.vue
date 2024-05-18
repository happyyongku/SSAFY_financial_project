<template>
    <div @click="$emit('selectOption')">
        <h4 class="m-2">예금 상품 옵션</h4>
        <div class="border-bottom p-3 my-2">
            <h5>저축 금리 유형</h5>
            {{ option.intr_rate_type_nm }}
        </div>
        <div class="border-bottom p-3 my-2">
            <h5>저축 기간</h5>
            {{ option.save_trm }}
        </div>
        <div class="border-bottom p-3 my-2">
            <h5>저축 금리</h5>
            {{ option.intr_rate }}
        </div>
        <div class="border-bottom p-3 my-2">
            <h5>최고 우대 금리</h5>
            {{ option.intr_rate2 }}
        </div>
    </div>
</template>

<script setup>
    defineProps({
        option:Object
    })
</script>

<style scoped>

</style>