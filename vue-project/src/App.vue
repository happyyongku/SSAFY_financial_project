<template>
  <div id="AppVue">
    <header>
      <nav class="navbar navbar-expand-lg bg-custom-navbar">
        <div class="container-fluid">
          <a class="navbar-brand px-2" href="/">
            <img src="@/assets/yg.jpg" alt="Logo" width="60" height="30" class="d-inline-block align-text-top ">
          </a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0 d-flex justify-content-evenly">
              <li class="nav-item">
                <RouterLink :to="{ name: 'ArticleView' }" class="custom-router-link">게시글</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink :to="{ name: 'SignUpView' }" class="custom-router-link">회원가입</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink :to="{ name: 'LogInView' }" class="custom-router-link"
                v-if="!userId">로그인</RouterLink>
                <RouterLink :to="{name:'HomeView'}" v-if="userId" >로그아웃</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink :to="{ name: 'CompareView' }" class="custom-router-link">예적금 금리 비교</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink :to="{ name: 'ExchangeView' }" class="custom-router-link">신혼 여행을 위한 환율계산기</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink :to="{ name: 'MapView' }" class="custom-router-link">내 집 주변 은행 검색</RouterLink>
              </li>

              <li class="nav-item">
                <RouterLink :to="{ name: 'UserView', params: {'id' : userId } }" class="custom-router-link">나의 프로필</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink :to="{name: 'ChatBotView'}" class="custom-router-link">
                  챗봇 상품 추천
                </RouterLink>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </header>
    <RouterView />
  </div>
  <footer>footer</footer>
</template>


<script setup>
import { RouterView, RouterLink } from 'vue-router'
import { ref } from 'vue'

const userId = ref(1)
const chatBot = ref(false)
const switchChat = function(){
  chatBot.value = chatBot.value===false?true:false
}

</script>

<style scoped>
.nav-item {
  margin-right: 20px;
  font-weight: bold;
}

.bg-custom-navbar {
  background-color: #F2E394 ;
}

.custom-router-link {
  color: black; 
  text-decoration: none; 
}

</style>
<style src="@/assets/styles.css">
  
</style>