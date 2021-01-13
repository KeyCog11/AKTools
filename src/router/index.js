import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import EnemyFinder from "../views/EnemyFinder.vue"
import MarkdownViewer from "../views/MarkdownViewer.vue"
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/enemyfinder',
    name: "EnemyFinder",
    component: EnemyFinder
  },
  {
    path: '/blog/:md',
    name: "MarkdownViewer",
    component: MarkdownViewer
  }
]

const router = new VueRouter({
  routes
})

export default router
