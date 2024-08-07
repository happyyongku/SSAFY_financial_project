import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const isLogin = computed(() => {
    return token.value !== null
  })
  const router = useRouter()
  const initialInfo = {
    pk:null
  }
  const userInfo = ref(initialInfo)
  const userId = ref(null)

  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/article/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then(response => {
        articles.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }

  const getComments = (articlePk) => {
    axios({
      method: 'get',
      url: `${API_URL}/article/${articlePk}/comments/`,
      headers: {
        Authorization: `Token ${token.value}`,
      },
    })
      .then((response) => {
        comments.value = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const signUp = function (payload) {
    const { username, password1, password2 } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/registration/`,
      data: {
        username, password1, password2
      }
    })
    .then((response) => {
      console.log('회원가입 성공!')
      const password = password1
      logIn({ username, password })
    })
    .catch((error) => {
      console.log(error)
    })
  }

  const logIn = function (payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then(async (response) => {
        token.value = response.data.key
      })
      .then(async response => {
          await axios({
            url: `${API_URL}/accounts/user/`,
            method:'get',
            headers:{
              Authorization:`Token ${token.value}`
            }
          })
          .then(res => {
            console.log(res.data)
            console.log('///////////')
            userInfo.value = res.data
            console.log(userInfo.value)
            userId.value = userInfo.value.pk
            console.log('///////////')
            console.log(userId.value)
          })
          .catch(err => {
            console.log(`error inform : ${err}`)
          })
      })
      .then(()=>{
        router.push({ name : 'HomeView' })
      })
      .catch((error) => {
        console.log(error)
        window.alert('입력이 제대로 이루어지지 않았습니다.')
      })
  }
  
  const logOut = function () {
    if (token.value === null) {
      window.alert('로그아웃 상태입니다.')
    } else {
      token.value = null
      window.alert('로그아웃 되었습니다.')
      userInfo.value = initialInfo
      userId.value = null
      router.push({ name: 'LogInView' })
    }
  }

  const signOut = function () {
    axios({
      method: 'delete',
      url: `${API_URL}/accounts/profile/delete/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then(() => {
        token.value = null
        router.push({ name: 'SignUpView' })
      })
      .catch((error) => {
        console.log(error)
      })
  }

  return { articles, API_URL, getArticles, getComments, signUp, logIn, logOut, signOut, token, isLogin, userInfo, userId }
}, { persist: true })
