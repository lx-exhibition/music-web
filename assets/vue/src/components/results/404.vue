<script setup>
import {ref} from 'vue'
let back = ()=>{
  history.back()
}
</script>

<template>
  <el-result title="注销成功">
    <template #icon>
      <el-image
          src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
      />
    </template>
    <template #extra>
      <el-button type="primary" @click="back">Back</el-button>
    </template>
  </el-result>
</template>

<style scoped>

</style>