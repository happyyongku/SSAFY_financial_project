import { ref, computed } from 'vue'
import { defineStore} from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter.js'



export const useFinancialStore = defineStore('financial', () => {
    const selectedType = ref(null)
    const bankList = ref([])
    const selectedBank1 = ref(null)
    const bank1 = ref(null)
    const selectedBank2 = ref(null)
    const bank2 = ref(null)
    const productList1 = ref([])
    const selectedProduct1 = ref(null)
    const product1 = ref(null)
    const productList2 = ref([])
    const selectedProduct2 = ref(null)
    const product2 = ref(null)
    const optionList1 = ref([])
    const selectedOption1 = ref(null)
    const optionList2 = ref([])
    const selectedOption2 = ref(null)
    const option1 = ref(null)
    const option2 = ref(null)
    const URL = 'http://127.0.0.1:8000'
    const token= ref(useCounterStore().token)

    // const switchBankName = function(side){
    //     if (side === 1){
    //         axios({
    //             url:`${URL}/financial_product/search/bank/${selectedBank1.value}/`,
    //             method:'get'
    //         })
    //     }
    // }

    const getBankList = function(){
        axios({
            url: `${URL}/financial_product/search/bank_list/`,
            method:'get',
            headers: {
                Authorization: `Token ${token.value}`
                }
        })
        .then(response => {
            bankList.value = response.data
        })
        .catch(err => {
            console.log(err)
        })
    }

    const getProductList = function(side){
        if (side === 1){
            axios({
                url:`${URL}/financial_product/search/product/${selectedType.value}/${selectedBank1.value}/`,
                method:'get'
            })
            .then(response => {
                productList1.value = response.data
                bank1.value = productList1.value[0].kor_co_nm
                console.log(`bank1 : ${bank1.value}`)
            })
            .catch(err => {
                console.log(err)
            })
        }
        else if (side === 2){
            axios({
                url:`${URL}/financial_product/search/product/${selectedType.value}/${selectedBank2.value}/`,
                method:'get'
            })
            .then(response => {
                productList2.value = response.data
                bank2.value = productList2.value[0].kor_co_nm
                console.log(`bank2 : ${bank2.value}`)
            })
            .catch(err => {
                console.log(err)
            })
        }
    }

    const getOptionList = function(side){
        if (side === 1){
            axios({
                url:`${URL}/financial_product/search/option/${selectedType.value}/${selectedProduct1.value}/`,
                method:'get'
            })
            .then(response => {
                optionList1.value = response.data
                console.log(optionList1.value)
            })
            .catch(err => {
                console.log(err)
            })
        }
        else if (side === 2){
            axios({
                url:`${URL}/financial_product/search/option/${selectedType.value}/${selectedProduct2.value}/`
            })
            .then(response => {
                optionList2.value = response.data
                console.log(optionList2.value)
            })
            .catch(err => {
                console.log(err)
            })
        }
    }

    const storeInitialize = function(){
        selectedType.value = null
        selectedBank1.value = null
        selectedBank2.value = null
        bankList.value = []
        selectedProduct1.value = null
        selectedProduct2.value = null
        productList1.value = []
        productList2.value = []
        selectedOption1.value = null
        selectedOption2.value= null
        optionList1.value = []
        optionList2.value = []
        }

    return { 
        selectedType, 
        bankList, 
        selectedBank1,
        bank1,
        selectedBank2,
        bank2,
        productList1, 
        selectedProduct1,
        product1, 
        productList2, 
        selectedProduct2,
        product2, 
        optionList1, 
        selectedOption1, 
        optionList2, 
        selectedOption2,
        option1,
        option2,
        getBankList,
        getProductList,
        storeInitialize,
        getOptionList
    }
})