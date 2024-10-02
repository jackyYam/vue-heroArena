<script setup lang="ts">
import type { Hero } from '@/lib/types';
import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
} from '@/components/ui/card'
const props = defineProps<{
    hero: Hero;
}>();
</script>

<template>
    <Card>
        <CardHeader>
            <CardTitle>{{ props.hero.name }}</CardTitle>
        </CardHeader>
        <CardContent>
            <img :src="props.hero.image" :alt="props.hero.name" class="w-36">
            <div>
                {{ props.hero.powerstats }}
            </div>
        </CardContent>
    </Card>
</template>
