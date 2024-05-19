<template>
  <div>
    <h1>UserPosts</h1>
    <div v-if="posts.length">
      <div v-for="post in posts" :key="post.id" class="post-card">
        <h2>{{ post.title }}</h2>
        <p>{{ post.content }}</p>
        <RouterLink :to="{ name: 'DetailView', params: { id: post.id } }">Read more</RouterLink>
      </div>
    </div>
    <div v-else>
      <p>No posts found.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRoute } from 'vue-router';
import { useCounterStore } from '@/stores/counter';

const route = useRoute();
const store = useCounterStore();
const posts = ref([]);

const fetchUserPosts = () => {
  axios({
    method: 'get',
    url: `${store.API_URL}/articles/?user=${route.params.id}`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((response) => {
      posts.value = response.data;
    })
    .catch((error) => {
      console.log(error);
    });
};

onMounted(() => {
  fetchUserPosts();
});
</script>

<style scoped>
.post-card {
  border: 1px solid #ccc;
  padding: 15px;
  margin: 10px;
  border-radius: 5px;
}
</style>
