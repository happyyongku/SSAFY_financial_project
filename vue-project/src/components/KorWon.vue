<template>
    <div>
        <h4>대한민국 원</h4>
        <div >
            <input type="number" @input="changeWonValue" v-model="korWon" 
            placeholder="환전 할 금액" v-if="type==='sell'">
            <p v-if="type==='buy'">{{result}}</p> 
            KRW
            
        </div>
    </div>
</template>

<script setup>
    import { ref } from 'vue';
    defineProps({
        type:String,
        result:Number
    })

    const korWon = ref(null)
    const emit = defineEmits(['changeKorWon', 'calculate'])

    const changeWonValue = function(){
        emit('changeKorWon', korWon.value)
        emit('calculate')
    }
</script>

<style scoped>

</style>