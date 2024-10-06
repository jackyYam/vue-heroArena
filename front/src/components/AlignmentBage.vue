<script setup lang="ts">
import Badge from './ui/badge/Badge.vue';
import { cn } from '@/lib/utils';
defineProps<{
    isAlignment: boolean;
    alignment?: string;
    buffed?: boolean;
    buff?: number;
}>();
</script>

<template>
    <Badge :class="cn('hover:none', {
        'bg-slate-400 text-black': alignment === 'bad',
        'bg-blue-400 text-black': alignment === 'good',
        'bg-green-400 text-black': !isAlignment && buffed,
        'bg-red-400 text-black': !isAlignment && !buffed,

    })">
        <img v-if="alignment === 'good'" src="/superhero.png" class="w-6 h-6 mr-1" />
        <img v-if="alignment === 'bad'" src="/villian.svg" class="w-6 h-6 mr-1" />
        <img v-if="buff && buffed" src="/buff.png" class="w-6 h-6 mr-1" />
        <img v-if="buff && !buffed" src="/debuff.png" class="w-6 h-6 mr-1" />
        <span v-if="isAlignment">{{ alignment }}</span>
        <span v-else>{{ buff }}</span>
    </Badge>
</template>
