<script setup lang="ts">
import { useHeroStore } from '@/stores/heroStore';
import { onMounted } from 'vue';
import Button from '@/components/ui/button/Button.vue';
import HeroCard from '@/components/HeroCard.vue';

const { team1, team2 } = useHeroStore();
const splitTeams = useHeroStore((state) => state.splitTeams);
onMounted(() => {
    splitTeams();
});
</script>

<template>
    <div class="w-[80%]">

        <div v-if="team1.length > 0">
            <h2>Heroes of Team 1:</h2>
            <div class="flex gap-2">
                <HeroCard v-for="hero in team1" :key="hero.id" :hero="hero" />
            </div>
        </div>
        <div v-if="team2.length > 0">
            <h2>Heroes of Team 2:</h2>
            <ul>
                <li v-for="hero in team2" :key="hero.id">{{ hero.name }}</li>
            </ul>
        </div>

        <Button class="w-[50%]" @click="splitTeams">Reform Teams</Button>
    </div>
</template>
