// Django API에서 예금 상품 가져오기
async function fetchDepositProducts() {
    try {
        const response = await fetch('http://your-django-api-endpoint/deposit-products/');
        return await response.json();
    } catch (error) {
        console.error('예금 상품을 가져오는 중 오류 발생:', error);
        return [];
    }
}

// Django API에서 적금 상품 가져오기
async function fetchInstallmentProducts() {
    try {
        const response = await fetch('http://your-django-api-endpoint/installment-products/');
        return await response.json();
    } catch (error) {
        console.error('적금 상품을 가져오는 중 오류 발생:', error);
        return [];
    }
}
async function fetchAIResponse(prompt) {
    const apiEndpoint = 'https://api.openai.com/v1/chat/completions';
    const apiKey = OPENAI_API_KEY;
    let chatHistory = [];

    const fixedPrompts = {
        "금융 상품을 추천해줘": "사용자가 '금융 상품을 추천해줘'와 비슷하게 물어보면 '물론이죠! 정기 예금과 적금 중에 선택해주세요!'로 대답해줘."
    };

    let adjustedPrompt = prompt;
    if (fixedPrompts[prompt]) {
        adjustedPrompt = fixedPrompts[prompt];
    } else {
        adjustedPrompt = `챗봇: 당신은 금리비교 사이트인 'INTERESTing'에서 금융상품을 알려주는 챗봇입니다(은행이 아닙니다). "${prompt}"에 적절히 짧게 답하고, 예적금 상품에 대해서 알려주면 잘 대답해주겠다고 해주세요. 또 금리 비교 하면서 적절한 상품을 알아보라고 홍보해주세요!(홍보는 한번만 해주세요.) 그리고 모든 답변은 100자 이내로 줄여서 답해주세요.`;
    }

    chatHistory.push({ role: "user", content: adjustedPrompt });

    const requestOptions = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${apiKey}`
        },
        body: JSON.stringify({
            model: "gpt-3.5-turbo",
            messages: chatHistory,
            temperature: 0.6,
            max_tokens: 300,
            top_p: 1,
            frequency_penalty: 0.5,
            presence_penalty: 0.5,
            stop: ["Human"],
        }),
    };

    try {
        const response = await fetch(apiEndpoint, requestOptions);
        const data = await response.json();
        const aiResponse = data.choices[0].message.content;

        chatHistory.push({ role: "assistant", content: aiResponse });

        // 예금 또는 적금 상품을 추천하는 로직 추가
        if (aiResponse.includes('정기 예금')) {
            const products = await fetchDepositProducts();
            return `추천 예금 상품: ${products.map(p => p.name).join(', ')}`;
        } else if (aiResponse.includes('적금')) {
            const products = await fetchInstallmentProducts();
            return `추천 적금 상품: ${products.map(p => p.name).join(', ')}`;
        }

        return aiResponse;
    } catch (error) {
        console.error('OpenAI API 호출 중 오류 발생:', error);
        return 'OpenAI API 호출 중 오류 발생';
    }
}
