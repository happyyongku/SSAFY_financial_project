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

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'ArticleView',
      component: ArticleView
    },
    {
      path: '/articles/:id',
      name: 'DetailView',
      component: DetailView
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
    }

  ]
})

import { useCounterStore } from '@/stores/counter'
import { useExchangeStore } from '@/stores/financial'


router.beforeEach((to, from) => {
  const store = useCounterStore()
  const exchangeStore = useExchangeStore()

  if (to.name === 'ArticleView' && store.isLogin === false) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView' }
  }
  // if (to.name === 'UserView' && store.isLogin === false) {
  //   window.alert('로그인이 필요합니다.')
  //   return { name: 'LogInView' }
  // }
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin === true)) {
    window.alert('이미 로그인 했습니다.')
    return { name: 'ArticleView' }
  }

  if (to.name === 'ExchangeView') {
    exchangeStore.getToday()
    console.log('///////////')
    exchangeStore.getTargetRate(exchangeStore.currentDate)
    exchangeStore.getDateList()
  }
})

export default router
