<script setup lang="ts">
import {VideoPause, VideoPlay} from "@element-plus/icons-vue"
import {PlaySkipBackOutline,PlaySkipForwardOutline} from '@vicons/ionicons5'

import {computed} from 'vue'
import {useRouter,useRoute} from 'vue-router'
let route = useRoute(), router = useRouter()
let c_row = 'flex flex-row', c_col = 'flex flex-col'
let c_hover = 'hover:text-blue-500 hover:cursor-pointer'

import {useTest} from '@/components/stores'
let p = useTest()
let icon = computed(()=>p.playing ? VideoPlay : VideoPause)
</script>

<template>
  <div :class="[c_row, 'bg-gray-300 text-black h-full rounded-3xl justify-center place-items-center']">
    <el-button round :icon="PlaySkipBackOutline"></el-button>
    <el-button round :icon="icon" @click="p.flip()"></el-button>
    <el-button round :icon="PlaySkipForwardOutline"></el-button>
    <img :src="p.song.img" :class="['size-11 rounded-full ml-4', p.c_circle]">

    <p class="w-3/12 ml-2"><el-progress :percentage="p.percentage" :format="()=>(`${p.time}/${p.total}`)"/></p>
    <p v-if="p.song" :class="[c_hover, 'mx-2']" @click="router.push(`/g/Song?id=${p.song.id}`)">{{p.song.title}}</p> /
    <p v-if="p.song.artist" :class="[c_hover, 'mx-2']" @click="router.push(`/g/Artist?id=${p.song.artist.id}`)">{{p.song.artist.stagename}}</p>
  </div>
</template>

<style scoped>

</style>