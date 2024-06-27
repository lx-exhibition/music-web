<script setup>
import {LocalFireDepartmentFilled} from '@vicons/material'
import {ShareAlt} from '@vicons/fa'
import {ThumbLike16Filled} from '@vicons/fluent'

import {useRouter,useRoute,useLink} from 'vue-router'
let route = useRoute(), router = useRouter()
import {get} from '@/components/utils/http'

import {watchEffect,ref} from 'vue'
let data = ref([])
let close_handle = watchEffect(async () => {
  get(`e-Ranks/`).then(res => data.value = res)
})

let c_row = 'flex flex-row', c_col = 'flex flex-col'
let c_hover = 'hover:text-sky-500 hover:cursor-pointer'

let tabs = ref('songs')
</script>

<template>
  <el-tabs v-model="tabs">
    <el-tab-pane name="songs" label="热歌榜">
      <div v-for="(v) in data.songs" :class="[c_row, 'mt-2 justify-between mx-8 hover:bg-sky-200 rounded-2xl']">
        <img :src="v.img" class="size-24 rounded-2xl ">
        <span :class="[c_hover, 'self-center ml-32']"
          @click="router.push(`/g/Song?id=${v.id}`)"
        >{{v.title}}</span>
        <span class="self-center ml-2"><span class="text-[12px]">点赞数:</span> {{v.liked_count}}
          <el-icon><ThumbLike16Filled class="text-orange-500"/></el-icon>
        </span>
        <span class="self-center ml-2"><span class="text-[12px]">分享数:</span> {{v.shared_count}}
          <el-icon><ShareAlt class="text-sky-500"/></el-icon>
        </span>
        <span class="self-center ml-2"><span class="text-[12px]">热度:</span> {{10*v.liked_count+v.shared_count}}
          <el-icon><LocalFireDepartmentFilled class="text-red-500"/></el-icon>
        </span>
      </div>
    </el-tab-pane>
    <el-tab-pane name="albums" label="热门专辑">
      <div v-for="(v) in data.albums" :class="[c_row, 'mt-2 justify-between mx-8 hover:bg-sky-200 rounded-2xl']">
        <img :src="v.background" class="size-24 rounded-2xl ">
        <span :class="[c_hover, 'self-center ml-32']"
              @click="router.push(`/g/Album?id=${v.id}`)"
        >{{v.title}}</span>
        <span class="self-center ml-2"><span class="text-[12px]">点赞数:</span> {{v.liked_count}}
          <el-icon><ThumbLike16Filled class="text-orange-500"/></el-icon>
        </span>
        <span class="self-center ml-2"><span class="text-[12px]">分享数:</span> {{v.shared_count}}
          <el-icon><ShareAlt class="text-sky-500"/></el-icon>
        </span>
        <span class="self-center ml-2"><span class="text-[12px]">热度:</span> {{10*v.liked_count+v.shared_count}}
          <el-icon><LocalFireDepartmentFilled class="text-red-500"/></el-icon>
        </span>
      </div>
    </el-tab-pane>
    <el-tab-pane name="songlists" label="热门歌单">
      <div v-for="(v) in data.playlists" :class="[c_row, 'mt-2 justify-between mx-8 hover:bg-sky-200 rounded-2xl']">
        <img :src="v.img" class="size-24 rounded-2xl ">
        <span :class="[c_hover, 'self-center ml-32']"
              @click="router.push(`/g/PlayList?id=${v.id}`)"
        >{{v.title}}</span>
        <span class="self-center ml-2"><span class="text-[12px]">点赞数:</span> {{v.liked_count}}
          <el-icon><ThumbLike16Filled class="text-orange-500"/></el-icon>
        </span>
        <span class="self-center ml-2"><span class="text-[12px]">分享数:</span> {{v.shared_count}}
          <el-icon><ShareAlt class="text-sky-500"/></el-icon>
        </span>
        <span class="self-center ml-2"><span class="text-[12px]">热度:</span> {{10*v.liked_count+v.shared_count}}
          <el-icon><LocalFireDepartmentFilled class="text-red-500"/></el-icon>
        </span>
      </div>
    </el-tab-pane>
  </el-tabs>


</template>

<style scoped>

</style>