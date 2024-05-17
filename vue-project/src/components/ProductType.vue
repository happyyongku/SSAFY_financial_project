<template>
    <div>
        <h1>상품 유형 선택</h1>
        <div @click="$emit('typeSelect', 'deposit')">
            정기 예금
        </div>
        <div @click="$emit('typeSelect', 'installment')">
            적금
        </div>
    </div>
</template>

<script setup>

</script>

<style scoped>

</style>