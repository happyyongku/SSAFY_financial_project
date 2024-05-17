import { ref, computed } from 'vue'
import { defineStore} from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter.js'



export const useFinancialStore = defineStore('financial', () => {
    const selectedType = ref(null)
    const bankList = ref([])
    const selectedBank = ref(null)
    const productList = ref([])
    const selectedProduct = ref(null)
    const optionList = ref([])
    const selectedOption = ref(null)
    const URL = 'http://127.0.0.1:8000'
    // const token = ref(counter.token)
    const token= ref(useCounterStore().token)
    const searchData = function(){
        axios({
            url : `${URL}/financial_product/search/`,
            method: 'get',
            params:{
                'search_type':selectedType.value,
                'target_bank': selectedBank.value,
                'target_product': selectedProduct.value,
                'target_option': selectedOption.value
            }
        })
        .then((response) => {
            console.log(response)
        })
        .catch(err => {
            console.log(err)
        })
    }
    const getBankList = function(){
        console.log(token)
        axios({
            url: `${URL}/financial_product/search/bank/`,
            method:'get',
            headers: {
                Authorization: `Token ${token.value}`
                }
        })
        .then(response => {
            bankList.value = response.data
            console.log(bankList.value)
        })
        .catch(err => {
            console.log(err)
        })
    }

    return { selectedType, bankList, selectedBank, productList, selectedProduct, optionList, selectedOption, searchData, getBankList}
})