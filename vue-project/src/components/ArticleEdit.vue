<template>
  <div>
    <h1>게시글 수정</h1>
    <form @submit.prevent="updateArticle">
      <div>
        <label for="title">제목 : </label>
        <input type="text" v-model.trim="title" id="title">
      </div>
      <div>
        <label for="content">내용 : </label>
        <textarea v-model.trim="content" id="content"></textarea>
      </div>
      <input type="submit" value="수정">
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      title: '', // 수정할 게시글의 제목
      content: '', // 수정할 게시글의 내용
      articleId: null // 수정할 게시글의 ID
    };
  },
  mounted() {
    // ArticleEdit.vue가 마운트될 때 게시글 데이터를 가져오는 메서드 호출
    this.getArticleData();
  },
  methods: {
    async getArticleData() {
      try {
        // 라우터에서 전달된 params를 통해 게시글 ID를 가져옴
        this.articleId = this.$route.params.id;
        
        // 서버 API를 호출하여 게시글 데이터를 가져옴
        const response = await axios.get(`/api/articles/${this.articleId}`);
        const article = response.data;

        // 가져온 게시글 데이터를 폼에 채움
        this.title = article.title;
        this.content = article.content;
      } catch (error) {
        console.error('Error fetching article data:', error);
      }
    },
    async updateArticle() {
      try {
        // 수정된 게시글 데이터를 서버에 보내어 업데이트
        await axios.put(`/api/articles/${this.articleId}`, {
          title: this.title,
          content: this.content
        });

        // 수정이 완료되면 DetailView.vue로 이동
        this.$router.push({ name: 'DetailView', params: { id: this.articleId } });
      } catch (error) {
        console.error('Error updating article:', error);
      }
    }
  }
}
</script>
  
  <style>
  </style>
  