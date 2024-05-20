<template>
    <div class="my-3">
        <h4 class="my-2">{{bank}}</h4>
        <div class="card shadow" style="width:28rem">
            <div class="card-body border-bottom">
                <ProductListItem :product="product"/>
            </div>
            <div class="card-body">
                <OptionListItmeDeposit :option="option" v-if="type==='deposit'"/>
                <OptionListItemInstallment :option="option" v-if="type==='installment'"/>
            </div>

        </div>
    </div>
</template>

<script setup>
    import ProductListItem from '@/components/ProductListItem.vue'
    import OptionListItmeDeposit from '@/components/OptionListItemDeposit.vue'
    import OptionListItemInstallment from '@/components/OptionListItemInstallment.vue'
    defineProps({
        bank:String,
        product:Object,
        option:Object,
        type:String
    })
</script>

<style scoped>

</style>