<template>
    <div class="table-container">
        <table>
            <thead style="border:1px solid">
                <tr>
                    <th v-for="key in keys" :key="key" style="border:1px solid">
                        {{ headers[key] }}
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(item, index) in items" :key="index">
                    <td v-for="key in keys" :key="key">{{ item[key] }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue';
import { useFinancialStore } from '@/stores/financial';
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';
import App from '../App.vue'


const store = useFinancialStore()
const counterStore = useCounterStore()
const token = computed(()=>{
    return counterStore.token
})

const items = ref([])

onMounted(() => {
    store.readType = 'deposit'
    fetchInitialData()
})

const fetchInitialData = async () => {

    try {
        console.log(token)
        await axios({
            url:`http://127.0.0.1:8000/financial_product/read_product/deposit/`,
            method: 'get',
            headers: {
            Authorization: `Token ${token.value}`
            }
        })
        .then(response => {
            store.readTable = response.data
            items.value = store.readTable
        })
        .catch(err => {
            console.log(err)
        })
    }
    catch (error){
        console.log('ss')
        console.log(error)
    }
    
}

const keys = [
    'kor_co_nm',
    'fin_prdt_cd',
    'fin_prdt_nm',
    'rate_1',
    'rate_3',
    'rate_6',
    'rate_12',
    'rate_24',
    'rate_36'
]
const headers = {
    kor_co_nm: '은행',
    fin_prdt_cd: '상품 코드',
    fin_prdt_nm: '상품명',
    rate_1: '1개월',
    rate_3: '3개월',
    rate_6: '6개월',
    rate_12: '12개월',
    rate_24: '24개월',
    rate_36: '36개월'
}

</script>

<style scoped>
.table-container {
    width: 100%;
    max-width: 100%;
    max-height: 400px;
    overflow: auto;
    border: 1px solid #ddd;
    padding-bottom: 10px;
    
}
table {
    width: 100%;
    border-collapse: collapse;
    padding-right:10px;
    padding-left: 10px;
}
th, td {
    padding: 8px, 12px;
    border: 1px solid;
    text-align: center;
    white-space-collapse: nowrap;
}
thead th {
    position:sticky;
    top:0;
    background-color: #f9f9f9;
    z-index: 1;
}
thead tr {
    border: 1px solid;
    margin-left: 5px;
    margin-right: 5px
}

</style>