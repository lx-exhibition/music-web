<script setup lang="ts">
// ==== 数据库表详情修改表单
// 依赖组件 => lx-form
// 依赖接口 ：
// GET model-types/ => 获取所有 model 类型的名字
// GET <model-name>/ids/ => 获取 model 对应的所有主键
// GET <model-name>/<id>/ => 获取指定 id 的 model


import GForm from "@/components/utils/lx-model-form.vue";

import {ref,onBeforeMount} from 'vue'
import {get} from '@/components/utils/http'
let gform = ref({model: {}, id: null, ids: [], model_types: []})

let on_change = async (update_id=true)=>{
  gform.value.model.method = 'put'
  gform.value.model.model_type = gform.value.model.model_type ? gform.value.model.model_type : gform.value.model_types[0]
  await get(`${gform.value.model.model_type}/ids/`).then(res => gform.value.ids = res)
  try {
    gform.value.id = update_id || !gform.value.id ? gform.value.ids[0].label : gform.value.id
  }catch (e){gform.value.model.data = {}}
  await get(`${gform.value.model.model_type}/${gform.value.id}/`).then(res => {
    gform.value.model = Object.assign({}, gform.value.model, res)
  })
  console.log(gform.value.model)
}
onBeforeMount(async ()=>{
  await get('model-types/').then(res => gform.value.model_types = res)
  await on_change()
})

</script>


<template>
  <el-tabs v-model="gform.model.model_type" @tab-change="on_change()">
    <el-tab-pane v-for="(v,i) in gform.model_types" :label="v" :name="v"/>
    <el-select-v2 v-model="gform.id" :options="gform.ids" @change="on_change(false)"/>
    <g-form v-model="gform.model"></g-form>
  </el-tabs>
</template>


<style scoped>

</style>