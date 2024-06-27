<script setup lang="ts">
import {useRoute,useRouter} from 'vue-router'
let route = useRoute(), router = useRouter()
import {get} from '@/components/utils/http'

import {watchEffect,ref} from 'vue'
let data = ref({})
let close_handle = watchEffect(async () => {
  const s = route.query.s
  get(`g-Search/`, {s: s}).then(res => data.value = res)
})

let c_hover = 'hover:text-cyan-500 hover:cursor-pointer'

let tabs = ref('歌曲')
</script>

<template>
  <el-tabs v-model="tabs">
    <el-tab-pane label="歌曲" name="歌曲">
      <el-table :data="data.songs">
        <el-table-column label="歌名">
          <template #default="{row}"><p :class="c_hover" @click="router.push(`/g/Song?id=${row.id}`)"
          >{{row.title}}</p></template>
        </el-table-column>
        <el-table-column label="歌手">
          <template #default="{row}"><p :class="c_hover" @click="router.push(`/g/Artist?id=${row.artist.id}`)"
          >{{row.artist.stagename}}</p></template>
        </el-table-column>
        <el-table-column prop="liked_count" label="点赞数"/>
        <el-table-column prop="shared_count" label="分享数"/>
      </el-table>
    </el-tab-pane>
    <el-tab-pane label="视频" name="视频">
      <el-table :data="data.videos">
        <el-table-column label="视频名">
          <template #default="{row}"><p :class="c_hover" @click="router.push(`/g/Video?id=${row.id}`)"
          >{{row.title}}</p></template>
        </el-table-column>
        <el-table-column label="用户">
          <template #default="{row}"><p :class="c_hover" @click="router.push(`/my/Home?id=${row.user.id}`)"
          >{{row.user.nickname}}</p></template>
        </el-table-column>
        <el-table-column prop="liked_count" label="点赞数"/>
        <el-table-column prop="shared_count" label="分享数"/>
      </el-table>
    </el-tab-pane>
    <el-tab-pane label="专辑" name="专辑">
      <el-table :data="data.albums">
        <el-table-column label="专辑名">
          <template #default="{row}"><p :class="c_hover" @click="router.push(`/g/Album?id=${row.id}`)"
          >{{row.title}}</p></template>
        </el-table-column>
        <el-table-column label="歌手">
          <template #default="{row}"><p :class="c_hover" @click="router.push(`/g/Artist?id=${row.artist.id}`)"
          >{{row.artist.stagename}}</p></template>
        </el-table-column>
        <el-table-column prop="liked_count" label="点赞数"/>
        <el-table-column prop="shared_count" label="分享数"/>
      </el-table>
    </el-tab-pane>
    <el-tab-pane label="歌单" name="歌单">
      <el-table :data="data.playlists">
        <el-table-column label="歌单名">
          <template #default="{row}"><p :class="c_hover" @click="router.push(`/g/PlayList?id=${row.id}`)"
          >{{row.title}}</p></template>
        </el-table-column>
        <el-table-column label="用户">
          <template #default="{row}"><p :class="c_hover" @click="router.push(`/my/Home?id=${row.user.id}`)"
          >{{row.user.nickname}}</p></template>
        </el-table-column>
        <el-table-column prop="liked_count" label="点赞数"/>
        <el-table-column prop="shared_count" label="分享数"/>
      </el-table>
    </el-tab-pane>
    <el-tab-pane label="歌手" name="歌手">
      <el-table :data="data.artists">
        <el-table-column label="艺名">
          <template #default="{row}"><p :class="c_hover" @click="router.push(`/g/Artist?id=${row.id}`)"
          >{{row.stagename}}</p></template>
        </el-table-column>
        <el-table-column label="描述">
          <template #default="{row}">
            <el-text :line-clamp="2">{{row.description}}</el-text>
          </template>
        </el-table-column>
      </el-table>
    </el-tab-pane>
    <el-tab-pane label="用户" name="用户">
      <el-table :data="data.users">
        <el-table-column label="用户名">
          <template #default="{row}"><p :class="c_hover" @click="router.push(`/my/Home?id=${row.id}`)"
          >{{row.nickname}}</p></template>
        </el-table-column>
        <el-table-column label="粉丝数" prop="fans.length"/>
        <el-table-column label="性别">
          <template #default="{row}">{{row.gender==0 ? '未知' :(row.gender==1 ? '男' : '女')}}</template>
        </el-table-column>
        <el-table-column label="github">
          <template #default="{row}"><el-link :href="row.github" target="_blank">{{row.github}}</el-link></template>
        </el-table-column>
      </el-table>
    </el-tab-pane>
  </el-tabs>
</template>

<style scoped>

</style>