<template>
  <div>
    <h1>예적금 금리 비교</h1>
    <ProductType v-if="!store.selectedType" @typeSelect="handleType"/>
    <BankList v-if="store.selectedType && !store.selectedBank" :bank-list="store.bankList"/>
    <ProductList v-if="store.selectedBank && !store.selectedProduct"/>
    
  </div>
</template>

<script setup>
  import {ref, onMounted, watch} from 'vue'
  import {useFinancialStore} from '@/stores/financial.js'
  import ProductType from '@/components/ProductType.vue'
  import BankList from '@/components/BankList.vue'
  import ProductList from '../components/ProductList.vue'

  const store = useFinancialStore()
  const handleType = function(type) {
    store.selectedType = type
    console.log(type)
  }

  watch(()=>store.selectedType, ()=>{
    store.getBankList()
  })
</script>

<style scoped>

</style>