<template>
  <div>
    <h1>DetailView</h1>
    <div v-if="article">
      <p>{{ article.id }}</p>
      <p>{{ article.title }}</p>
      <p>{{ article.content }}</p>
    </div>
    <div v-if="comments.length">
      <h2>Comments</h2>
      <div v-for="comment in comments" :key="comment.id" class="comment-card">
        <p>{{ comment.content }}</p>
        <p>by {{ comment.author }}</p>
      </div>
    </div>
    <div v-else>
      <p>No comments found.</p>
    </div>
    <button @click="goToEdit">수정</button>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';

const store = useCounterStore();
const route = useRoute();
const router = useRouter();
const article = ref(null);
const comments = ref([]);

const goToEdit = () => {
  router.push({ name: 'ArticleEdit', params: { id: article.value.id } });
};

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/articles/${route.params.id}/comments/`
  })
    .then((response) => {
      article.value = response.data;
    })
    .catch((error) => {
      console.error('Error fetching article:', error);
    });

  store.getComments(route.params.id);
  comments.value = store.comments;
});
</script>

<style>
.user-posts {
  text-align: center;
  padding: 20px;
}
.post-card, .comment-card {
  border: 1px solid #ccc;
  padding: 15px;
  margin: 10px;
  border-radius: 5px;
}
</style>
