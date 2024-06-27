<script setup lang="ts">
import {inject} from 'vue'
// let conf = inject('conf')

import {useTheme,useTest} from '@/components/stores'
let theme = useTheme(), player = useTest()
</script>

<template>
  <h1>设置</h1>
  <el-divider></el-divider>
  <el-row align="middle" justify="center">
    <el-col :span="4">侧边栏</el-col>
    <el-col :span="20"><el-switch v-model="theme.fold" active-text="展开" inactive-text="折叠" inline-prompt></el-switch></el-col>
  </el-row>
  <el-row align="middle" justify="center">
    <el-col :span="4">模式</el-col>
    <el-col :span="20"><el-switch v-model="theme.light" active-text="亮模式" inactive-text="暗模式" inline-prompt label="主题"></el-switch></el-col>
  </el-row>
  <el-row align="middle">
    <el-col :span="4">音量</el-col>
    <el-col :span="12"><el-slider v-model="player.vol"></el-slider></el-col>
  </el-row>
  <el-row align="middle">
    <el-col :span="4">播放速度</el-col>
    <el-col :span="12"><el-slider v-model="player.rate" :max="5" :step="0.01"></el-slider></el-col>
  </el-row>
</template>

<style scoped>

</style>