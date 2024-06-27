<script setup lang="ts">
import {useRouter,useRoute,useLink} from 'vue-router'
let route = useRoute(), router = useRouter()
import {get} from '@/components/utils/http'

import {watchEffect,ref} from 'vue'
import {DotCircleRegular} from "@vicons/fa";
let data = ref([])
let close_handle = watchEffect(async () => {
  // const id = route.query.id ? route.query.id : localStorage.getItem('id')
  get(`e-Recommends/`).then(res => data.value = res)
})

let c_row = 'flex flex-row', c_col = 'flex flex-col'
let c_hover = 'hover:text-sky-500 hover:cursor-pointer'
</script>

<template>
  <el-carousel height="300px" arrow="always" direction="horizontal" type="card">
    <el-carousel-item v-for="(v) in ['cIF0zVh9LdoKYMGHGChD2g==/109951169457307033.jpg','RJclxzQoZ4PqAoF8VdkKRg==/109951169457307633.jpg',
  'ahTmwbFHsTrXvkpDZhT5yQ==/109951169456971307.jpg','iArWYllwWXYm6GWPkaVSaw==/109951169457543712.jpg','OyYaLj9JBivdUYsPT9DELA==/109951169456989019.jpg',
  '2JSQ0um8RMTDk1qzkhH-vA==/109951169456987218.jpg','6X8kP26YkneLIqn4wmwj3Q==/109951169456993616.jpg']">
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