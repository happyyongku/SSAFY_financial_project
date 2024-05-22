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
    const counterStore = useCounterStore()
        const token = computed(()=>{
            return counterStore.token
        })
    const readTable = ref([])
    const readType = ref('deposit')
    const FIN_URL = 'http://127.0.0.1:8000/financial_product'

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
                method:'get',
                headers: {
                    Authorization: `Token ${token.value}`
                    }
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
                method:'get',
                headers: {
                    Authorization: `Token ${token.value}`
                    }
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
                method:'get',
                headers: {
                    Authorization: `Token ${token.value}`
                    }
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
                url:`${URL}/financial_product/search/option/${selectedType.value}/${selectedProduct2.value}/`,
                method:'get',
                headers: {
                    Authorization: `Token ${token.value}`
                    }
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

    const productRead = function(type){
        console.log('start')
        axios({
            url: `${FIN_URL}/read_product/${type}/`,
            method:'get',
            headers: {
                Authorization: `Token ${token.value}`
                }
        })
        .then(response => {
            console.log(response.data)
            console.log('aa')
            readTable.value = response.data
        })
        .catch(error => {
            console.log(`error : ${error}`)
        })
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
        readTable,
        readType,
        getBankList,
        getProductList,
        storeInitialize,
        getOptionList,
        productRead
    }
})

export const useExchangeStore = defineStore('exchange', () => {
    const currentExchange = ref([]) // 해당 날짜의 환율 정보
    const targetDate = ref('0000-00-00')
    const currentDate = ref(null)
    const tradeType = ref('sell')
    const dateList = ref([])
    const URL = 'http://127.0.0.1:8000'
    const token= ref(useCounterStore().token)
    const korWon = ref(null)
    const tradeMoney = ref(null)
    const tradeCurrent = ref(null)
    const selectedCurrent = ref(null)
    const result = ref(null)
    
    const getToday = function(){
        const today = new Date()
        const formattedToday = today.getFullYear() + '-' + (today.getMonth()+1) + '-' + today.getDate()
        currentDate.value = formattedToday
        console.log(currentDate.value)
    }
    const switchTrade = function(){
        tradeType.value = tradeType.value === 'buy' ? 'sell':'buy'
        console.log('switch')
    }

    const getTargetRate = function(target){
        axios({
            url:`${URL}/financial_product/get_rate/${target}/`,
            method:'get',
            headers: {
                Authorization: `Token ${token.value}`
                }
        })
        .then(response => {
            currentExchange.value = response.data
        })
    }

    const getDateList = function(){
        for (let i=-1; i<30; i++){
            const curDate = new Date(currentDate.value)
            curDate.setDate(curDate.getDate() - i)
            dateList.value.push(curDate.toISOString().split('T')[0])
            }
            console.log(dateList.value)
        return dateList
    }
    const initialize = function(){
        korWon.value = null
        tradeMoney.value = null
        result.value = null
        tradeCurrent.value = null
    }

    return {
        currentDate,
        targetDate,
        currentExchange,
        tradeType,
        dateList,
        korWon,
        tradeCurrent,
        selectedCurrent,
        result,
        tradeMoney,
        getDateList,
        getToday,
        getTargetRate,
        getDateList,
        switchTrade,
        initialize
    }
})