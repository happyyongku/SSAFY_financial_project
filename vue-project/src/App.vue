<template>
  <header>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
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
              <RouterLink :to="{ name: 'ArticleView' }">Articles</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name: 'SignUpView' }">회원가입</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink :to="{ name: 'LogInView' }">로그인</RouterLink>
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
  margin-right: 5px;
}
</style>
