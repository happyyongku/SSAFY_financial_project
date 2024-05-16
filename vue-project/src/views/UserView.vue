<template>
  <div>
    <RouterLink :to="{ name: 'user-profile' }" class="custom-router-link">Profile</RouterLink> 
    <RouterLink :to="{ name: 'user-posts' }" class="custom-router-link">Posts</RouterLink>
    <h1>유저 페이지</h1>
    <h2>{{ userId }}번 user 페이지</h2>
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