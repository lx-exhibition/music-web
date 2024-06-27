<script setup lang="ts">
import {useRouter,useRoute,useLink} from 'vue-router'
let route = useRoute(), router = useRouter()

import {watchEffect,ref} from 'vue'
import {get} from '@/components/utils/http'
let data = ref()
watchEffect(async ()=>{
  await get('o-Friends/').then(res => data.value = res)
})

let c_row = 'flex flex-row', c_col = 'flex flex-col'
</script>

<template>
  <div v-for="(v) in data" :class="c_row">
    <el-image :src="v.user.avatar" class="size-24 rounded-2xl mt-2"></el-image>
    <div :class="[c_col, 'ml-2 mt-6']">
      <p>{{v.content}}</p>
      <p class="mt-4">{{v.pub_date}}</p>
    </div>
  </div>

</template>

<style scoped>

</style>