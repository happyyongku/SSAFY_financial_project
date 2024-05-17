<template>
<h1>UserProfile</h1>
  <div class="profile-container">
    <div class="card custom-border" style="width: 18rem;">
      <img src="@/assets/yonggu.png" class="card-img-top" alt="user image">
      <div class="card-body">
        <h3 class="card-title">유저 프로필</h3>
        <p class="card-text">.</p>
      </div>
      <ul class="list-group list-group-flush">
        <li class="list-group-item">전화번호 :</li>
        <li class="list-group-item">이메일 주소 : </li>
        <li class="list-group-item">주소 : </li>
      </ul>
      <div class="card-body">
        <a class="card-link" @click="logOut">로그아웃</a>
        <a class="card-link" @click="deleteAccount">회원탈퇴</a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'


  const store = useCounterStore()

  const logOut = () => {
    store.logOut()
  }

  const deleteAccount = () => {
    if (confirm('Are you sure you want to delete your account? This action cannot be undone.')) {
      store.deleteAccount()
    }
  }

</script>

<style scoped>

.profile-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  text-align: center;
}
.custom-border {
  border: 2px solid #D6B534;
  margin: 2px;
}
</style>
