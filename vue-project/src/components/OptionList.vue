<template>
    <div>
        <h4 class="my-2">{{ bank }}</h4>
        <h5 class="my-2">{{ product.fin_prdt_nm }}</h5>
        <div class="card my-4 shadow" style="width:28rem" 
        v-for="option in optionList" :key="option.id">
            <div class="card-body">
                <OptionListItmeDeposit
                :option="option"
                @selectOption="$emit('updateOption', option, myItem)"
                v-if="type==='deposit'"
                />
                <OptionListItemInstallment
                :option="option"
                v-if="type==='installment'"
                @selectOption="$emit('updateOption', option, myItem)"
                />
            </div>

        </div>

    </div>
</template>

<script setup>
    import OptionListItmeDeposit from '@/components/OptionListItemDeposit.vue'
    import OptionListItemInstallment from '@/components/OptionListItemInstallment.vue'
    defineProps({
        optionList:Array,
        myItem:Number,
        type:String,
        bank:String,
        product:Object
    })

</script>

<style scoped>

</style>