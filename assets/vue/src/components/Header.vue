<template>
  <el-menu :default-active="route.fullPath" mode="horizontal" router style="height: 100%; border: 1rem"
           :background-color="theme.bg" :text-color="theme.text"
  >

    <el-menu-item index="/">
      <el-avatar src="http://localhost:8001/media/logo.ico" alt="logo" size="large"></el-avatar>
    </el-menu-item>
    <el-sub-menu index="/explore">
      <template #title>发现音乐</template>
<!--      , ['DJ','主播电台']-->
      <el-menu-item v-for="v in [['Recommends','推荐'], ['Ranks','排行榜'], ['PlayLists','歌单'],
        ['Artists','歌手'], ['Albums','新碟上架']]" :index="`/explore/${v[0]}`">{{v[1]}}</el-menu-item>
    </el-sub-menu>
    <el-sub-menu index="/my">
      <template #title>我的</template>
      <el-menu-item v-for="v in [['Artists','我的歌手'], ['Videos','我的视频'], ['DJs','我的电台'],
        ['CreatedSongLists','创建的歌单'], ['CollectedSongLists','收藏的歌单']]" :index="`/my/${v[0]}`">{{v[1]}}</el-menu-item>
    </el-sub-menu>
    <el-menu-item v-for="(v,i) in [['Friends','关注'], ['Market','商城'], ['Artist','音乐人'], ['Advanced','云推歌'],
      ['Client','下载客户端']]" :index="`/other/${v[0]}`" :key="i">{{v[1]}}</el-menu-item>

    <div style="flex-grow: 0.8;"/>
    <el-input v-model="search" placeholder="音乐/视频/歌单/用户" class="h-8 w-56 self-center"
                     @keydown="(e)=>{e.keyCode===13?router.push(`/Search?s=${search}`):0}">
      <template #suffix><el-link :icon="Search" :underline="false"
                                 @click="router.push(`/Search?s=${search}`)"
      ></el-link></template>
    </el-input>

    <div style="flex-grow: 0.1;"/>

    <el-row align="middle">
      <el-button round @click="router.push('/g/Artist')">创作者中心</el-button>
    </el-row>

    <div style="flex-grow: 0.09;"/>


    <el-sub-menu index="/person">
      <template #title>
<!--        <el-badge :value="123">-->
<!--          <el-avatar src="http://p3.music.126.net/E0hOSpWP4XBov9hsO5KJBA==/109951165422241301.jpg" alt="头像" size="default"></el-avatar>-->
          <el-avatar :src="`http://localhost:8001/rest/img-user/?id=${uid}`" alt="头像" size="default"></el-avatar>
<!--        </el-badge>-->
      </template>
      <el-menu-item v-for="v in [['home','我的主页',InprivateAccount16Regular], ['messages','我的消息',EmailOutlined],
        ['degree','我的等级',Medal], ['vip','vip会员',Smoking], ['settings','个人设置',Settings48Regular],
        ['authorization','实名认证',OfficeBuilding], ['logout','退出',DoorExit]]" :index="`/my/${v[0]}`"
      >
        <el-link :icon="v[2]" :underline="false">{{v[1]}}</el-link>
      </el-menu-item>
    </el-sub-menu>

    <div style="flex-grow: 0.01;"/>
    <div style="flex-grow: 0.01;"/>
    <div style="flex-grow: 0.01;"/>
    <div style="flex-grow: 0.01;"/>


    <el-menu direction="vertical">
      <el-menu-item :index="`${i}`" v-for="(v,i) in dialogs" @click="v.open = true">
        {{v.label}}
      </el-menu-item>
    </el-menu>
  </el-menu>

  <el-dialog v-for="(v) in dialogs" v-model="v.open">
    <component :is="v.component"/>
  </el-dialog>
</template>

<script setup lang="ts">
import {
  Settings32Regular, InprivateAccount16Regular, Settings48Regular,
} from '@vicons/fluent'
import {DoorExit} from "@vicons/tabler";
import {Medal, OfficeBuilding, Smoking, Search} from "@element-plus/icons-vue";
import {EmailOutlined} from "@vicons/material";

import {ref} from 'vue'
import {useRoute,useRouter} from 'vue-router'
let route = useRoute(), router = useRouter()

let search = ref('')



import {reactive,markRaw} from 'vue'
import Register from '@/components/pages/forms/user-create.vue'
import Login from '@/components/pages/forms/user-login.vue'
import Password from '@/components/pages/forms/user-password.vue'
import Artist from '@/components/pages/forms/user-artist.vue'
import Setting from '@/components/Settings.vue'
let dialogs = reactive([
  {component: markRaw(Register), label: '注册', open: false},
  {component: markRaw(Login), label: '登录', open: false},
  {component: markRaw(Password), label: '修改密码', open: false},
  {component: markRaw(Artist), label: '入驻歌手', open: false},
  {component: markRaw(Setting), label: '设置', open: false},
])


let uid = localStorage.getItem('id')


import {useTheme} from '@/components/stores.js'
let theme = useTheme()
</script>



<style scoped>

</style>