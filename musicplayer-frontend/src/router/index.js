import { createRouter, createWebHistory } from 'vue-router'
import Songs from '../components/Songs.vue'
import Albums from '../components/Albums.vue'
import Artists from '../components/Artists.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {path: '/songs', name: 'songs', component: Songs},
    {path: '/albums', name: 'albums', component: Albums},
    {path: '/artists', name: 'artists', component: Artists},
  ]
})

export default router
