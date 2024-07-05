<template>
  <div class="ms-5">
    <h1>User Posts</h1>
    <div v-if="userPosts.length > 0">
      <ul>
        <li v-for="post in userPosts" :key="post.id">
          <h3 class="noto">제목: {{ post.title }}</h3>
          <p class="noto">내용: {{ post.content }}</p>
          <p class="noto">작성일: {{ post.created_at }}</p>
        </li>
      </ul>
    </div>
    <div v-else>
      <h3>작성한 게시글이 없습니다.</h3>
    </div>
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
const userId = computed(() => {
  return store.userId
})

onMounted(() => {
  // 유저가 작성한 게시글을 가져오는 API 요청
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/article/articles/user/${store.userId}/`, // 유저가 작성한 게시글을 가져오는 엔드포인트로 수정 필요
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
.noto {
    font-family: "Noto Sans KR", sans-serif;
    font-optical-sizing: auto;
    font-style: normal;
    }
</style>
