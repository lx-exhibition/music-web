<script setup lang="ts">
import {defineProps,useAttrs} from 'vue'
let props = defineProps(['pri', 'sub', 'img', 'vertical'])
let pri: object, sub: object, img: string, vertical: boolean
pri = props.pri ? props.pri : {title: 'example title', path: '#example/path', id: '114514'}
sub = props.sub ? props.sub : {title: 'example subtitle', path: '#example/sub-path', id: '114514'}
img = props.img ? props.img : 'https:/example/to/img'
vertical = !!props.vertical

</script>

<template>
  <el-row style="width: 200px; height: 50px" v-if="!vertical">
    <el-col :span="7">
      <el-link :href="`${pri.path}?id=${pri.id}`">
        <template #icon><img :src="img" style="width: 50px; height: 50px; object-fit: cover"/></template>
      </el-link>
    </el-col>
    <el-col :span="17">
      <el-row align="middle" style="height: 30px">
        <el-link :href="`${pri.path}?id=${pri.id}`" :underline="false"><strong>{{pri.title}}</strong></el-link>
      </el-row>
      <el-row align="middle" style="height: 20px">
        <el-link :href="`${sub.path}?id=${sub.id}`" :underline="false" style="font-size: 10px">by {{sub.title}}</el-link>
      </el-row>
    </el-col>
  </el-row>

  <el-col style="width: 100px; height: 150px" v-else>
    <el-row>
      <el-link :href="`${pri.path}?id=${pri.id}`">
        <template #icon><img :src="img" style="width: 100px; height: 100px; object-fit: cover"/></template>
      </el-link>
    </el-row>
    <el-row justify="center" style="height: 30px">
      <el-link :href="`${pri.path}?id=${pri.id}`" :underline="false"><strong>{{pri.title}}</strong></el-link>
    </el-row>
    <el-row justify="center" style="height: 20px">
      <el-link :href="`${sub.path}?id=${sub.id}`" :underline="false" style="font-size: 10px">by {{sub.title}}</el-link>
    </el-row>
  </el-col>
</template>

<style scoped>

</style>