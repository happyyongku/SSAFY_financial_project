<template>
    <body>
        <div id="chat-container">
            <div id="chat-messages">
                <div v-for="(msg, index) in messages" :key="index" class="message">{{ msg.sender }}: {{ msg.content }}</div>
            </div>
            <div id="user-input">
                <input v-model="userMessage" @keyup.enter="sendMessage" type="text" placeholder="나에게 맞는 금융 상품을 추천해줘"/>
                <button @click="sendMessage">전송</button>
            </div>
        </div>
    </body>
    </template>
    
    <script setup>
    import axios from 'axios';
    import { ref, computed } from 'vue'
    
    const FIN_URL = 'http://127.0.0.1:8000/financial_product'
    const messages = ref([])
    const userMessage = ref('')

    const sendMessage = function(){
        messages.value.push({sender: 'user', content: userMessage.value})
        axios({
            url:`${FIN_URL}/chat/`,
            method:'get',
            params:{
                message: userMessage.value
            }
        })
        .then(response=>{
            const responseMessage =response.data
            console.log(responseMessage)
            messages.value.push({sender:'챗봇', content: responseMessage})
        })
        .catch(error => {
            console.log(error)
        })
        userMessage.value = null
    }
    
    

    </script>
    
    <style scoped>
    body {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
    }
    .message {
        border-top: 1px solid #ccc;
        padding: 10px;
        margin-top: 5px;
        background-color: #e6e6e6;
    }
    #chat-container {
        width: 400px;
        height: 600px;
        display: flex;
        flex-direction: column;
        border: 1px solid #ccc;
    }
    #chat-messages {
        flex: 1;
        overflow-y: auto;
        padding: 10px;
        display: flex;
        flex-direction: column;
    }
    #user-input {
        display: flex;
        padding: 10px;
    
    }
    #user-input input {
        flex: 1;
        padding: 10px;
        outline: none;
    }
    #user-input button {
        border: none;
        background-color: #1e88e5;
        color: white;
        padding: 10px 15px;
        cursor: pointer;
    }
    </style>