<script setup lang="ts">
import {useRouter,useRoute,useLink} from 'vue-router'
let route = useRoute(), router = useRouter()
import {get} from '@/components/utils/http'

import {watchEffect,ref} from 'vue'
let data = ref([])
let close_handle = watchEffect(async () => {
  const id = route.query.id ? route.query.id : localStorage.getItem('id')
  get(`my-videos/?id=${id}`).then(res => data.value = res)
})

let c_row = 'flex flex-row', c_col = 'flex flex-col'
</script>

<template>
  <!--  {{route.fullPath}}-->
  <el-scrollbar v-if="data.length">
    <div v-for="(v) in data" :class="[c_row, '*:m-2 mx-8 hover:bg-sky-200 rounded-2xl']">
      <div class="size-20">
        <el-image :src="v.img" class="size-20 rounded-[30px]"/>
      </div>
      <div :class="[c_col, 'basis-auto']">
        <div class="basis-1/3">
          <div class="text-[20px] stroke-2 hover:cursor-pointer hover:text-sky-500"
               @click="router.push(`/g/Video?id=${v.id}`)"
          >{{v.title}}</div>
        </div>
        <div :class="c_row">
          <el-text line-clamp="2" class="hover:cursor-pointer hover:text-sky-500"
                   @click="router.push(`/g/Video?id=${v.id}`)"
          >{{v.description}}</el-text>
        </div>
      </div>
    </div>
  </el-scrollbar>
  <el-skeleton v-else class="animate-pulse">
    <template #template>
      <div v-for="(v) in 5" :class="[c_row, '*:m-2 mx-8']">
        <el-skeleton-item class="size-20" variant="image">
        </el-skeleton-item>
        <el-skeleton :rows="2">
        </el-skeleton>
      </div>
    </template>
  </el-skeleton>

</template>
<style scoped>

</style>