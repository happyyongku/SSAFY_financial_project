<template>
    <div>
      <h1>Edit Article</h1>
      <form @submit.prevent="updateArticle">
        <div>
          <label for="title">Title:</label>
          <input type="text" v-model="title" id="title" required>
        </div>
        <div>
          <label for="content">Content:</label>
          <textarea v-model="content" id="content" required></textarea>
        </div>
        <button type="submit">Update</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  import { useCounterStore } from '@/stores/counter';
  import axios from 'axios';
  
  const store = useCounterStore();
  const route = useRoute();
  const router = useRouter();
  const title = ref('');
  const content = ref('');
  
  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.API_URL}/articles/${route.params.id}/`,
      headers: {
        Authorization: `Token ${store.token}`,
      },
    })
      .then((response) => {
        title.value = response.data.title;
        content.value = response.data.content;
      })
      .catch((error) => {
        console.log(error);
      });
  });
  
  const updateArticle = () => {
    axios({
      method: 'put',
      url: `${store.API_URL}/articles/${route.params.id}/`,
      headers: {
        Authorization: `Token ${store.token}`,
      },
      data: {
        title: title.value,
        content: content.value,
      },
    })
      .then(() => {
        router.push({ name: 'DetailView', params: { id: route.params.id } });
      })
      .catch((error) => {
        console.log(error);
      });
  };
  </script>
  
  <style>
  </style>
  