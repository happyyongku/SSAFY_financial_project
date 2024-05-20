<template>
    <body>
        <div id="chat-container">
            <div id="chat-messages">
                <div v-for="(msg, index) in messages" :key="index" class="message">{{ msg.sender }}: {{ msg.content }}</div>
            </div>
            <div id="user-input">
                <input v-model="userMessage" @keyup.enter="sendMessage" type="text" placeholder="나에게 맞는 금융 상품을 추천해줘" />
                <button @click="sendMessage">전송</button>
            </div>
        </div>
    </body>
    </template>
    
    <script setup>
    import { ref } from 'vue'
    
    const FIN_URL = 'http://127:0.0.1:8000/financial_product'
    const messages = ref([])
    const userMessage = ref('')
    
    const OPENAI_API_KEY = import.meta.env.VITE_API_KEY_GPT
    
    // Django API에서 예금 상품 정보 가져오기
    async function fetchDepositProducts(){
        try {
            const response = await fetch(`${FIN_URL}/fetch/product/deposit/`)
            return await response.json()
        }
        catch(error){
            console.error('예금 상품 정보를 가져오는 중 오류 발생', error)
            return []
        }
    }
    // Django API에서 적금 상품 정보 가져오기
    async function fetchInstallmentProducts() {
        try{
            const response = await fetch(`${FIN_URL}/fetch/product/installment/`)
            return await response.json()
        }
        catch(error){
            console.error('적금 상품 정보를 가져오는 중 오류 발생', error)
            return []
        }
    }

    // ChatGPT API 요청
    async function fetchAIResponse(prompt) {
        // API 엔드포인트 주소
        const apiEndpoint = 'https://api.openai.com/v1/chat/completions';
        const apiKey = OPENAI_API_KEY;
        
      // 대화 히스토리를 저장할 배열
        let chatHistory = []
    
      // 특정 문장에 비슷한 응답을 하도록 지침 추가
        const fixedPrompts = {
            //-----------------------
            "금융 상품을 추천해줘":"사용자가 '금융 상품을 추천해줘'와 비슷하게 물어보면 '물론이죠! 정기 예금과 적금 중에 선택해주세요!'로 대답해줘."
        }
    
        let adjustedPrompt = prompt
        
        if (fixedPrompts[prompt]) {
            adjustedPrompt = fixedPrompts[prompt];
        } else {
            adjustedPrompt = `챗봇: 당신은 금리비교 사이트 YG 에서 금융상품을 알려주는 챗봇입니다(은행이 아닙니다). "${prompt}"에 적절히 짧게 답하고, 예적금 상품에 대해서 알려주면 잘 대답해주겠다고 해주세요. 또 금리 비교 하면서 적절한 상품을 알아보라고 홍보해주세요!(홍보는 한번만 해주세요.) 그리고 모든 답변은 100자 이내로 줄여서 답해주세요.`
        }
        
      // 히스토리 배열에 현재 메시지 추가
        chatHistory.push({ role: "user", content: adjustedPrompt });
        
        // API 요청에 사용할 옵션을 정의
        const requestOptions = {
            method: 'POST',
            // API 요청의 헤더를 설정
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${apiKey}`
            },
            body: JSON.stringify({
                model: "gpt-3.5-turbo",  // 사용할 AI 모델
                messages: chatHistory,  // 대화 히스토리 포함
                temperature: 0.6, // 모델의 출력 다양성
                max_tokens: 300, // 응답받을 메시지 최대 토큰(단어) 수 설정
                top_p: 1, // 토큰 샘플링 확률을 설정
                frequency_penalty: 0.5, // 일반적으로 나오지 않는 단어를 억제하는 정도
                presence_penalty: 0.5, // 동일한 단어나 구문이 반복되는 것을 억제하는 정도
                stop: ["Human"], // 생성된 텍스트에서 종료 구문을 설정
            }),
        };
      // API 요청후 응답 처리
        try {
            const response = await fetch(apiEndpoint, requestOptions);
            const data = await response.json();
            const aiResponse = data.choices[0].message.content;
            // 히스토리에 AI 응답 추가
            chatHistory.push({ role: "assistant", content: aiResponse });
            console.log(aiResponse)

            if (aiResponse.includes('예금')) {
                const products = await fetchDepositProducts()
                return `추천 예금 상품: ${products.map(p => p.name).join(', ')}`
            }
            else if (aiResponse.includes('적금')){
                const products = await fetchInstallmentProducts()
                return `추천 적금 상품: ${products.map(p=> p.name).join(', ')}`
            }

            return aiResponse;
        } catch (error) {
        console.error('OpenAI API 호출 중 오류 발생:', error);
            return 'OpenAI API 호출 중 오류 발생';
        }
    }
    
    function addMessage(sender, message) {
        messages.value.unshift({ sender, content: message });
    }
    
    function sendMessage() {
        const message = userMessage.value.trim();
        if (message.length === 0) return;
        
        addMessage('나', message);
        userMessage.value = '';
        
        fetchAIResponse(message).then(aiResponse => {
            addMessage('챗봇', aiResponse);
        });
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
        flex-direction: column-reverse;
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