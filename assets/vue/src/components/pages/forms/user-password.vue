<script setup lang="ts">
import {ref} from "vue";
import {get} from "@/components/utils/http";

let form = ref({})

let is_sended = ref(false)
let send = async ()=>{
  console.log('send')
  await get(`email/`,{email: form.value.email})
      .then(()=>{
        is_sended.value = true
        setTimeout(()=>is_sended.value=false,60000)
      })
}
</script>

<template>
  <el-form class="flex flex-col" inline>
    <el-form-item label="新密码" prop="password">
      <el-input v-model="form.password" type="password"></el-input>
    </el-form-item>
    <el-form-item label="邮箱" prop="email"
                  :rules="[{validator: ()=>/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(form.email), message: '邮箱不合法'}]">
      <el-input v-model="form.email"></el-input>
    </el-form-item>
    <el-form-item label="验证码" prop="token" :rules="[]">
      <el-input v-model="form.token" :disabled="!is_sended"></el-input>
      <el-button @click="send" style="float: right">发送验证码</el-button>
    </el-form-item>
    <el-button>修改密码</el-button>
  </el-form>

</template>

<style scoped>

</style>