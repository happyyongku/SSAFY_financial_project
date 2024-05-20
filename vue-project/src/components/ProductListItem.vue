<template>
    <div @click="$emit('selectProduct')">
        <div class="my-2 text-center border-bottom p-3">
            <h5>{{ product.fin_prdt_nm }}</h5> 
        </div>
        <div class="fs-6 border-bottom p-3 my-2">
            <h5>만기 후 이자 </h5>
            {{ product.mtrt_int }}
        </div>
        <div class="fs-6 border-bottom p-3 my-2">
            <h5>우대 사항</h5>
            {{ product.spcl_cnd }}
        </div>
        <div class="fs-6 border-bottom p-3 my-2">
            <h5>가입 대상</h5>
            {{ product.join_member }}
        </div>
        <div class="fs-6 border-bottom p-3 my-2">
            <h5>한도</h5>
            <div v-if="product.max_limit">
                {{ product.max_limit }}
            </div>
            <div v-else>
                없음
            </div>
        </div>
        <div class="fs-6 border-bottom p-3 my-2">
            <h5>기타 사항</h5>
            {{ product.etc_note }}
        </div>
    </div>
</template>

<script setup>
    defineProps({
        product:Object,
    })
</script>

<style scoped>

</style>