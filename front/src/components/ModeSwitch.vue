<script setup lang="ts">
import { useColorMode } from '@vueuse/core'
import { Button } from '@/components/ui/button'
import { Sun, Moon } from 'lucide-vue-next';

// Pass { disableTransition: false } to enable transitions
const mode = useColorMode()
</script>

<template>
    <Button @click="mode = 'light'" size="icon" variant="outline" v-if="mode === 'dark'">
        <Moon />
    </Button>
    <Button @click="mode = 'dark'" size="icon" variant="outline" v-else>
        <Sun />
    </Button>
</template>
