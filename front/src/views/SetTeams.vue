<script setup lang="ts">
import { useHeroStore } from '@/stores/heroStore';
import { onMounted } from 'vue';
import Button from '@/components/ui/button/Button.vue';
import HeroCard from '@/components/HeroCard.vue';
import { useGameSettingsStore } from '@/stores/heroStore';
import { api } from '@/lib/api';
import { useRouter } from 'vue-router';
import AlignmentBage from '@/components/AlignmentBage.vue';


const { heroes } = useHeroStore();
const team1 = useGameSettingsStore((state) => state.team1);
const team2 = useGameSettingsStore((state) => state.team2);
const setTeam1 = useGameSettingsStore((state) => state.setTeam1);
const setTeam2 = useGameSettingsStore((state) => state.setTeam2);
const router = useRouter();

const splitTeams = () => {
    api.post('/teams', {
        heroes: heroes.value,
    }).then((response) => {
        setTeam1(response.data.team1);
        setTeam2(response.data.team2);
    });
};

const startBattle = () => {
    router.push('/game');
};

onMounted(() => {
    if (heroes.value.length === 0) {
        router.push('/');
    }
    splitTeams();
});

</script>

<template>
    <div class="w-[80%]">

        <div v-if="team1.heroes.value.length > 0">
            <h2 class="font-bold text-2xl flex items-center mb-2 gap-2">
                <p>Heroes of Team 1:</p>
                <AlignmentBage :alignment="team1.alignment.value" :is-alignment="true" />
            </h2>
            <div class="flex gap-2">
                <HeroCard v-for="hero in team1.heroes.value" :key="hero.id" :hero="hero" size="large" />
            </div>
        </div>
        <div v-if="team2.heroes.value.length > 0" class="mt-3">
            <h2 class="font-bold text-2xl flex items-center mb-2 gap-2">
                <p>Heroes of Team 2:</p>
                <AlignmentBage :alignment="team2.alignment.value" :is-alignment="true" />
            </h2>
            <div class="flex gap-2">
                <HeroCard v-for="hero in team2.heroes.value" :key="hero.id" :hero="hero" size="large" />
            </div>
        </div>

        <Button class="w-56 absolute bottom-28 right-8 text-xl" @click="startBattle"> 🚀 Begin Battle</Button>
        <Button class="w-56 absolute bottom-8 right-8 text-xl" @click="splitTeams" variant="secondary"> 🔄 Reform
            Teams</Button>

    </div>
</template>
