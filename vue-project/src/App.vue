<template>
  <header>
    <nav class="navbar navbar-expand-lg bg-custom-navbar">
      <div class="container-fluid">
        <a class="navbar-brand" href="/">
          <img src="@/assets/yg.jpg" alt="Logo" width="60" height="30" class="d-inline-block align-text-top">
          YG
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <RouterLink :to="{ name: 'ArticleView' }">게시글</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name: 'SignUpView' }">회원가입</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name: 'LogInView' }">로그인</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name: 'CompareView' }">예적금 금리 비교</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name: 'CalculatorView' }">신혼 여행을 위한 환율계산기</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name: 'MapView' }">내 집 주변 은행 검색</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name: 'ProductRecommendView' }">나에게 맞는 상품 추천</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
</script>

<style scoped>
.nav-item {
  margin-right: 10px;
}

.bg-custom-navbar {
  background-color: #D6B534 ;
}

</style>
