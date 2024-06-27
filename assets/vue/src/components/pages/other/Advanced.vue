<script setup>
import {LocalFireDepartmentFilled} from '@vicons/material'
import {ShareAlt} from '@vicons/fa'
import {ThumbLike16Filled} from '@vicons/fluent'

import {useRouter,useRoute} from 'vue-router'
let route = useRoute(), router = useRouter()
import {get} from '@/components/utils/http'

import {watchEffect,ref} from 'vue'
let data = ref([])
let close_handle = watchEffect(async () => {
  get(`o-Advanced/`).then(res => data.value = res)
})

let c_row = 'flex flex-row', c_col = 'flex flex-col'
let c_hover = 'hover:text-sky-500 hover:cursor-pointer'
</script>

<template>
  <div v-for="(v) in data" :class="[c_row, 'items-center *:mr-12']">
    <img :src="v.img" class="size-24 rounded-2xl m-2">
    <div :class="[c_col, 'self-center items-center']">
      <p :class="[c_hover, 'ml-2']" @click="router.push(`/g/Song?id=${v.id}`)">{{v.title}}</p>
      <p :class="[c_hover, 'ml-2']" @click="router.push(`/g/Album?id=${v.album.id}`)">
        <p class="text-[10px]">《{{v.album.title}}》</p>
      </p>
      <p :class="[c_hover, 'ml-2']" @click="router.push(`/g/Artist?id=${v.artist.id}`)">
        <p class="text-[10px]">{{v.artist.stagename}}</p>
      </p>
    </div>
    <p>{{v.liked_count}}<el-icon class="text-orange-500"><ThumbLike16Filled/></el-icon></p>
    <p>{{v.shared_count}}<el-icon><ShareAlt class="text-sky-500"/></el-icon></p>
    <p>{{10*v.liked_count+v.shared_count}}<el-icon><LocalFireDepartmentFilled class="text-red-500"/></el-icon></p>
  </div>

  <el-skeleton class="animate-pulse"></el-skeleton>
</template>

<style scoped>

</style>