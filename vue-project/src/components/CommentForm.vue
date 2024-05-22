<template>
    <div>
      <h1>Comment Form</h1>
      <form @submit.prevent="submitComment">
        <div>
          <label for="content">Content:</label>
          <input type="text" v-model="content" id="content" required>
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  import { useCounterStore } from '@/stores/counter';
  import axios from 'axios';
  
  const store = useCounterStore();
  const route = useRoute();
  const router = useRouter();
  const content = ref('');
  
  const submitComment = () => {
    axios({
      method: 'post',
      url: `${store.API_URL}/articles/${route.params.id}/comments/`,
      headers: {
        Authorization: `Token ${store.token}`,
      },
      data: {
        content: content.value,
      },
    })
      .then(() => {
        store.getComments(route.params.id);
        comments.value = store.comments;
        router.push({ name: 'DetailView', params: { id: route.params.id } });
      })
      .catch((error) => {
        console.log(error);
      });
  };
  </script>
  
  <style>
  </style>
  