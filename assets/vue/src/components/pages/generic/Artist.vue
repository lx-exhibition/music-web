<script setup>
import {Play48Filled} from '@vicons/fluent'

import {useRouter,useRoute} from 'vue-router'
let route = useRoute(), router = useRouter()
import {get} from '@/components/utils/http'

import {watchEffect,ref} from 'vue'
let data = ref([])
let close_handle = watchEffect(async () => {
  const id = route.query.id ? route.query.id : localStorage.getItem('aid')
  get(`g-Artist/?id=${id}`).then(res => data.value = res)
})

let c_row = 'flex flex-row', c_col = 'flex flex-col'
let tabs = ref('热门歌曲')


import {useTest} from '@/components/stores'
let player = useTest()
</script>

<template>
  <div class="flex justify-center">
    <div class="w-7/12">
      <p class="text-2xl">{{data.stagename}}</p>
      <img :src="data.background"
           class="h-64 rounded-3xl w-full object-cover">
    </div>
  </div>
  <el-tabs v-model="tabs">
    <el-tab-pane label="热门歌曲" name="热门歌曲">
      <div v-for="(v) in data.songs" :class="[c_row, '*:m-2 mx-8',
      'hover:bg-sky-200 rounded-3xl']">
        <div class="size-20">
          <el-image :src="v.img" class="size-20 rounded-[30px]"/>
        </div>
        <div :class="[c_col, 'basis-auto']">
          <div class="basis-1/3">
            <div class="text-[20px] stroke-2 hover:cursor-pointer hover:text-sky-500"
                 @click="router.push(`/g/Song?id=${v.id}`)"
            >{{v.title}}
            </div>
          </div>
          <div :class="c_row">
            <el-text line-clamp="1" class="hover:cursor-pointer hover:text-sky-500"
                     @click="router.push(`/g/Album?id=${v.album.id}`)"
            >{{v.album.title}}</el-text>
          </div>
          <el-icon><Play48Filled class="hover:text-blue-500 hover:cursor-pointer"
            @click="player.load_play(v)"
          /></el-icon>
        </div>
      </div>
    </el-tab-pane>

    <el-tab-pane label="所有专辑" name="所有专辑">
      <div v-for="(v) in data.albums" :class="[c_row, '*:m-2 mx-8',
      'hover:bg-sky-200 rounded-3xl']">
        <div class="size-20">
          <el-image :src="v.background" class="size-20 rounded-[30px]"/>
        </div>
        <div :class="[c_col, 'basis-auto']">
          <div class="basis-1/3">
            <div class="text-[20px] stroke-2 hover:cursor-pointer hover:text-sky-500"
                 @click="router.push(`/g/Album?id=${v.id}`)"
            >{{v.title}}</div>
          </div>
          <div :class="c_row">
            <el-text line-clamp="2" class="hover:cursor-pointer hover:text-sky-500"
                     @click="router.push(`/g/Album?id=${v.id}`)"
            >{{v.description}}</el-text>
          </div>
        </div>
      </div>
    </el-tab-pane>

    <el-tab-pane label="相关MV" name="相关MV">
      <div v-for="(v) in data.videos" :class="[c_row, '*:m-2 mx-8',
      'hover:bg-sky-200 rounded-3xl']">
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
    </el-tab-pane>

    <el-tab-pane label="艺人介绍" name="艺人介绍">
      <p class="*:m-2 mx-8">{{data.description}}</p>
    </el-tab-pane>
  </el-tabs>
  <div class="flex justify-center">
  </div>


</template>

<style scoped>

</style>