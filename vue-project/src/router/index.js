import { createRouter, createWebHistory } from 'vue-router'
import ArticleView from '@/views/ArticleView.vue'
import DetailView from '@/views/DetailView.vue'
import CreateView from '@/views/CreateView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import CompareView from '@/views/CompareView.vue'
import CalculatorView from '@/views/CalculatorView.vue'
import MapView from '@/views/MapView.vue'
import ProductRecommendView from '@/views/ProductRecommendView.vue'
import UserView from '@/views/UserView.vue'
import UserProfile from '@/components/UserProfile.vue'
import UserPosts from '@/components/UserPosts.vue'
import ExchangeCalculator from '@/views/ExchangeCalculator.vue'
import ChatBotView from '@/views/ChatBotView.vue'
import HomeView from '@/views/HomeView.vue'
import ReadProductView from '@/views/ReadProductView.vue'
import ArticleEdit from '@/components/ArticleEdit.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/',
      name: 'HomeView',
      component: HomeView
    },
    {
      path: '/articles',
      name: 'ArticleView',
      component: ArticleView
    },
    {
      path: '/articles/:id',
      name: 'DetailView',
      component: DetailView,
      props: true
    },
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/compare',
      name: 'CompareView',
      component: CompareView
    },
    {
      path: '/calculator',
      name: 'CalculatorView',
      component: CalculatorView
    },
    {
      path: '/map',
      name: 'MapView',
      component: MapView
    },
    {
      path: '/product_recommend',
      name: 'ProductRecommendView',
      component: ProductRecommendView
    },
    {
      path: '/user/:id',
      name: 'UserView',
      component: UserView,
      children: [
        { path: 'profile', name: 'user-profile', component: UserProfile },
        { path: 'posts', name: 'user-posts', component: UserPosts }
      ]
    },
    {
      path: '/exchange-calculrator',
      name: 'ExchangeView',
      component: ExchangeCalculator,
    },
    {
      path: '/chatbot',
      name: 'ChatBotView',
      component: ChatBotView
    },
    {
      path:'/read-product',
      name:'ReadProductView',
      component: ReadProductView
    },
    {
      path: '/ArticleEdit',
      name: 'ArticleEdit',
      component: ArticleEdit
    }
  ]
})

import { useCounterStore } from '@/stores/counter'
import { useExchangeStore } from '@/stores/financial'
import { useFinancialStore } from '@/stores/financial'
import { ref } from 'vue'
import axios from 'axios'


router.beforeEach((to, from) => {
  const store = useCounterStore()
  const exchangeStore = useExchangeStore()
  const financialStore = useFinancialStore()
  const token= ref(useCounterStore().token)

  if (to.name === 'ArticleView' && store.isLogin === false) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView' }
  }
  if (to.name === 'UserView' && store.isLogin === false) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView' }
  }
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin === true)) {
    window.alert('이미 로그인 했습니다.')
    return { name: 'HomeView' }
  }
  if ((to.name==='ReadProductView' && !store.isLogin)){
    window.alert('로그인이 필요합니다.')
  }
  if ((to.name==='ExchangeView' && !store.isLogin)){
    window.alert('기능 사용을 위해 로그인이 필요합니다.')
  }
  if ((to.name === 'CompareView' && !store.isLogin)){
    window.alert('기능 사용을 위해 로그인이 필요합니다.')
  }

  if (to.name === 'ExchangeView') {
    exchangeStore.getToday()
    console.log('///////////')
    exchangeStore.getTargetRate(exchangeStore.currentDate)
    exchangeStore.getDateList()
  }

  if (to.name === 'ChatBotView'){
    axios({
      url:'http://127.0.0.1:8000/financial_product/chat/initialize/',
      method: 'post'
    })
    .then(res => {
      console.log('initialized')
    })
  }

  // if (to.name === 'ReadProductView') {
  //   financialStore.readType = 'deposit'
  //   axios({
  //     url: `http://127.0.0.1:8000/financial_product/read_product/deposit/`,
  //     method:'get',
  //     headers: {
  //       Authorization: `Token ${token.value}`
  //       }
  //   })
  //   .then(response => {
  //     financialStore.readTable = response.data
  //   })
  //   .then(() => {
  //     next()
  //   })
  //   .catch(error => {
  //     console.log(error)
  //   })
  // }
})

export default router