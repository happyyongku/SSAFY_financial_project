<template>
  <div class="table-container">
    <h3 class="noto">상품 유형 선택</h3>
    <div class="option-container">
      <button class="option" @click="$emit('typeSelect', 'deposit')">
        정기 예금
      </button>
      <button class="option" @click="$emit('typeSelect', 'installment')">
        적금
      </button>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
h3 {
  font-family: Georgia, serif;
}

.table-container {
  max-height: 400px;
  overflow: auto;
  border: 1px solid #ddd;
  padding-bottom: 10px;
  padding-top: 20px;
  text-align: center;
  background-color: #8C7C68;
  font-family: Arial, sans-serif;
}

.option-container {
  display: flex;
  justify-content: space-evenly;
  padding: 10px;
}

.option {
  cursor: pointer;
  padding: 10px;
  width: 300px; /* 버튼의 너비를 줄이기 위해 설정 */
  text-align: center;
  margin-right: 10px;
  font-family: 'Century Gothic', sans-serif;
}

.option:last-child {
  margin-right: 0;
}

.noto {
  font-family: "Noto Sans KR", sans-serif;
  font-optical-sizing: auto;
  font-style: normal;
}
</style>
