<template>
  <div class="m-3 compare-product">
    <h3 @click="selectInitialize">◎ 예적금 금리 비교</h3>
    <button @click="selectInitialize">초기화</button>
    <ProductType v-if="!store.selectedType" @typeSelect="handleType"/>
    <div class="d-flex flex-row justify-content-evenly table-container" v-if="store.selectedType">
      <div>
        <h2>상품 1</h2>
        <BankList 
        v-if="store.selectedType" 
        :bank-list="store.bankList" 
        :my-item="1" 
        @bankSelect="handleBank"
        />
        <ProductList 
        v-if="store.selectedBank1 && !store.selectedProduct1" 
        :product-list="store.productList1"
        :my-item="1"
        :type="store.selectedType"
        @updateProduct="updateProduct"
        />
        <OptionList
        v-if="store.selectedProduct1 && !store.selectedOption1"
        :option-list="store.optionList1"
        :my-item="1"
        :type="store.selectedType"
        :bank="store.bank1"
        :product="store.product1"
        @updateOption="updateOption"
        />
        <ProductCompare
        v-if="store.selectedOption1"
        :bank="store.bank1"
        :product="store.product1"
        :option="store.option1"
        :type="store.selectedType"
        />
      </div>
      <div>
        <h2>상품 2</h2>
        <BankList 
        v-if="store.selectedType" 
        :bank-list="store.bankList" 
        :my-item="2" 
        @bankSelect="handleBank"
        />
        <ProductList 
        v-if="store.selectedBank2 && !store.selectedProduct2" 
        :product-list="store.productList2"
        :my-item="2"
        :type="store.selectedType"
        @updateProduct="updateProduct"
        />
        <OptionList
        v-if="store.selectedProduct2 && !store.selectedOption2"
        :option-list="store.optionList2"
        :my-item="2"
        :type="store.selectedType"
        :bank="store.bank2"
        :product="store.product2"
        @updateOption="updateOption"
        />
        <ProductCompare
        v-if="store.selectedOption2"
        :bank="store.bank2"
        :product="store.product2"
        :option="store.option2"
        :type="store.selectedType"
        />

      </div>
    </div>
    
  </div>
</template>

<script setup>
  import {ref, onMounted, watch, watchEffect} from 'vue'
  import { useRoute, useRouter } from 'vue-router'
  import {useFinancialStore} from '@/stores/financial.js'
  import ProductType from '@/components/ProductType.vue'
  import BankList from '@/components/BankList.vue'
  import ProductList from '@/components/ProductList.vue'
  import OptionList from '@/components/OptionList.vue'
  import ProductCompare from '@/components/ProductCompare.vue'

  const store = useFinancialStore()
  const router = useRouter()

  const handleType = function(type) {
    store.selectedType = type
    console.log(type)
  }

  const handleBank = function(side, bank) {
    if (side === 1){
      store.selectedBank1 = bank
      store.selectedProduct1 = null
      store.selectedOption1 = null
    }
    else if (side === 2){
      store.selectedBank2 = bank
      store.selectedProduct2 = null
      store.selectedOption2 = null
    }
  }

  const updateProduct = function(product, item){
    if (item === 1){
      store.selectedProduct1 = product.id
      store.product1 = product
      console.log(`상품1 : ${store.product1}`)
    }
    else if (item === 2){
      store.selectedProduct2 = product.id
      store.product2 = product
      console.log(`상품2 : ${store.product2}`)
    }
  }

  const updateOption = function(option, item){
    if (item === 1){
      store.selectedOption1 = option.id
      store.option1 = option
      console.log('옵션 1',store.option1)
    }
    else if (item === 2){
      store.selectedOption2 = option.id
      store.option2 = option
      console.log('옵션 2', store.option2)
    }

  }

  const selectInitialize = function(){
    store.storeInitialize()
  }

  watch(()=>store.selectedType, (newValue)=>{
    if (newValue != null){
      store.getBankList()
    }
  })

  watch(()=>[store.selectedBank1, store.selectedBank2], (newValue) =>{
    if (newValue[0] != null) {
      store.getProductList(1)
    }
    if (newValue[1] != null) {
      store.getProductList(2) 
    }
  })

  watch(()=>[store.selectedProduct1, store.selectedProduct2], (newValue) => {
    console.log(`change! ${newValue}`)
    if (newValue[0] != null) {
      store.getOptionList(1)
    }
    if (newValue[1] != null) {
      store.getOptionList(2)
    }
  })

</script>

<style scoped>
h3 {
  font-family: Georgia, serif;
}

.table-container {
    width: 100%;
    max-width: 100%;
    max-height: 600px;
    overflow: auto;
    border: 1px solid #ddd;
    padding-bottom: 10px;
    text-align: center;
    background-color: #8C7C68;
}


.compare-product {
  width: 90%;
}
</style>