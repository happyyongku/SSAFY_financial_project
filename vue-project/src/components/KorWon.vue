<template>
    <div>
        <h4 class="noto">대한민국 원</h4>
        <div >
            <input type="number" @input="changeWonValue" v-model="korWon" 
            placeholder="환전 할 금액" v-if="type==='sell'">
            KRW
            <p v-if="type==='buy'">{{result}}</p> 
            
        </div>
    </div>
</template>

<script setup>
    import { ref } from 'vue';
    // const apiKey = import.meta.env.VITE_API_KEY_GPT
    defineProps({
        result:Number,
        type: String,
        result:Number,
    })

    const korWon = ref(null)
    const emit = defineEmits(['changeKorWon', 'calculate'])

    const changeWonValue = function(){
        emit('changeKorWon', korWon.value)
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