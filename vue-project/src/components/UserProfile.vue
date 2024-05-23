
<template>
<h1>UserProfile</h1>
  <div class="profile-container">
    <div class="card custom-border" style="width: 24rem;">
      <img :src="imgSrc" class="card-img-top w-75" @error="handleError" alt="User Image">
      <div class="card-body">
        <h3 class="card-title">유저 프로필</h3>
      </div>
      <ul class="list-group list-group-flush">
        <li class="list-group-item">User Number : {{ userInfo.pk }}</li>
        <li class="list-group-item">ID : {{ userInfo.username }}</li>
        <li class="list-group-item">별명 : 
          {{ userInfo.nickname? userInfo.nickname:'anonymous' }}</li>
        <li class="list-group-item">Email : 
          {{ userInfo.email? userInfo.email: 'Not registed' }}</li>
        <li class="list-group-item">First name : 
          {{ userInfo.first_name? userInfo.first_name: 'John' }}</li>
        <li class="list-group-item">Last name : 
          {{ userInfo.last_name? userInfo.last_name: 'Doe' }}</li>
        
      </ul>
      <div class="card-body">
        <a class="card-link" @click="logOut">로그아웃</a>
        <a class="card-link" @click="confirmSignOut">회원탈퇴</a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'
import {ref, computed, onMounted, watch} from 'vue'

const store = useCounterStore()
const router = useRouter()
const defaultImg = new URL('@/assets/anonymous.png', import.meta.url).href
const userId = computed(() => {
  return store.userId
})

const userInfo = computed(() => {
  return store.userInfo
})

const logOut = () => {
  store.logOut()
  router.push({ name: 'LoginView' })
}

const confirmSignOut = () => {
  if (confirm('정말 회원 탈퇴 하시겠습니까?')) {
    store.signOut()
    router.push({ name: 'ArticleView' })
  }
}

const imgSrc = ref('')

async function getUserImage(userId) {
  const userImagePath = new URL(`@/assets/user_${userId}.png`, import.meta.url).href;
  try {
    const response = await fetch(userImagePath);
    if (!response.ok) throw new Error('Image not found');
    return userImagePath;
  } catch (error) {
    return defaultImg;
  }
}

onMounted(async () => {
  imgSrc.value = await getUserImage(userId.value);
});

// 사용자 ID 변경 시 이미지 업데이트
watch(userId, async (newUserId) => {
  imgSrc.value = await getUserImage(newUserId);
});

const handleError = (event) => {
  event.target.src = defaultImg;
};

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
  display: flex;
  flex-direction: column;
  align-items: center;
}

</style>
