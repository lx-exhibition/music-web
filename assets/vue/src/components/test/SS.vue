<template>
  <el-scrollbar style="height: 500px">
    <el-image v-for="v in imgs" :src="v" style="display: block"></el-image>
  </el-scrollbar>
  <!--  <el-image-viewer :url-list="imgs">-->
  <!--  </el-image-viewer>-->
</template>

<script setup>
import TestForm from "@/components/pages/forms/main-form.vue";

import {inject,ref} from 'vue'
let conf = inject('conf')
let imgs = []
for (let i = 0; i < 20; i++) {
  let idx = Math.floor(2000*Math.random())
  let img = conf.value.imgs[idx]
  imgs.push(img)
}
imgs = imgs.map((v)=>`http://localhost:8001/img/${v}`)
console.log(imgs)

</script>

<style scoped>

</style>