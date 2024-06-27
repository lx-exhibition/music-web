<script setup>
import {useRouter,useRoute,useLink} from 'vue-router'
let route = useRoute(), router = useRouter()
import {get} from '@/components/utils/http'

import {watchEffect,ref} from 'vue'
import {DotCircleRegular} from "@vicons/fa";
let data = ref([])
let close_handle = watchEffect(async () => {
  const tag = route.query.tag
  const subtag = route.query.subtag
  get(`e-PlayLists/`, {tag: tag, subtag: subtag}).then(res => data.value = res)
})

let c_row = 'flex flex-row', c_col = 'flex flex-col'
let c_hover = 'hover:text-sky-500 hover:cursor-pointer'
</script>

<template>

  <el-card shadow="hover">
    <template #header>
      <el-row align="middle">
        <el-col :span="1">
          <el-icon><DotCircleRegular/></el-icon>
        </el-col>
        <el-col :span="1">
          <el-link :underline="false" @click="router.push('/explore/PlayLists')"><h1>歌单</h1></el-link>
        </el-col>
        <el-col :span="22">
          <el-tag v-for="(v) in data.tags" class="mx-2 hover:cursor-pointer" @click="router.push(`/explore/PlayLists?tag=${v.subtag}`)"
          >{{v.subtag}}</el-tag>
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
  </el-card>
</template>

<style scoped>

</style>