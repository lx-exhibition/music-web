<script setup lang="ts">
// ==== 模型表单
// model（ref）应提供三个参数 =>
// @data: {id: .., other: ..., ... }, 表单数据
// @conf: dict, 各字段的 tag 配置
// @model_type: str, 模型类名
// @method: 'post' | 'put', 是发送 post，还是发送 put


import {defineModel,onBeforeUpdate} from 'vue'
import {put, post, check} from '@/components/utils/http'
let m = defineModel()
onBeforeUpdate(()=>{
  check(m.value.data, 'model.data')
  check(m.value.conf, 'model.conf')
  check(m.value.model_type, 'model.model_type')
  check(m.value.method, 'model.method')
})

let on_send = ()=>{
  let url = `${m.value.model_type}/${m.value.data.id}/`
  console.log(url)
  if (m.value.method === 'post'){ post(`${m.value.model_type}/`, m.value.data) }
  if (m.value.method === 'put'){ put(`${m.value.model_type}/${m.value.data.id}/`, m.value.data) }
}

console.log(m.value.data)
m.value.data_b = Object.assign({},m.value.data)
console.log(m.value.data_b)
</script>

<template>

  <el-form inline>
    <el-form-item v-for="(v,k,i) in m.conf" v-show="k !== 'id'"
                  :label="k">
<!--      <component :is="`el-${m.conf[k].tag}`" v-model="m.data[k]" :options="m.conf[k].attrs.opts"/>-->
      <component :is="`el-${v.tag}`" v-model="m.data[k]"
                 :multiple="v.attrs.multiple" :options="v.attrs.opts"
                 :type="v.attrs.type" :format="v.attrs.format"
                 style="min-width: 200px"/>
    </el-form-item>
    <el-row justify="center">
      <el-button @click="on_send">提交</el-button>
      <el-button @click="m.data = m.data_b">重置</el-button>
    </el-row>
  </el-form>
{{m.data}}
</template>

<style scoped>

</style>