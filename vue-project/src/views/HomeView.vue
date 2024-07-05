<template>
    <div class=" d-flex flex-column align-items-center py-5">
        <section class="border w-75">
            <div class="d-flex justifiy-content-between">
                <div class="">
                    <h1 class="mt-5 ms-5" @click="testId">YG Financial</h1>
                    <h4 class="mt-5 ms-5">고객 맞춤형 금융 서비스 YG Financial</h4>
                </div>
                <div class="image-container">
                    <img src="@/assets/man_img.png" alt="man" id="man-img">
                    <img src="@/assets/woman_img.png" alt="woman" id="woman-img">
                </div>
            </div>
            <nav class="d-flex p-3 justify-content-evenly " id="nav-icon">
                <div class="flex-column text-center" @click="goToList">
                    <img src="@/assets/checklist_icon.png" alt="checklist-icon" id="icon" style="width: 100px; height: 146.25px;">
                    <p class="m-2" id="nav-icon-text">금융 상품 목록</p>
                </div>
                <div class="flex-column text-center" @click="goToCompare">
                    <img src="@/assets/product_compare_icon.png" alt="compare-icon" id="icon">
                    <p class="m-2" id="nav-icon-text">금융 상품 비교</p>
                </div>
                <div class="flex-column text-center" @click="goToExchange">
                    <img src="@/assets/exchange.png" alt="exchange-icon" id="icon">
                    <p class="m-2" id="nav-icon-text">환율 계산기</p>  
                </div>
                <div class="flex-column text-center" @click="goToBankMap">
                    <img src="@/assets/bank_map.png" alt="map-icon" id="icon">
                    <p class="m-2" id="nav-icon-text">주변 은행 검색</p>
                </div>
                <div class="flex-column text-center" @click="goToChatBot">
                    <img src="@/assets/chatbot.png" alt="chatbot-icon" id="icon">
                    <p class="m-2" id="nav-icon-text">챗봇 상담</p>
                </div>
            </nav>
        </section>
        <section class="d-flex justify-content-evenly w-75">
            <CurrentChart class="ms-3 me-3"/>
        </section>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import CurrentChart from '@/components/CurrentChart.vue'
import { useCounterStore } from '@/stores/counter.js';


const router = useRouter()
const goToList = function(){
    router.push({name:"ReadProductView"})
}
const goToCompare = function(){
    router.push({name:"CompareView"})
}
const goToExchange = function(){
    router.push({name:"ExchangeView"})
}
const goToBankMap = function(){
    router.push({name: "MapView"})
}
const goToChatBot = function(){
    router.push({name:"ChatBotView"})
}

const store = useCounterStore()
const testId = function(){
    console.log(`inform : ${store.userId}`)
    console.log(store.test)
}

</script>

<style scoped>

</style>