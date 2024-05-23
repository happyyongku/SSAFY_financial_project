<template>
  <div class="m-3">
    <RouterLink :to="{ name: 'user-profile' }" class="custom-router-link">나의 프로필 보기</RouterLink> 
    <RouterLink :to="{ name: 'user-posts' }" class="custom-router-link">나의 게시글 보기</RouterLink>
    <h3>◎ {{ userId }}번 유저 페이지</h3>
    <hr>
    <RouterView />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const userId = ref(route.params.id)
</script>

<style scoped>
.custom-router-link {
  color: black; 
  text-decoration: none; 
  margin-right: 10px;
}

</style>