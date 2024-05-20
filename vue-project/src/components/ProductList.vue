<template>
    <div>
        <h4 class="mt-2">상품 목록</h4>
        <div class="card my-4 shadow" style="width:28rem" v-for="product in productList" :key="product.id">
            <div class="card-body">
                <h4>{{ product.kor_co_nm }}</h4>
                <ProductListItem :product="product" @selectProduct="$emit('updateProduct', product, myItem)"/>
            </div>
        </div>
    </div>
</template>

<script setup>
    import ProductListItem from '@/components/ProductListItem.vue'
    defineProps({
        productList:Array,
        myItem: Number,
        type: String
    })

</script>

<style scoped>

</style>