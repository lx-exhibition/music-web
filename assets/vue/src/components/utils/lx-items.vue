<script setup lang="ts">
import LxItem from "@/components/utils/lx-item.vue";
import {ArrowRight} from '@element-plus/icons-vue'

import {defineProps,useAttrs} from 'vue'
let props = defineProps(['title','priObjs','subObjs','imgs','vertical'])

let title: string, pri_objs: object[], sub_objs: object[], imgs : string[], vertical: boolean
title = props.title ? props.title : '相关推荐'
pri_objs = props.priObjs? props.priObjs : [{title: 'example title', path: '#example/path', id: '114514'}]
sub_objs = props.subObjs ? props.subObjs : [{title: 'example subtitle', path: '#example/sub-path', id: '114514'}]
imgs = props.imgs ? props.imgs : ['https:/example/to/img']
vertical = !!props.vertical
let path = pri_objs[0] && pri_objs[0].path ? pri_objs[0].path : '#example/path'


</script>

<template>
  <el-card shadow="hover" style="width: 200px">
    <template #header>
      <el-row align="middle">
        <el-col :span="17"><strong>{{title}}</strong></el-col>
        <el-col :span="7" style="font-size: 10px">
          <el-link :underline="false" :href="path">更多<el-icon><arrow-right/></el-icon></el-link>
        </el-col>
      </el-row>
    </template>
    <lx-item v-for="(v,i) in pri_objs.length" :pri="pri_objs[i]" :sub="sub_objs[i]" :img="imgs[i]" :vertical="vertical"
      style="margin-top: 10px"/>
  </el-card>
</template>

<style scoped>

</style>