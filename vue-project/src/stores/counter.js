// import { ref, computed } from 'vue'
// import { defineStore } from 'pinia'
// import axios from 'axios'
// import { useRouter } from 'vue-router'

// export const useCounterStore = defineStore('counter', () => {
//   const articles = ref([])
//   const API_URL = 'http://127.0.0.1:8000'
//   const token = ref(null)
//   const isLogin = computed(() => {
//     return token.value !== null
//   })
//   const router = useRouter()

//   const getArticles = function () {
//     axios({
//       method: 'get',
//       url: `${API_URL}/article/articles/`,
//       headers: {
//         Authorization: `Token ${token.value}`
//       }
//     })
//       .then(response => {
//         articles.value = response.data
//       })
//       .catch(error => {
//         console.log(error)
//       })
//   }

//   const getComments = (articlePk) => {
//     axios({
//       method: 'get',
//       url: `${API_URL}/article/${articlePk}/comments/`,
//       headers: {
//         Authorization: `Token ${token.value}`,
//       },
//     })
//       .then((response) => {
//         comments.value = response.data;
//       })
//       .catch((error) => {
//         console.log(error);
//       });
//   };

//   const signUp = function (payload) {
//     const { username, password1, password2 } = payload
//     axios({
//       method: 'post',
//       url: `${API_URL}/accounts/registration/`,
//       data: {
//         username, password1, password2
//       }
//     })
//     .then((response) => {
//       const password = password1
//       logIn({ username, password })
//     })
//     .catch((error) => {
//       console.log(error)
//     })
//   }

//   const logIn = function (payload) {
//     const { username, password } = payload
//     axios({
//       method: 'post',
//       url: `${API_URL}/accounts/login/`,
//       data: {
//         username, password
//       }
//     })
//       .then((response) => {
//         token.value = response.data.key
//         router.push({ name : 'ArticleView' })
//       })
//       .catch((error) => {
//         console.log(error)
//         window.alert('입력이 제대로 이루어지지 않았습니다.')
//       })
//   }

//   const logOut = function () {
//     axios({
//       method: 'post',
//       url: `${API_URL}/accounts/logout/`,
//       headers: {
//         Authorization: `Token ${token.value}`
//       }
//     })
//     .then(() => {
//       token.value = null
//       router.push({ name: 'LogInView' })
//     })
//     .catch((error) => {
//       console.log(error)
//     })
//   }

//   const deleteAccount = function (userPk) {
//     axios({
//       method: 'delete',
//       url: `${API_URL}/accounts/${userPk}/`,
//       headers: {
//         Authorization: `Token ${token.value}`
//       }
//     })
//     .then(() => {
//       token.value = null
//       router.push({ name: 'SignUpView' })
//     })
//     .catch((error) => {
//       console.log(error)
//     })
//   }

//   return { articles, API_URL, getArticles, getComments, signUp, logIn, logOut, deleteAccount, token, isLogin }
// }, { persist: true })

import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const userId = ref(null)
  const isLogin = computed(() => {
    return token.value !== null
  })
  const router = useRouter()

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
      .then((response) => {
        token.value = response.data.key
        return axios({
          method: 'get',
          url: `${API_URL}/accounts/login/`, // Endpoint to fetch user data
          headers: {
            Authorization: `Token ${token.value}`
          }
        })
      })
      .then((response) => {
        userId.value = response.data.id // Assuming the user ID is returned in the response
        router.push({ name : 'ArticleView' })
      })
      .catch((error) => {
        console.log(error)
        window.alert('입력이 제대로 이루어지지 않았습니다.')
      })  
  }

  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(() => {
      token.value = null
      userId.value = null
      router.push({ name: 'LogInView' })
    })
    .catch((error) => {
      console.log(error)
    })
  }

  const deleteAccount = function () {
    axios({
      method: 'delete',
      url: `${API_URL}/accounts/${userId.value}/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then(() => {
      token.value = null
      userId.value = null
      router.push({ name: 'HomeView' })
    })
    .catch((error) => {
      console.log(error)
    })
  }

  return { articles, API_URL, getArticles, getComments, signUp, logIn, logOut, deleteAccount, token, isLogin, userId }
}, { persist: true })
