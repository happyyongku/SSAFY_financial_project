<template>
    <div class="m-3">
        <h1>환율 계산</h1>
        <div class="border border-3 p-3">
            <h3 v-if="store.tradeType==='sell'">TTS</h3>
            <h3 v-if="store.tradeType==='buy'">TTB</h3>
            <div class="m-3">
                <form @submit.prevent="changeRate">
                    <select id="selectDate" @change="changeDate($event)" v-model="selectedDate">
                        <option v-for="date in store.dateList" :value="date">{{ date }}</option>
                    </select>
                    <input type="submit" value="날짜 선택">
                </form>
            </div>
            <div class="d-flex justify-content-evenly">
                <KorWon v-if="store.tradeType==='sell'"
                @changeKorWon="updateKorWon"
                @calculate="calculate"
                :type="store.tradeType"
                :result="store.result"
                />
                <CurrentList v-if="store.tradeType==='buy'"
                :rate-list="store.currentExchange"
                :type="store.tradeType"
                :result="store.result"
                @updateCurrent="updateCurrent"
                @changeTradeMoney="updateTradeMoney"
                @calculate="calculate"
                />
                <button @click="switching">switch</button>
                <KorWon v-if="store.tradeType==='buy'"
                :type="store.tradeType"
                :result="store.result"
                @changeKorWon="updateKorWon"
                />
                <CurrentList v-if="store.tradeType==='sell'"
                :rate-list="store.currentExchange"
                :type="store.tradeType"
                :result="store.result"
                @updateCurrent="updateCurrent"
                @changeTradeMoney="updateTradeMoney"
                @calculate="calculate"
                />
            </div>
        </div>
    </div>
</template>

<script setup>
    import { useExchangeStore } from '@/stores/financial';
    import { onMounted, ref } from 'vue';
    import KorWon from '@/components/KorWon.vue'
    import CurrentList from '@/components/CurrentList.vue'

    const store = useExchangeStore()
    const selectedDate = ref('')
    const changeDate = (event)=>{
        selectedDate.value = event.target.value
        console.log(selectedDate.value)
    }
    const changeRate = ()=>{
        store.getTargetRate(selectedDate.value)
    }
    const updateKorWon = (won) => {
        store.korWon = won
        console.log(store.korWon)
    }
    const calculate = function(){
        console.log(store.tradeCurrent)
        const current = store.tradeCurrent
        const tts = ref(null)
        const ttb = ref(null)
        if (!current) {
            alert('환전할 대상을 선택해 주십시오')
            return
        }
        if (current.cur_unit==='KRW') {
            alert('다른 대상을 선택해 주십시오')
            console.log('nope')
            return
        }
        else {
            if (current.cur_unit.includes('100')){
                tts.value = (100/current.tts).toFixed(8)
                ttb.value = current.ttb/100
            }
            else {
                tts.value = (1/current.tts).toFixed(8)
                ttb.value = current.ttb
            }
        }
        if (store.tradeType==='sell'){
            store.result = Number((store.korWon * tts.value).toFixed(3))
        }
        else if (store.tradeType==='buy') {
            store.result = Number((store.tradeMoney * ttb.value).toFixed(3))
        }
        
    }
    const updateCurrent = (current) => {
        store.tradeCurrent = current
        console.log(store.tradeCurrent)
    }
    const switching = function(){
        store.switchTrade()
        store.initialize()
    }
    const updateTradeMoney = function(input){
        store.tradeMoney = input
        console.log(`trade : ${store.tradeMoney}`)
    }


</script>

<style scoped>

</style>