<template>
  <el-menu :default-active="route.fullPath" mode="vertical" router :collapse="theme.fold" menu-trigger="click"
           :background-color="theme.bg" :text-color="theme.text"
  >
    <el-sub-menu @click="theme.fold=!theme.fold"
     :expand-open-icon="ArrowLeft" :expand-close-icon="ArrowLeft" index=""
    >
    <template #title>
      <el-icon><fold v-if="theme.fold"/><expand v-else/></el-icon>
      <span>展开/折叠</span>
    </template>
    </el-sub-menu>

<!--['DJs','我的电台',AudioDescription],-->
    <el-sub-menu v-for="v in [['Artists','我的歌手',PersonAvailable20Regular], ['Videos','我的视频',Video16Regular],
    ['CreatedSongLists','创建的歌单',Album20Regular], ['CollectedSongLists','收藏的歌单',AudiotrackSharp],
    ['Messages','我的消息',MessageOutlined], ['Home','我的主页',BuildingHome16Regular], ['Settings','设置',Setting]
            ]" :index="`/my/${v[0]}`"
                 :popper-append-to-body="false" :teleported="true"
                 @click="router.push(`/my/${v[0]}`)"
    >
      <template #title><el-icon><component :is="v[2]"></component></el-icon><span>{{v[1]}}</span></template>
    </el-sub-menu>

  </el-menu>
</template>

<script setup lang="ts">
import {Setting, ArrowLeft, Expand, Fold} from "@element-plus/icons-vue";
import {Album20Regular,BuildingHome16Regular,PersonAvailable20Regular,Video16Regular,
} from '@vicons/fluent'
import {MessageOutlined} from '@vicons/antd'
import {AudiotrackSharp} from '@vicons/material'

import {useRoute,useRouter} from 'vue-router'
let route = useRoute(), router = useRouter()
import {useTheme} from '@/components/stores.js'
let theme = useTheme()

</script>

<style scoped>

</style>