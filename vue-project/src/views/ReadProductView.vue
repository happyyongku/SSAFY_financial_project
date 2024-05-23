<template>
    <div class="d-flex justify-content-center">
        <div class="m-3 read-product">
            <h3 class="my-3">◎ 전체 금융 상품 조회</h3>
            <div>
                <ProductTable/>
            </div>
        </div>
    </div>
</template>

<script setup>
import ProductTable from '@/components/ProductTable.vue';


</script>

<style scoped>

.read-product {
    width: 90%;
}

.my-3 {
    font-family: Georgia, serif;
}

</style>