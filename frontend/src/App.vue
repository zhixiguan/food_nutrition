<script setup>
import BottomNav from './components/BottomNav.vue'
import TopNav from './components/TopNav.vue'
</script>

<template>
  <TopNav />
  <router-view></router-view>
  <BottomNav />
</template>

<style>
#app {
  max-width: 1280px;
  margin: 0 auto;
  padding: 1rem;
  padding-bottom: 0;
}
</style>
