<script setup lang="ts">
import type { HeroFull } from '@/lib/types';
import {
    Card,
    CardContent,
    CardHeader,
    CardTitle,
} from '@/components/ui/card'
import { ref, watch } from 'vue';
import { NotepadText } from 'lucide-vue-next';
import AlignmentBage from './AlignmentBage.vue';
import { cn } from '@/lib/utils';
import Button from './ui/button/Button.vue';
import {
    HoverCard,
    HoverCardContent,
    HoverCardTrigger,
} from '@/components/ui/hover-card'

const props = defineProps<{
    hero: HeroFull;
    size: 'small' | 'medium' | 'large';
    isDead?: boolean;
}>();

const heroImage = ref(props.hero.image);

watch(() => props.hero.image, (newImage) => {
    heroImage.value = newImage;
});


const setFallbackImage = (event: Event) => {
    (event.target as HTMLImageElement).src = '/fallback.png'; // Path to your fallback image in the public folder
};

</script>

<template>
    <Card :class="cn({
        'w-72': size === 'medium',
        'w-52': size === 'small',
        'w-96': size === 'large',
    })">
        <CardHeader class="p-4 flex items-center" :class="cn('p-4 flex items-center', {
            'p-1 flex-row gap-1 justify-between': size === 'small',
        })">
            <CardTitle :class="cn({
                'text-base w-[70%]': size === 'small',
                'text-xl': size !== 'small',
            })">{{ props.hero.name }} <span v-if="size !== 'small'"
                    class="rounded-md bg-red-700 text-white p-1 text-sm text-center">❤️
                    {{
                        props.hero.hp
                    }}</span>

                <span v-if="isDead" class="rounded-md bg-black text-white p-1 text-sm text-center">
                    💀
                </span>
            </CardTitle>
            <div class="flex flex-row gap-1" v-if="size !== 'small'">
                <AlignmentBage :alignment="props.hero.alignment" :is-alignment="true" />
                <AlignmentBage :buff="props.hero.fb" :is-alignment="false" :buffed="props.hero.isbuffed" />
            </div>

            <HoverCard v-if="size !== 'large'">
                <HoverCardTrigger>
                    <Button variant="outline" class="gap-2" :size="size === 'small' ? 'icon' : 'default'">
                        <NotepadText />
                        <span v-if="size !== 'small'">View Stats</span>
                    </Button>
                </HoverCardTrigger>
                <HoverCardContent :side="'right'">
                    <div class="border border-gray-300 rounded-lg w-56 p-2">
                        <ul>
                            <li v-if="size === 'small'">
                                <span class="rounded-md bg-red-700 text-white p-1 text-sm text-center">❤️
                                    {{
                                        props.hero.hp
                                    }}</span>
                            </li>
                            <li v-for="(value, key) in props.hero.powerstats" :key="key">
                                <span class="capitalize">{{ key }}:</span> {{ value }} -> <span class="font-semibold">{{
                                    hero.actualStats[key] }}</span>
                            </li>
                        </ul>
                    </div>
                </HoverCardContent>
            </HoverCard>

        </CardHeader>
        <CardContent class="flex flex-col items-center gap-2 pb-3">
            <img :src="heroImage" :alt="props.hero.name" @error="setFallbackImage" :class="cn({
                'w-36 h-48': size !== 'small',
                'w-18 h-20': size === 'small',
                'grayscale': isDead
            })">
            <div v-if="size === 'large'" class="border border-gray-300 rounded-lg w-56 p-2">
                <ul>
                    <li v-for="(value, key) in props.hero.powerstats" :key="key">
                        <span class="capitalize">{{ key }}:</span> {{ value }} -> <span class="font-semibold">{{
                            hero.actualStats[key] }}</span>
                    </li>
                </ul>
            </div>
        </CardContent>
    </Card>
</template>
