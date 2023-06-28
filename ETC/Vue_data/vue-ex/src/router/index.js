import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'parent',
    component: () => import('@/views/ParentView')
  },
  {
    path: '/global',
    name: 'global',
    component: () => import('@/views/GlobalView')
  },
  {
    path: '/vuex',
    name: 'vuex',
    component: () => import('@/views/VuexView')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
