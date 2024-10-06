<script setup lang="ts">
import { useGameSettingsStore } from '@/stores/heroStore';
import HeroCard from '@/components/HeroCard.vue';
import { Brain, BicepsFlexed, Zap } from 'lucide-vue-next';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import { Progress } from '@/components/ui/progress'
import { HeroFull } from '@/lib/types';
import Button from '@/components/ui/button/Button.vue';
import AlignmentBage from '@/components/AlignmentBage.vue';
const team1 = useGameSettingsStore((state) => state.team1);
const team2 = useGameSettingsStore((state) => state.team2);
const router = useRouter();

const currentHeroT1 = ref(team1.heroes.value.shift());
const currentHeroT2 = ref(team2.heroes.value.shift());
const currentHPT1 = ref(currentHeroT1.value?.hp);
const currentHPT2 = ref(currentHeroT2.value?.hp);
const turnNumber = ref(1);
const deadHeroesT1 = ref<HeroFull[]>([]);
const deadHeroesT2 = ref<HeroFull[]>([]);
const gameLogs = ref<string[]>([]);
const winner = ref<string | null>(null);

onMounted(() => {
    if (team1.heroes.value.length === 0 || team2.heroes.value.length === 0) {
        router.push('/');
    }
});

const takeTurn = () => {
    if (winner.value) {
        return;
    }
    gameLogs.value.push('Turn ' + turnNumber.value);
    gameLogs.value.push("Turn of team " + (turnNumber.value % 2 === 1 ? 1 : 2));
    // Get the attacker and defender
    const attacker = turnNumber.value % 2 === 1 ? currentHeroT1.value : currentHeroT2.value;
    const defender = turnNumber.value % 2 === 1 ? currentHeroT2.value : currentHeroT1.value;
    const defenderHP = turnNumber.value % 2 === 1 ? currentHPT2 : currentHPT1;


    // Randomly select one of the attacks
    const attacks = ['mental', 'strong', 'fast'];
    const randomAttack = attacks[Math.floor(Math.random() * attacks.length)];

    if (attacker && defender && defenderHP.value) {

        // Reduce the opponent's HP
        defenderHP.value = Math.max(defenderHP.value - attacker.attacks[randomAttack as keyof typeof attacker.attacks], 0);
        gameLogs.value.push(`${attacker.name} attacked ${defender.name} with ${randomAttack} attack`);
        gameLogs.value.push(`${defender.name} lost ${attacker.attacks[randomAttack as keyof typeof attacker.attacks]} HP remaining HP: ${Math.max(defenderHP.value, 0)}`);
        gameLogs.value.push('----------------------');
        // Check if the defender's HP drops to 0

        if (defenderHP.value <= 0) {
            if (turnNumber.value % 2 === 1) {
                // Team 2's hero is defeated

                const nextHero = team2.heroes.value.shift();

                if (nextHero) {
                    deadHeroesT2.value.push(defender);
                    gameLogs.value.push(`${defender.name} is defeated`);
                    currentHeroT2.value = nextHero;
                    gameLogs.value.push(`${nextHero?.name} is the up next for Team 2`);
                    gameLogs.value.push('----------------------');
                    currentHPT2.value = nextHero.hp;
                } else {
                    winner.value = 'Team 1';
                    gameLogs.value.push('Team 1 wins!');
                    alert('Team 1 wins!');
                    return;
                }
            } else {
                // Team 1's hero is defeated

                const nextHero = team1.heroes.value.shift();
                if (nextHero) {
                    deadHeroesT1.value.push(defender);
                    gameLogs.value.push(`${defender.name} is defeated`);
                    currentHeroT1.value = nextHero;
                    gameLogs.value.push(`${nextHero?.name} is the up next for Team 1`);
                    gameLogs.value.push('----------------------');
                    currentHPT1.value = nextHero.hp;
                } else {
                    winner.value = 'Team 2';
                    gameLogs.value.push('Team 2 wins!');
                    alert('Team 2 wins!');
                    return;
                }
            }
        }
    }
    // Update the turn number
    turnNumber.value += 1;
};

</script>

