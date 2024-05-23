<template>
  <div class="table-container">
    <h3>상품 유형 선택</h3>
    <div class="options">
      <div class="option" @click="$emit('typeSelect', 'deposit')">
        정기 예금
      </div>
      <div class="option" @click="$emit('typeSelect', 'installment')">
        적금
      </div>
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
  width: 100%;
  max-width: 100%;
  max-height: 400px;
  overflow: auto;
  border: 1px solid #ddd;
  padding-bottom: 10px;
  text-align: center;
  background-color: #8C7C68;

}

.options {
  display: flex;
  justify-content: space-between;
  padding: 10px;
}

.option {
  cursor: pointer;
  padding: 10px;
  flex: 1;
  text-align: center;
  margin-right: 10px;
  font-family: 'Century Gothic', sans-serif; 

}

.option:last-child {
  margin-right: 0;
}

div {
  font-family: 'Century Gothic', sans-serif; 
}
</style>