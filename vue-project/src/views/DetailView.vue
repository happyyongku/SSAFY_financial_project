<template>
  <div>
    <h1>DetailView</h1>
    <div v-if="article">
      <p>{{ article.id }}</p>
      <p>{{ article.title }}</p>
      <p>{{ article.content }}</p>
      <p>{{ article.created_at }}</p>
      <p>{{ article.updated_at }}</p>
      <button @click="navigateToEditArticle">Edit Article</button>
      <button @click="deleteArticle">Delete Article</button>
    </div>
    <button @click="navigateToCommentForm">Add Comment</button>
    <div v-if="comments.length">
      <h2>Comments</h2>
      <div v-for="comment in comments" :key="comment.id" class="comment-card">
        <p>{{ comment.content }}</p>
        <p>by {{ comment.author }}</p>
        <button @click="navigateToEditComment(comment.id)">Edit</button>
        <button @click="deleteComment(comment.id)">x</button>
      </div>
    </div>
    <div v-else>
      <p>No comments found.</p>
    </div>
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

const navigateToCommentForm = () => {
  router.push({ name: 'CommentForm', params: { id: route.params.id } });
};

const navigateToEditArticle = () => {
  router.push({ name: 'ArticleEdit', params: { id: route.params.id } });
};

const deleteArticle = () => {
  axios({
    method: 'delete',
    url: `${store.API_URL}/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then(() => {
      router.push({ name: 'ArticleListView' });
    })
    .catch((error) => {
      console.log(error);
    });
};

const navigateToEditComment = (commentId) => {
  router.push({ name: 'CommentEdit', params: { articleId: route.params.id, commentId } });
};

const deleteComment = (commentId) => {
  axios({
    method: 'delete',
    url: `${store.API_URL}/comments/${commentId}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then(() => {
      store.getComments(route.params.id);
      comments.value = store.comments;
    })
    .catch((error) => {
      console.log(error);
    });
};

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
  })
    .then((response) => {
      article.value = response.data;
    })
    .catch((error) => {
      console.log(error);
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
