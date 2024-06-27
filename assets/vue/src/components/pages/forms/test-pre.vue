<script setup lang="ts">
import {post} from '@/components/utils/http'

import moment from 'moment'
// let t = ()=>{
//   post('user2/', {data: JSON.stringify({
//       origin_user_id: 51,
//       location_id: 0,
//       avatar_id: 0,
//       fans: [4],
//       msg_users: [3],
//
//       gender: 0,
//       birthday: moment().format('YYYY-MM-DD'),
//       nickname: '各级',
//       cellphone: '',
//       qq: '',
//       github: '',
//       experience: 123,
//     })})
// }

import {ref} from 'vue'
import {FormInstance} from 'element-plus'
let form_data = ref({str: '', int: 10, arr: [], file: []}), file = ref([])
let form_ref = ref<FormInstance>()

let dep = 2+Math.random()*2
let dfs = (root, layer)=>{
  if (layer>dep) return
  let len = 3+Math.random()*2
  root.children = []
  for (let i = 0; i < len; i++) {
    let child = {
      label: `${root.label ? `${root.label}-` : ''}${i+1}`,
      value: `${root.value ? `${root.value}-` : ''}${i+1}`,
      children: [], disabled: Math.random()>0.7 }
    root.children.push(child)
    dfs(child,layer+1)
  }
}
let options = {children: []}
dfs(options, 0)
options = options.children
// console.log(options)

let props = { multiple: true, checkStrictly: false }

import {ElMessage} from 'element-plus'
import {Plus} from "@element-plus/icons-vue";
let on_submit = (isValid, invalidFields)=>{
  if (isValid){
    ElMessage.success('数据验证成功')
    post(`test/?time=${new Date()}`, form_data.value)
    console.log(URL.createObjectURL(form_data.value.file[0].raw))
  }else {
    ElMessage.error('数据验证失败')
  }
}

import {UploadInstance} from 'element-plus'

let upload_ref = ref<UploadInstance>()
let dialog = ref(false), dialog_url = ref('')
</script>

<template>
  <el-form :model="form_data" ref="form_ref">
    <el-form-item label="str" prop="str">
      <el-input v-model="form_data.str"></el-input>
    </el-form-item>
    <el-form-item label="int" prop="int">
      <el-slider v-model="form_data.int"></el-slider>
    </el-form-item>
    <el-form-item label="arr" prop="arr">
      <el-cascader v-model="form_data.arr" :options="options" :props="props"
                   clearable filterable :show-all-levels="false">
      </el-cascader>
    </el-form-item>
    <el-form-item label="file" prop="file">
      <el-upload v-model:file-list="form_data.file" :auto-upload="false" list-type="picture-card" drag
                 :on-preview="(uploadFile)=>{dialog=true;dialog_url = uploadFile.url; console.log(dialog_url)}"
                 accept="image/*" multiple :http-request="(options)=>{console.log(23,options); return }"
                 ref="upload_ref"
      >
        <template #trigger><el-button>选择文件</el-button></template>
        <el-button type="success" @click="upload_ref.submit()">上传文件</el-button>
      </el-upload>
    </el-form-item>


    <el-form-item>
      <el-button @click="form_ref.validate(on_submit)">提交</el-button>
      <el-button @click="form_ref.resetFields()">重置</el-button>
    </el-form-item>
  </el-form>
  {{form_data}}

  <el-dialog v-model="dialog">
    <el-image :src="dialog_url" alt="dialog"></el-image>
  </el-dialog>
</template>

<style scoped>

</style>