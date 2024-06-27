<script setup lang="ts">
import {FormInstance} from 'element-plus'
import {ref,reactive,toRaw} from 'vue'
let form = ref({}), form_ref = ref<FormInstance>(), form_data = ref({})
import {get,post,post_f} from '@/components/utils/http'
let is_sended = ref(false)

let locations = reactive([])
get('Location/').then(res => {
  locations = res.data.map((v)=>({label: v.location,value: v.id}))
})

let send = async ()=>{
  console.log('send')
  await get(`email/`,{email: form.value.email})
      .then(()=>{
        is_sended.value = true
        setTimeout(()=>is_sended.value=false,60000)
      })
}
let register = async ()=>{
  console.log('register')
  try {
    form.value.avatar = form_data.value.avatar[0].raw
  }catch (e){console.log('文件未上传')}
  // console.log(form)
  await post_f(`register/?time=${new Date().getTime()}`, form.value)
}
let login = async ()=>{
  console.log(form.value)
  await post(`login/`, form.value).then(res => {
    localStorage.setItem('id', res.id)
    localStorage.setItem('aid', res.aid)
  })
}

let steps = ref(0)
let f = ref(),preview = ref(false)

import axios from 'axios'
</script>

<template>
  <el-form :model="form" ref="form_ref" label-position="left" label-width="auto">
    <el-steps :active="steps" align-center finish-status="success">
      <el-step title="账号信息"/>
      <el-step title="详细信息"/>
    </el-steps>

    <template v-if="steps==0">
      <el-form-item label="用户名" prop="username" :rules="[]" required>
        <el-input v-model="form.username"></el-input>
      </el-form-item>
      <el-form-item label="密码" prop="password" :rules="[]" required>
        <el-input v-model="form.password" type="password"></el-input>
      </el-form-item>
      <el-form-item label="确认密码" prop="password" required
                    :rules="[{validator: ()=>form.password && form.password===form.password_confirm, message: '两次密码必须一致'}]">
        <el-input v-model="form.password_confirm" type="password"></el-input>
      </el-form-item>
      <el-form-item label="邮箱" prop="email"
                    :rules="[{validator: ()=>/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(form.email), message: '邮箱不合法'}]">
        <el-input v-model="form.email"></el-input>
      </el-form-item>
      <el-form-item label="验证码" prop="token" :rules="[]">
        <el-input v-model="form.token" :disabled="!is_sended"></el-input>
        <el-button @click="send" style="float: right">发送验证码</el-button>
      </el-form-item>
    </template>
    <template v-if="steps==1">
      <el-row :gutter="20">
        <el-col :span="16">
          <el-form-item label="昵称" prop="nickname">
            <el-input v-model="form.nickname"></el-input>
          </el-form-item>
          <el-form-item label="性别" prop="gender">
            <el-select-v2 v-model="form.gender" :options="[{label: '未知', value: 0}, {label: '男', value: 1}, {label: '女', value: 2}]"></el-select-v2>
          </el-form-item>
          <el-form-item label="地区" prop="location">
            <el-select-v2 v-model="form.location" :options="locations"></el-select-v2>
          </el-form-item>
          <el-form-item label="生日" prop="birthday">
            <el-date-picker v-model="form.birthday"></el-date-picker>
          </el-form-item>
          <el-form-item label="手机号" prop="cellphone">
            <el-input v-model="form.cellphone"></el-input>
          </el-form-item>
          <el-form-item label="github" prop="github"
                        :rules="[{validator: ()=>/^https?:\/\/\S+$/.test(form.github), message: '链接不合法'}]">
            <el-input v-model="form.github"></el-input>
          </el-form-item>
          <el-form-item label="qq" prop="qq">
            <el-input v-model="form.qq"></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="8">
          <el-form-item prop="avatar">
            <el-upload v-model:file-list="form_data.avatar" drag ref="f" :auto-upload="false"
                       list-type="picture-card" accept="image/*"
                       :limit="1" :on-exceed="(files)=>{f.clearFiles();f.handleStart(files[0])}"
            >上传头像
              <template #file="f">
                <el-image :src="f.file.url" :preview-src-list="[f.file.url]" fit="contain"/>
<!--                <img :src="f.file.url">-->
<!--                <span class="el-upload-list__item-actions">-->
<!--                <span class="el-upload-list__item-preview" @click="preview=true">-->
<!--                  预览-->
<!--                  <el-dialog v-model="preview">-->
<!--                    <el-image-viewer :url-list="[f.file.url]"/>-->
<!--                  </el-dialog>-->
<!--                </span>-->
<!--                </span>-->
              </template>
            </el-upload>
          </el-form-item>
        </el-col>
      </el-row>

      <el-row justify="center">
        <el-button @click="register">注册</el-button>
        <el-button @click="login">登录</el-button>
        <el-button @click="post(`logout/`, form)">登出</el-button>
      </el-row>
    </template>

    <el-row justify="center" :gutter="200">
      <el-button @click="steps=Math.max(0,steps-1)" type="primary">上一步</el-button>
      <el-button @click="steps=Math.min(2,steps+1)" type="primary">下一步</el-button>
    </el-row>
<!--    {{form}}-->
  </el-form>
</template>

<style scoped>
.el-input{
  max-width: 240px;
}
</style>