<template>
    <div class="flex flex-col w-full items-center">
        <Button @click="router.go(0)" class="absolute bottom-28 right-3 w-28" v-if="winner" variant="secondary">New
            Game</Button>
        <Button @click="takeTurn" class="absolute bottom-10 right-3" :disabled="winner">
            {{ winner ? 'Game Ended' : '▶️ Take Turn' }}
        </Button>
        <div class="border border-blue-500 w-[1500px] h-[430px] rounded-xl p-3">
            <div class="flex justify-between">
                <div>
                    <h1 class="text-lg font-bold flex items-center gap-2">Team 1
                        <AlignmentBage :is-alignment="true" :alignment="team1.alignment.value" />
                    </h1>
                    <div class="flex gap-2">

                        <HeroCard v-if="currentHeroT1" :hero="currentHeroT1" size="medium" />
                        <div class="flex flex-col justify-end py-10 gap-2">
                            <div class="flex flex-col items-end gap-2">
                                <h2 class="rounded-md bg-red-700 text-white p-1 text-sm text-center">Hp ❤️
                                    {{ currentHPT1 }} / {{ currentHeroT1?.hp }}</h2>
                                <Progress :model-value="(currentHPT1 ?? 0) * 100 / (currentHeroT1?.hp ?? 1)"
                                    class="w-[400px]" indicator-class="bg-red-500" />
                            </div>
                            <div class="border border-dashed border-blue-500 flex gap-3 items-center rounded-lg p-2">
                                <Brain class="w-10 h-10" />
                                <h3>Mental attack: {{ currentHeroT1?.attacks.mental }}</h3>
                            </div>
                            <div class="border border-dashed border-orange-500 flex gap-3 items-center rounded-lg p-2">
                                <BicepsFlexed class="w-10 h-10" />
                                <h3>Strong attack: {{ currentHeroT1?.attacks.strong }}</h3>
                            </div>
                            <div class="border border-dashed border-green-500 flex gap-3 items-center rounded-lg p-2">
                                <Zap class="w-10 h-10" />
                                <h3>Speed attack: {{ currentHeroT1?.attacks.fast }}</h3>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="flex gap-2 flex-col w-[50%]">
                    <div>
                        <h2>Next team members</h2>
                        <div class="flex gap-2 mt-1">
                            <HeroCard v-for="hero in team1.heroes.value" :key="hero.id" :hero="hero" size="small" />
                        </div>
                    </div>
                    <div>
                        <h2>Dead members</h2>
                        <div class="flex gap-2 mt-1">
                            <HeroCard v-for="hero in deadHeroesT1" :key="hero.id" :hero="hero" :is-dead="true"
                                size="small" />
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <h2 class="text-3xl my-3">VS</h2>
        <div class="border border-orange-500 w-[1500px] h-[430px] rounded-xl p-3">
            <div class="flex justify-between">
                <div>
                    <h1 class="text-lg font-bold flex items-center gap-2">Team 2
                        <AlignmentBage :is-alignment="true" :alignment="team2.alignment.value" />
                    </h1>
                    <div class="flex gap-2">

                        <HeroCard v-if="currentHeroT2" :hero="currentHeroT2" size="medium" />
                        <div class="flex flex-col justify-end py-10 gap-2">
                            <div class="flex flex-col items-end gap-2">
                                <h2 class="rounded-md bg-red-700 text-white p-1 text-sm text-center">Hp ❤️
                                    {{ currentHPT2 }} / {{ currentHeroT2?.hp }}</h2>
                                <Progress :model-value="(currentHPT2 ?? 0) * 100 / (currentHeroT2?.hp ?? 1)"
                                    class="w-[400px]" indicator-class="bg-red-500" />
                            </div>
                            <div class="border border-dashed border-blue-500 flex gap-3 items-center rounded-lg p-2">
                                <Brain class="w-10 h-10" />
                                <h3>Mental attack: {{ currentHeroT2?.attacks.mental }}</h3>
                            </div>
                            <div class="border border-dashed border-orange-500 flex gap-3 items-center rounded-lg p-2">
                                <BicepsFlexed class="w-10 h-10" />
                                <h3>Strong attack: {{ currentHeroT2?.attacks.strong }}</h3>
                            </div>
                            <div class="border border-dashed border-green-500 flex gap-3 items-center rounded-lg p-2">
                                <Zap class="w-10 h-10" />
                                <h3>Speed attack: {{ currentHeroT2?.attacks.fast }}</h3>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="flex gap-2 flex-col w-[50%]">
                    <div>
                        <h2>Next team members</h2>
                        <div class="flex gap-2 mt-1">
                            <HeroCard v-for="hero in team2.heroes.value" :key="hero.id" :hero="hero" size="small" />
                        </div>
                    </div>
                    <div>
                        <h2>Dead members</h2>
                        <div class="flex gap-2 mt-1">
                            <HeroCard v-for="hero in deadHeroesT2" :key="hero.id" :hero="hero" :is-dead="true"
                                size="small" />
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="border border-slate-400 border-dashed w-[1500px] h-[200px] rounded-xl p-4 mt-10 overflow-y-auto">
            <h2 class="text-lg font-bold">Game Logs:</h2>
            <ul>
                <li v-for="log, index in gameLogs" :key="'log' + index" class="text-sm">{{ log }}</li>
            </ul>
        </div>
    </div>

</template>
