<script setup>
import {useRouter,useRoute} from 'vue-router'
let route = useRoute(), router = useRouter()

router.push('/g/Artist')
</script>

<template>
  <el-skeleton class="animate-pulse"></el-skeleton>
</template>

<style scoped>

</style>