<template>
  <div class="d-flex justify-content-center">
    <div class="mt-3">
      <RouterLink :to="switching==='fold'?{ name: 'user-posts' }:{name:'UserView'}" 
      class="custom-router-link" @click="switchRouter">{{ postText }}</RouterLink>
      <h3 class="noto mt-3">유저 프로필 페이지</h3>
      <hr>
      <div class="d-flex">
        <UserProfile/>
        <RouterView/>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, computed } from 'vue'
import { useRoute } from 'vue-router'
import UserProfile from '@/components/UserProfile.vue';

const route = useRoute()
const userId = ref(route.params.id)

const switching = ref('fold')

const switchRouter = () => {
  switching.value = switching.value === 'fold'? 'expand': 'fold'
  console.log(switching.value)
}

const postText = computed(() => {
  if (switching.value === 'fold'){
    return '나의 게시글 보기'
  }
  else if (switching.value === 'expand'){
    return '작성글 접기'
  }
})


</script>

<style scoped>
.custom-router-link {
  color: black; 
  text-decoration: none; 
  margin-right: 10px;
}

.noto {
    font-family: "Noto Sans KR", sans-serif;
    font-optical-sizing: auto;
    font-style: normal;
}


</style>