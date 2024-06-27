<template>
  <el-form ref="form_ref" :model="form_data" style="max-width: 500px">
    <el-form-item label="用户名" prop="username" :rules="[
        { required: true, message: '用户名是必须的' },
        { min: 4, message: '用户名必须至少为 4 个字符' },
        ]">
      <el-input v-model="form_data.username"></el-input>
    </el-form-item>
    <el-form-item label="密码" prop="password" :rules="[
        { required: true, message: '密码是必须的' },
        { min: 4, max: 13, message: '密码必须为 4 ~ 13 个字符之间' },
        ]">
      <el-input v-model="form_data.password" type="password"></el-input>
    </el-form-item>
    <el-form-item label="密码" prop="password_confirm" :rules="[
        { validator: vl_password_confirm },
        ]" required>
      <el-input v-model="form_data.password_confirm" type="password"></el-input>
    </el-form-item>
    <el-form-item label="邮箱" prop="email" :rules="[
        { validator: vl_email },
        ]">
      <el-input v-model="form_data.email"></el-input>
    </el-form-item>
    <br/>
    <el-button @click="ob_submit(form_ref)">提交</el-button>
    <el-button @click="form_ref.resetFields()">清空</el-button>
  </el-form>
  {{form_data}}
</template>

<script setup>
import {ref} from "vue";
let form_ref = ref(), form_data = ref({})
let vl_password_confirm = (rule, value, cb)=>{
  if (value===''){
    cb(new Error('请再次确认密码'))
  }else if (value!==form_data.value.password){
    cb(new Error('两次密码必须相同！'))
  }
}
let vl_email = async (rule, value, cb)=>{

}
let ob_submit = async (form_ref)=>{
  await form_ref.validate((a,b)=>a?console.log('123'):console.log(b))
}

</script>

<style scoped>

</style>