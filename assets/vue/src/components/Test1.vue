
<template>
  <el-button style="height: 100px;width: 100px" ref="btn">个几把</el-button>
  <input>
</template>

<script setup>
import {useRouter,useLink,useRoute} from 'vue-router'
let router = useRouter(), route = useRoute()
// router.back()
// console.log(route.matched)
// console.log(route.hash)
// console.log(route.fullPath)
console.log(route.query)
// console.log(route.redirectedFrom)
// console.log(route.params)
// console.log(route.path)

import {onMounted,ref,inject,defineEmits} from 'vue'

let btn = ref()
onMounted(()=>{
  // ['click', 'dblclick', 'mousedown', 'mouseup', 'mouseenter', 'mouseleave', 'mouseover', 'mouseout', 'mousemove', 'auxclick']
  //   .forEach((v,i,arr)=>{
  //     btn.value.$el.addEventListener(v,()=>{console.log(v)})
  //   })

})

</script>

<style scoped>

</style>