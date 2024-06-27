<script setup lang="ts">

import LxItem from "@/components/utils/lx-item.vue";
import {paginate} from './tool'

import {defineProps} from 'vue'
let props = defineProps(['title','priObjs','subObjs','imgs','vertical'])

let title: string, pri_objs: object[] = [], sub_objs: object[] = [], imgs: string[] = []
title = props.title ? props.title : '相关推荐'
pri_objs = props.priObjs? props.priObjs : [{title: 'example title', path: '#example/path', id: '114514'}]
sub_objs = props.subObjs ? props.subObjs : [{title: 'example subtitle', path: '#example/sub-path', id: '114514'}]
imgs = props.imgs ? props.imgs : ['https:/example/to/img']

let page_size = 5
let pag = paginate(pri_objs, page_size)

</script>

<template>
  <el-card>
    <h1>{{title}}</h1>
    <el-divider/>
    <el-carousel indicator-position="outside" :autoplay='false' >
      <el-carousel-item v-for="(v,i) in pag" :label="`page ${i+1}`">
        <el-row justify="center" style="position: relative;top: 80px">
          <el-col v-for="(w,j) in v" :span="4">
            <lx-item :pri="pri_objs[page_size*i+j]" :sub="sub_objs[page_size*i+j]"
                     :img="imgs[page_size*i+j]" :vertical="true"
            />
          </el-col>
        </el-row>
      </el-carousel-item>
    </el-carousel>
  </el-card>
</template>

<style scoped>

</style>