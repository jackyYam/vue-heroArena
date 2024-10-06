<script setup lang="ts">
import ModeSwitch from './components/ModeSwitch.vue';
import { RouterView } from 'vue-router';
</script>

<template>
    <img src="./assets/logo.png" alt="logo" class="absolute top-5 left-5 w-32 h-32">
    <main class="h-screen w-screen flex justify-center items-center">
        <RouterView />
    </main>
    <div class="absolute bottom-8 left-8 ">
        <ModeSwitch />
    </div>
</template>
