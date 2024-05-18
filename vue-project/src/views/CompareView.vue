<template>
  <div>
    <h1>예적금 금리 비교</h1>
    <button @click="selectInitialize">초기화</button>
    <ProductType v-if="!store.selectedType" @typeSelect="handleType"/>
    <div class="d-flex flex-row justify-content-evenly" v-if="store.selectedType">
      <div>
        <h2>상품 1</h2>
        <BankList v-if="store.selectedType && !store.selectedBank1" :bank-list="store.bankList" :my-item="1" @bankSelect="handleBank"/>
        <ProductList v-if="store.selectedBank1 && !store.selectedProduct1" :product-list="store.productList1"/>
      </div>
      <div>
        <h2>상품 2</h2>
        <BankList v-if="store.selectedType && !store.selectedBank2" :bank-list="store.bankList" :my-item="2" @bankSelect="handleBank"/>
        <ProductList v-if="store.selectedBank2 && !store.selectedProduct2" :product-list="store.productList2"/>
      </div>
    </div>
    
  </div>
</template>

<script setup>
  import {ref, onMounted, watch, watchEffect} from 'vue'
  import {useFinancialStore} from '@/stores/financial.js'
  import ProductType from '@/components/ProductType.vue'
  import BankList from '@/components/BankList.vue'
  import ProductList from '../components/ProductList.vue'

  const store = useFinancialStore()
  const handleType = function(type) {
    store.selectedType = type
    console.log(type)
  }

  const handleBank = function(side, bank) {
    if (side === 1){
      store.selectedBank1 = bank
    }
    else if (side === 2){
      store.selectedBank2 = bank
    }
    console.log(side)
    console.log(bank)
  }

  const selectInitialize = function(){
    store.storeInitialize()
  }

  watch(()=>store.selectedType, (newValue)=>{
    if (newValue != null){
      store.getBankList()
    }
  })
  watch(()=>[store.selectedBank1, store.selectedBank2], (newValue, oldValue) =>{
    if (newValue[0] != null) {
      store.getProductList(1)
    }
    if (newValue[1] != null) {
      store.getProductList(2) 
    }
  })
</script>

<style scoped>

</style>