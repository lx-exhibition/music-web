<script setup>
import {useRouter,useRoute,useLink} from 'vue-router'
let route = useRoute()
</script>

<template>
  {{route.fullPath}}
  <el-skeleton class="animate-pulse"></el-skeleton>
</template>

<style scoped>

</style>