<script setup>

import {ref} from 'vue'
import {post} from '@/components/utils/http'
let form = ref({username: '', password: ''})

let on_login = ()=>{
  post('login/', form.value).then(res => {
    localStorage.setItem('id', res.id)
    localStorage.setItem('aid', res.aid)
    location.reload()
  })
}
</script>

<template>
  <div class="flex flex-col">
    <el-form-item label="用户名">
      <el-input v-model="form.username"></el-input>
    </el-form-item>
    <el-form-item label="密码">
      <el-input v-model="form.password" type="password"></el-input>
    </el-form-item>
    <el-button type="primary" @click="on_login" class="self-center">登录</el-button>
  </div>
</template>

<style scoped>

</style>