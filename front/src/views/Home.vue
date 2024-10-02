<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
import { Button } from '@/components/ui/button';
import { Progress } from '@/components/ui/progress'
import { useRouter } from 'vue-router';
import { useHeroStore } from '@/stores/heroStore';

const progress = ref(0);
const loading = ref(false);

let socket: WebSocket | null = null;
const router = useRouter();
const setHeroes = useHeroStore(state => state.setHeroes);

const startProgress = () => {
  if (socket) {
    loading.value = true;
    socket.send('start');
  }
};

onMounted(() => {
  socket = new WebSocket('ws://localhost:8000/ws/get-heroes');

  socket.onopen = () => {
    console.log('WebSocket connection opened');
  };

  socket.onmessage = (event) => {
    try {
      const data = JSON.parse(event.data);
      if (data.heroes) {
        setHeroes(data.heroes);
        loading.value = false;
        router.push('/set-teams');
      } else {
        progress.value = event.data;
      }
    } catch (e) {
      progress.value = event.data;
    }
  };

  socket.onclose = (event) => {
    console.log('WebSocket connection closed: ', event);
  };

  socket.onerror = (error) => {
    console.log('WebSocket error: ', error);
  };
});

onUnmounted(() => {
  if (socket) {
    socket.close();
  }
});
</script>

<template>
  <div class="w-full flex justify-center flex-col items-center gap-4">
    <h1 class="text-4xl font-bold">Epic superhero battle simulator</h1>
    <h3 class="text-2xl">Battle in team of 5 superheros from all universe</h3>
    <img src="../assets/front.jpg" alt="landing picture" />
    <Button class="w-[50%]" @click="startProgress" :disabled="loading">{{ loading ? "Assembling..." : "Assemble Heros"
      }}</Button>
    <div v-if="loading" class="w-full flex flex-col justify-center items-center">
      <div>Progress: {{ progress }}%</div>
      <Progress :model-value="Number(progress)" class="w-[50%]" />
    </div>

  </div>
</template>
