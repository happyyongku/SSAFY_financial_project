<template>
    <div>
        <h4 v-if="!selectedCurrent" class="noto">환전 할 대상</h4>
        <h4 v-if="selectedCurrent" class="noto">{{ selectedCurrent.cur_nm }}</h4>
        <div class="my-2">
            <select id="selectCurrent" @change="selected($event)">
                <option value="" disabled selected v-if="!selectedCurrent">선택된 대상이 없습니다.</option>
                <option v-for="current in rateList" :value="current" class="noto">
                    <p class="noto">
                        {{ current.cur_nm }} {{ current.cur_unit }}
                    </p>
                </option>
            </select>
        </div>
        <div class="my-2">
            <input type="number" @input="changeCurrent" v-model="tradeMoney"    
            placeholder="환전 할 금액" v-if="type==='buy'">
            <div v-if="type==='sell'">
                <p>{{result}}</p>
            </div>
        </div>
        <div v-if="tradeCurrent">
            <p class="noto">거래 기준율: {{ tradeCurrent.deal_bas_r }}</p>
            <p v-if="type==='sell'" class="noto">환전 비율: {{ tradeCurrent.tts }}</p>
            <p v-if="type==='buy'" class="noto">환전 비율: {{ tradeCurrent.ttb }}</p>
        </div>
    </div>
</template>

<script setup>
    import { ref } from 'vue';
    const props = defineProps({
        rateList:Object,
        type: String,
        result:Number,
        tradeCurrent: Object
    })
    const selectedCurrent = ref(null)
    const tradeMoney = ref(null)

    const emit = defineEmits(['changeTradeMoney', 'calculate', 'updateCurrent'])

    const selected = function(event){
        const selectedIdx = event.target.selectedIndex
        selectedCurrent.value = props.rateList[selectedIdx]
        emit('updateCurrent', selectedCurrent.value)
        if (tradeMoney.value){
            emit('calculate')
        }
    }

    const changeCurrent = function(){
        emit('changeTradeMoney', tradeMoney.value)
        emit('calculate')
    }
</script>

<style scoped>
.noto {
    font-family: "Noto Sans KR", sans-serif;
    font-optical-sizing: auto;
    font-style: normal;
    }

</style>