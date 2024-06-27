<script setup>
import {useRouter,useRoute,useLink} from 'vue-router'
let route = useRoute()
</script>

<template>
  <div class="flex flex-row">
    <a class="mx-auto" href="http://localhost:8001/media/player.exe" target="_blank">
      <el-button>桌面客户端</el-button>
    </a>
  </div>
</template>

<style scoped>

</style>