<template>
    <div>
        <h2>현재 환율</h2>
        <div class="table-container">
            <table>
                <thead style="border:1px solid">
                    <tr>
                        <th v-for="key in keys" :key="key" style="border:1px solid">
                            {{ headers[key] }}
                        </th>
                    </tr>
                </thead>
                <tbody v-if="items">
                    <tr v-for="(item, index) in items" :key="index">
                        <td v-for="key in keys" :key="key">{{ item[key] }}</td>
                    </tr>
                </tbody>
                <tbody v-else>
                    <h3>오늘의 환율 정보가 없습니다.</h3>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { useFinancialStore } from '@/stores/financial';
import { onMounted, ref, computed } from 'vue';
import axios from 'axios';

const counterStore = useCounterStore()
const financialStore = useFinancialStore()

const token = computed(() => {
    return counterStore.token
})
const keys = [
    'cur_nm',
    'cur_unit',
    'ttb',
    'tts',
    'deal_bas_r'
]

const headers = {
    'cur_nm': '화폐 명',
    'cur_unit': '화폐',
    'ttb': '사실 때',
    'tts': '파실 때',
    'deal_bas_r': '매매 기준율'
}

const items = ref('')

onMounted(async () => {
    await axios({
        url: 'http://127.0.0.1:8000/financial_product/fetch/exchange/',
        method: 'get',
        headers: {
            Authorization: `Token ${token.value}`
        }
    })
    .then(response => {
        items.value = response.data
        console.log(items.value)
    })
    .then(response => {

    })
    .catch(error => {
        console.log(error)
    })
})

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
    background-color: #faedad;
}
thead tr {
    border: 1px solid;
    margin-left: 5px;
    margin-right: 5px
}

</style>