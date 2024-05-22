<template>
  <div>
    <h1>User Posts</h1>
    <ul>
      <li v-for="post in userPosts" :key="post.id">
        <h2>{{ post.title }}</h2>
        <p>{{ post.content }}</p>
        <p>작성일: {{ post.created_at }}</p>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore();
const userPosts = ref([]);
const token = computed(()=>{
    return store.token
})

onMounted(() => {
  // 유저가 작성한 게시글을 가져오는 API 요청
  axios({
    method: 'get',
    url: `${store.API_URL}/user-posts/`, // 유저가 작성한 게시글을 가져오는 엔드포인트로 수정 필요
    headers: {
      Authorization: `Token ${token.value}`,
    },
  })
    .then((response) => {
      userPosts.value = response.data;
    })
    .catch((error) => {
      console.error('Error fetching user posts:', error);
    });
});
</script>

<style scoped>
/* 스타일링 추가 */
</style>
