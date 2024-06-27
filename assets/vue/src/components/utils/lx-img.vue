<script setup>
import {defineProps, shallowRef} from 'vue'
import {Error,ErrorFilled} from '@vicons/carbon'
let props = defineProps(['images'])
let imgs = Object.assign([], props.images)

if (imgs.constructor !== Array){
  imgs = [Error,ErrorFilled]
}else {
  if (!imgs[0]) imgs[0] = Error
  if (!imgs[1]) imgs[1] = ErrorFilled
}

let cur = shallowRef(imgs[0])
</script>

<template>
  <el-link style="color: white" :underline="false" :icon="cur" @mouseenter="cur=imgs[1]" @mouseleave="cur=imgs[0]"></el-link>
</template>

<style scoped>

</style>