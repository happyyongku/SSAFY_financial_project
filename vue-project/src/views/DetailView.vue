<template>
  <div class="m-4">
    <h1 class="noto">게시글 상세보기</h1>
    <div v-if="article" class="my-3">
      <p>{{ article.id }}번 게시글</p>
      <p>제목: {{ article.title }}</p>
      <p>내용: {{ article.content }}</p>
    </div>
    <div v-if="comments.length > 0">
      <h2>Comments</h2>
      <div class="comment-card">
        <ul v-for="comment in comments" :key="comment.id" >
          <li>{{ comment.content }}</li>
        </ul>
      </div>
    </div>
    <div v-else>
      <p>No comments found.</p>
    </div>
    <form @submit.prevent="updateComment">
      <input type="text" v-model="commentContent">
      <input type="submit" value="댓글 등록">
    </form>
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

const commentContent = ref('')

const switchEdit = () => {
  editType.value = editType.value === true? false:true
};

const updateComment = ()=>{
  axios({
    url:`http://127.0.0.1:8000/article/articles/${article.value.id}/comments/`,
    method:'POST',
    data: {
      content: commentContent.value,
      userId: store.userId
    }
  })
  .then(response => {
    console.log(response)
  })
  .catch(err => {
    console.log(err)
  })
}

onMounted(async () => {
  console.log('dd')
  
  await axios({
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
