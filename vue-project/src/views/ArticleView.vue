<template>
  <div>
    <header>게시판</header>
    <div class="d-flex flex-column align-items-center w-75">
      <div>
        <h1>게시글</h1>
      <RouterLink :to="{ name: 'CreateView' }">
        [CREATE]
      </RouterLink>
      <ArticleList />
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import ArticleList from '@/components/ArticleList.vue'

const store = useCounterStore()

onMounted(() => {
  store.getArticles()
})

</script>

<style>

</style>
