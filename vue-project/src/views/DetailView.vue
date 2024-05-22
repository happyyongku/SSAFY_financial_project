<template>
  <div>
    <h1>DetailView</h1>
    <div v-if="article">
      {{ article }}
      {{ article.user }}
      <p>{{ article.id }}</p>
      <p>{{ article.title }}</p>
      <p>{{ article.content }}</p>
    </div>
    <div v-if="comments.length > 0">
      <h2>Comments</h2>
      <div v-for="comment in comments" :key="comment.id" class="comment-card">
        <p>{{ comment.content }}</p>
        <p>by {{ comment.author }}</p>
      </div>
    </div>
    <div v-else>
      <p>No comments found.</p>
    </div>
    <button @click="switchEdit" 
    v-if="!editType && (article?.user === store.userInfo.pk)"
    >수정</button>
    <div class="w-50">
      <ArticleEdit v-if="editType" :article-id="article.id" @switchType="switchEdit"/>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';
import ArticleEdit from '@/components/ArticleEdit.vue';

const store = useCounterStore();
const route = useRoute();
const router = useRouter();
const article = ref(null);
const comments = ref([]);
const editType = ref(false)
const token = computed(()=>{
  return store.token
})
const API_URL = 'http://127.0.0.1:8000'

const props = defineProps({
  articleItem:Object
})

const switchEdit = () => {
  editType.value = editType.value === true? false:true
};


onMounted(() => {
  console.log('dd')
  axios({
    method: 'get',
    url: `${API_URL}/article/articles/${route.params.id}/comments/`,
    headers: {
      Authorization:`Token ${token.value}`
    }
  })
    .then((response) => {
      comments.value = response.data;
    })
    .catch((error) => {
      console.error('Error fetching article:', error);
    });
  axios({
    url: `${API_URL}/article/articles/${route.params.id}/`,
    method:'get',
    headers: {
      Authorization:`Token ${token.value}`
    }
  })
  .then(response => {
    console.log(response)
    article.value = response.data
  })
  .catch(error => {
    console.log(`article error : ${error}`)
  })
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
