<script setup lang="ts">
import { useGameSettingsStore } from '@/stores/heroStore';
import HeroCard from '@/components/HeroCard.vue';
import { Brain, BicepsFlexed, Zap } from 'lucide-vue-next';
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { Progress } from '@/components/ui/progress'
const team1 = useGameSettingsStore((state) => state.team1);
const team2 = useGameSettingsStore((state) => state.team2);
const router = useRouter();

onMounted(() => {
    if (team1.heroes.value.length === 0 || team2.heroes.value.length === 0) {
        router.push('/');
    }
});
</script>

<template>
    <div class="flex flex-col w-full items-center">
        <div class="border border-blue-500 w-[1400px] h-[400px] rounded-xl p-3">

            <div class="flex justify-between">
                <div>
                    <h1 class="text-lg font-bold">Team 1</h1>
                    <div class="flex gap-2">

                        <HeroCard v-for="hero in team1.heroes.value.slice(0, 1)" :key="hero.id" :hero="hero"
                            size="medium" />
                        <div class="flex flex-col justify-end py-10 gap-2">
                            <div class="flex flex-col items-end gap-2">
                                <h2 class="rounded-md bg-red-700 text-white p-1 text-sm text-center">Hp ❤️
                                    200 / 200</h2>
                                <Progress :model-value="100" class="w-[400px]" indicator-class="bg-red-500" />
                            </div>
                            <div class="border border-dashed border-blue-500 flex gap-3 items-center rounded-lg p-2">
                                <Brain class="w-10 h-10" />
                                <h3>Mental attack: 300</h3>
                            </div>
                            <div class="border border-dashed border-orange-500 flex gap-3 items-center rounded-lg p-2">
                                <BicepsFlexed class="w-10 h-10" />
                                <h3>Strong attack: 300</h3>
                            </div>
                            <div class="border border-dashed border-green-500 flex gap-3 items-center rounded-lg p-2">
                                <Zap class="w-10 h-10" />
                                <h3>Speed attack: 300</h3>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="flex gap-2 flex-col w-[40%]">
                    <div>
                        <h2>Next team members</h2>
                        <div class="flex gap-2 mt-1">
                            <HeroCard v-for="hero in team1.heroes.value.slice(1, 4)" :key="hero.id" :hero="hero"
                                size="small" />
                        </div>
                    </div>
                    <div>
                        <h2>Dead members</h2>
                        <div class="flex gap-2 mt-1">
                            <HeroCard v-for="hero in team1.heroes.value.slice(4)" :key="hero.id" :hero="hero"
                                :is-dead="true" size="small" />
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <h2 class="text-3xl my-3">VS</h2>
        <div class="border border-orange-500 w-[1400px] h-[400px] rounded-xl p-3">
            <h1>GameField</h1>
        </div>

        <div class="border border-slate-400 border-dashed w-[1400px] h-[200px] rounded-xl p-4 mt-10 overflow-y-auto">
            <h1>GameField</h1>
            <h1>GameField</h1>
            <h1>GameField</h1>
            <h1>GameField</h1>
            <h1>GameField</h1>
            <h1>GameField</h1>
            <h1>GameField</h1>
            <h1>GameField</h1>
            <h1>GameField</h1>
            <h1>GameField</h1>
            <h1>GameField</h1>
            <h1>GameField</h1>
            <h1>GameField</h1>
            <h1>GameField</h1>
            <h1>GameField</h1>
            <h1>GameField</h1>
            <h1>GameField</h1>
            <h1>GameField</h1>
            <h1>GameField</h1>
            <h1>GameField</h1>
        </div>
    </div>

</template>
