<template>
  <el-tabs v-model="table.model_type" @tabChange="on_tab_change">
    <el-tab-pane v-for="(v) in table.model_types" :label="v" :name="v"/>
    <el-table :data="table.data" max-height="480" stripe border size="small">
      <el-table-column v-for="(v) in table.cols" :label="v" :prop="v" sortable/>

      <el-table-column type="selection" fixed="left"/>
      <el-table-column type="index" fixed="left" title="序号"/>
      <el-table-column type="expand" fixed="left">
        <template #default="v">
          <el-descriptions direction="horizontal" border>
            <el-descriptions-item v-for="(w) in table.cols" :label="w">{{v.row[w]}}</el-descriptions-item>
          </el-descriptions>
        </template>
      </el-table-column>
      <el-table-column fixed="right">
        <template #header>
          <el-button type="text" style="width: 100%;border-radius: 30px"
                     @click="()=>{dialog_add.open=true}">add</el-button>
        </template>
        <template #default="v">
          <el-row justify="center">
            <el-button type="primary" style="width: 100%;border-radius: 30px"
                       @click="()=>{dialog_edit.open = true; dialog_edit.data = v.row}">edit</el-button>
            <br/>
            <el-popconfirm title="确定要删除吗？" @confirm="()=>{delete_(`auth_User/${v.row.id}/`).then((res)=>{
                       table.data.splice(v.$index,1)
            })}" >
              <template #reference><el-button type="danger" style="width: 100%;border-radius: 30px">remove</el-button></template>
            </el-popconfirm>
          </el-row>
        </template>
      </el-table-column>
    </el-table>
  </el-tabs>
  {{table.model_types}}

  <el-dialog v-model="dialog_add.open">
    <lx-model-form v-model="dialog_add"/>
  </el-dialog>
  <el-dialog v-model="dialog_edit.open">
    <lx-model-form v-model="dialog_edit"/>
  </el-dialog>
</template>

<script setup lang="ts">
import {delete_, get} from '@/components/utils/http'
import {ref,reactive,onBeforeMount} from 'vue'
import {ElTable} from "element-plus";
import LxModelForm from "@/components/utils/lx-model-form.vue";
let table = reactive({model_types: [], model_type: null, cols: [], data: []})
let dialog_add = ref({data: {}, conf: {}, model_type: '', method: 'post', open: false})
let dialog_edit = ref({data: {}, conf: {}, model_type: '', method: 'put', open: false})


let on_tab_change = async ()=>{
  // table.model_type 首次赋值时，取 table.model_types[0]
  table.model_type = table.model_type ? table.model_type : table.model_types[0]
  await get(`${table.model_type}/cols/`).then(res => table.cols = res )
  await get(`${table.model_type}/`).then(res => {
    table.data = res.data

    dialog_add.value.conf = res.conf
    dialog_edit.value.conf = res.conf
  })

  dialog_add.value.model_type = table.model_type
  dialog_edit.value.model_type = table.model_type
}
onBeforeMount(async ()=>{
  await get('model-types/').then((res)=> table.model_types = res)
  on_tab_change()
})
</script>

<style scoped>

</style>