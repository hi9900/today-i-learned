import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'parent',
    component: () => import('@/views/ParentView.vue')
  },
  {
    path: '/global',
    name: 'global',
    component: () => import('@/views/GlobalView.vue')
  },
  {
    path: '/vuex',
    name: 'vuex',
    component: () => import('@/views/VuexView.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
