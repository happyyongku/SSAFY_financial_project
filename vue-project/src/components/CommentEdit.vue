<template>
  <div>
    <h1>Edit Comment</h1>
    <form @submit.prevent="updateComment">
      <div>
        <label for="content">Content:</label>
        <input type="text" v-model="content" id="content" required>
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
const content = ref('');

onMounted(() => {
axios({
  method: 'get',
  url: `${store.API_URL}/comments/${route.params.id}/`, // 수정된 부분
  headers: {
    Authorization: `Token ${store.token}`,
  },
})
  .then((response) => {
    content.value = response.data.content;
  })
  .catch((error) => {
    console.log(error);
  });
});

const updateComment = () => {
axios({
  method: 'put', // HTTP 요청 방식 변경
  url: `${store.API_URL}/comments/${route.params.id}/`, // 수정된 부분
  headers: {
    Authorization: `Token ${store.token}`,
  },
  data: { // 수정된 부분: 댓글의 수정된 내용을 요청 본문에 포함
    content: content.value,
  },
})
  .then(() => {
    router.push({ name: 'DetailView', params: { id: route.params.articleId } });
  })
  .catch((error) => {
    console.log(error);
  });
};
</script>

<style>
</style>
