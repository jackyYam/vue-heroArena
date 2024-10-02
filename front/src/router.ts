import Home from './views/Home.vue';
import SetTeams from './views/SetTeams.vue';
import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  { path: '/', component: Home },
  { path: '/set-teams', component: SetTeams },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
