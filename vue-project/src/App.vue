<template>
  <div id="AppVue">
    <div class="d-flex flex-column justify-content-center ">
      <header>
        <nav class="navbar navbar-expand-lg bg-custom-navbar">
          <div class="container-fluid">
            <a class="navbar-brand px-2" href="/">
              <img src="@/assets/yg.png" alt="Logo" width="60" height="30" class="d-inline-block align-text-top ">
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
                <li class="nav-item" v-if="!userId">
                  <RouterLink :to="{ name: 'LogInView' }" class="custom-router-link">로그인</RouterLink>              
                </li>
                <li class="nav-item" v-if="userId">
                  <a @click="store.logOut">로그아웃</a>              
                </li>
                <li class="nav-item">
                  <RouterLink :to="{ name: 'ReadProductView' }" class="custom-router-link">전체 금융 상품 조회</RouterLink>
                </li>
                <li class="nav-item">
                  <RouterLink :to="{ name: 'CompareView' }" class="custom-router-link">예적금 금융 상품 비교</RouterLink>
                </li>
                <li class="nav-item">
                  <RouterLink :to="{ name: 'ExchangeView' }" class="custom-router-link">신혼 여행을 위한 환율계산기</RouterLink>
                </li>
                <li class="nav-item">
                  <RouterLink :to="{ name: 'MapView' }" class="custom-router-link">내 집 주변 은행 검색</RouterLink>
                </li>
  
                <li class="nav-item" v-if="userId">
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
      <div class="content-body">
        <RouterView/>
      </div>
    </div>
    <footer class="py-3" style="background-color: #ac672c;">
        <div class="container">
            <p class="m-0 text-center text-white">Copyright YG Financial. All Rights Reserved.</p>
            <div class="d-flex justify-content-end">
            <a href="https://www.ssafy.com/ksp/jsp/swp/swpMain.jsp">
              <img src="@/assets/home_page.png" alt="homepage img" style="width: 25px; height: 25px; border: solid black 1px; border-radius: 10%; margin: 5px; background-color: white;">
            </a>
            <a href="https://www.facebook.com/hellossafy">
              <img src="@/assets/facebook.png" alt="facebook img" style="width: 25px; height: 25px; border: solid black 1px; border-radius: 10%; margin: 5px; background-color: white;">
            </a>
            <a href="https://www.instagram.com/jeong90_97/">
              <img src="@/assets/instagram.png" alt="instagram img" style="width: 25px; height: 25px; border: solid black 1px; border-radius: 10%; margin: 5px; background-color: white;">
            </a>
            <a href="https://www.youtube.com/channel/UC_XI3ByFO1uZIIH-g-zJZiw/featured">
              <img src="@/assets/youtube.png" alt="youtube img" style="width: 25px; height: 25px; border: solid black 1px; border-radius: 10%; margin: 5px; background-color: white;">
            </a>
            <a href="https://pf.kakao.com/_Vhxoxnxb">
              <img src="@/assets/kakao.png" alt="kakao img" style="width: 25px; height: 25px; border: solid black 1px; border-radius: 10%; margin: 5px; background-color: white;">
            </a>
            <a href="https://www.notion.so/62e62adb6dc04794a74009c54b3791a9?v=56c520a058ef49cd9405cb80d1274585">
              <img src="@/assets/notion.png" alt=" img" style="width: 25px; height: 25px; border: solid black 1px; border-radius: 10%; margin: 5px; background-color: white;">
          </a>
          </div>
      </div>
    </footer>
  </div>
</template>


<script setup>
import { RouterView, RouterLink } from 'vue-router'
import { ref, computed } from 'vue'
import { useCounterStore } from './stores/counter';

const store = useCounterStore()
const userId = computed(()=>{
  return store.userId
})

const test = function(){
  console.log(userId.value)
  console.log('/////')
  console.log(store.userId)
}


</script>

<style scoped>
.nav-item {
  margin-right: 20px;
  font-weight: bold;
}

.bg-custom-navbar {
  background-color: #faedad ;
}

.custom-router-link {
  color: black; 
  text-decoration: none; 
}

*h3 {
  font-family: 'Century Gothic', sans-serif; 
}

div {
      font-family: "Noto Sans KR", sans-serif;
      font-optical-sizing: auto;
      font-style: normal;
}
.content-body {
  min-height: 800px;
}

</style>
<style src="@/assets/styles.css">
  
</style>