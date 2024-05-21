<template>
    <div class="d-flex flex-column align-items-center py-5">
        <div class="border w-75">
            <h3 class="m-3">YG Financial</h3>
            <nav class="d-flex p-3 justify-content-evenly">
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
        </div>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter()
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

</script>

<style scoped>

</style>