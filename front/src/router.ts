import Home from './views/Home.vue';
import SetTeams from './views/SetTeams.vue';
import GameField from './views/GameField.vue';
import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  { path: '/', component: Home },
  { path: '/set-teams', component: SetTeams },
  { path: '/game', component: GameField },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
