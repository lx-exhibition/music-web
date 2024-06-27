<script setup lang="ts">
import {useRouter,useRoute,useLink} from 'vue-router'
let route = useRoute(), router = useRouter()
import {get} from '@/components/utils/http'

import {watchEffect,ref} from 'vue'
import {DotCircleRegular} from "@vicons/fa";
let data = ref([])
let close_handle = watchEffect(async () => {
  get(`e-Recommends/`).then(res => data.value = res)
})

let c_row = 'flex flex-row', c_col = 'flex flex-col'
let c_hover = 'hover:text-sky-500 hover:cursor-pointer'
</script>

<template>
  <el-carousel height="300px" arrow="always" direction="horizontal" type="card">
    <el-carousel-item v-for="(v) in ['pFT6zNHNOT7KktcjWVky8A==/109951169597296396.jpg','vpY55ZszhRTgApsqiZbgIQ==/109951169595275862.jpg',
  '6_6huShmciSwl2s4bSd41Q==/109951169597267586.jpg','XxL3rHs4SH0SF441cX80Ig==/109951169595285757.jpg','u3FhzU_gpXhL_tKIa20-yQ==/109951169595289778.jpg',
  'HAQnvcfIOnQ_lng0Y_lVLg==/109951169597166568.jpg','0HvRNWwfEmB7h-i-0ushvg==/109951169595451697.jpg']">
      <img :src="`http://p1.music.126.net/${v}?imageView&quality=89`" style="height: 100%"/>
    </el-carousel-item>
  </el-carousel>

  <el-card shadow="hover">
    <template #header>
      <el-row align="middle">
        <el-col :span="1">
          <el-icon><DotCircleRegular/></el-icon>
        </el-col>
        <el-col :span="6">
          <el-link :underline="false" @click="router.push('/explore/Albums')"><h1>最新专辑</h1></el-link>
        </el-col>
        <el-col :span="17">
          <el-space spacer="|" alignment="center">
            <el-link v-for="(v) in data.album_tag" @click="router.push(`/explore/Albums?tag=${v}`)"
            >{{v}}</el-link>
          </el-space>
        </el-col>
      </el-row>
    </template>
    <template #default>
      <div class="grid grid-cols-5">
        <el-card v-for="(v) in data.albums" :class="[c_col,'w-36 h-40 drop-shadow-2xl wrap mt-4', c_hover]" shadow="hover"
                 @click="router.push(`/g/Album?id=${v.id}`)"
        >
          <img class="size-24 object-cover mx-auto rounded-xl " :src="v.background"/>
          <span :class="[c_row, 'justify-center text-[12px] mt-2']">{{v.title}}</span>
        </el-card>
      </div>
    </template>
    <template #footer>
      <div :class="[c_row, c_hover, 'justify-center']"
           @click="router.push('/explore/Albums')"
      >更多</div>
    </template>
  </el-card>

  <el-card shadow="hover">
    <template #header>
      <el-row align="middle">
        <el-col :span="1">
          <el-icon><DotCircleRegular/></el-icon>
        </el-col>
        <el-col :span="6">
          <el-link :underline="false" @click="router.push('/explore/PlayLists')"><h1>最新歌单</h1></el-link>
        </el-col>
        <el-col :span="17">
          <el-space spacer="|" alignment="center">
            <el-link v-for="(v) in data.play_tag" @click="router.push(`/explore/PlayLists?tag=${v}`)"
            >{{v}}</el-link>
          </el-space>
        </el-col>
      </el-row>
    </template>
    <template #default>
      <div class="grid grid-cols-5">
        <el-card v-for="(v) in data.playlists" :class="[c_col,'w-36 h-40 drop-shadow-2xl wrap mt-4', c_hover]" shadow="hover"
                 @click="router.push(`/g/PlayList?id=${v.id}`)"
        >
          <img class="size-24 object-cover mx-auto rounded-xl " :src="v.img"/>
          <span :class="[c_row, 'justify-center text-[12px] mt-2']">{{v.title}}</span>
        </el-card>
      </div>
    </template>
    <template #footer>
      <div :class="[c_row, c_hover, 'justify-center']"
           @click="router.push('/explore/PlayLists')"
      >更多</div>
    </template>
  </el-card>

  <el-card shadow="hover">
    <template #header>
      <el-row align="middle">
        <el-col :span="1">
          <el-icon><DotCircleRegular/></el-icon>
        </el-col>
        <el-col :span="6">
          <el-link :underline="false" @click="router.push('/explore/Artists')"><h1>最新入住歌手</h1></el-link>
        </el-col>
        <el-col :span="17">
          <el-space spacer="|" alignment="center">
            <el-link v-for="(v) in data.artist_tag" @click="router.push(`/explore/Artists?tag=${v}`)"
            >{{v}}</el-link>
          </el-space>
        </el-col>
      </el-row>
    </template>
    <template #default>
      <div class="grid grid-cols-5">
        <el-card v-for="(v) in data.artists" :class="[c_col,'w-36 h-40 drop-shadow-2xl wrap mt-4', c_hover]" shadow="hover"
                 @click="router.push(`/g/PlayList?id=${v.id}`)"
        >
          <img class="size-24 object-cover mx-auto rounded-xl " :src="v.background"/>
          <span :class="[c_row, 'justify-center text-[12px] mt-2']">{{v.stagename}}</span>
        </el-card>
      </div>
    </template>
    <template #footer>
      <div :class="[c_row, c_hover, 'justify-center']"
           @click="router.push('/explore/Artists')"
      >更多</div>
    </template>
  </el-card>
</template>

<style scoped>

</style>
