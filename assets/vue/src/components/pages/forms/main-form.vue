<template>
  <el-tabs v-model="sel">
<!--    <el-tab-pane v-for="v in components" :label="v[1]" :name="v[1]">-->
<!--      <component :is="v[0]"/>-->
<!--    </el-tab-pane>-->
    <el-tab-pane label="test" name="测试">
      <component :is="Test"/>
    </el-tab-pane>
  </el-tabs>

<!--  <iframe class="w-1/2 aspect-square md:aspect-video rounded-lg shadow-lg" src="https://www.youtube.com/embed/dQw4w9WgXcQ"-->
<!--          frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"-->
<!--          allowfullscreen=""></iframe>-->
</template>

<script setup lang="ts">
import {ref} from 'vue'

import User from './user-form.vue'
import Register from './user-create.vue'
import Test from './test.vue'
let sel = ref('测试')
let components = [
  [User,'用户'],
  [Register,'注册'],
  [Test,'测试'],
]

import {use_counter} from './pi'


</script>


<style scoped>

</style>