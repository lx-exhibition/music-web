<script setup>
import {useRouter,useRoute,useLink} from 'vue-router'
let route = useRoute()
</script>

<template>
  {{route.fullPath}}
</template>

<style scoped>

</style>