<template>
  <div>
    <h1>예적금 금리 비교</h1>
    <form>
      <select id="bank" @select.prevent>
        <option value="" disabled>Select Bank</option>
        <option value=""></option>
      </select>
    </form>
  </div>
</template>

<script setup>
  import { useFinancialStore } from '@/stores/financial';
  import { ref, computed } from 'vue'
  const store = useFinancialStore()
  const search_params = ref({
    'search_type': null,
    'target_bank': null,
    'target_product': null,
  })
  

</script>

<style scoped>

</style>