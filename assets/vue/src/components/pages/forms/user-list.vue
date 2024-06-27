
<template>

  <el-table :data="table.data" max-height="500" stripe border highlight-current-row
            @current-change="(cur)=>{console.log(cur)}"
            ref="table_ref"
  >
    <el-table-column type="expand" fixed>
      <template #default="v">
        <el-descriptions :title="v.row.username" :column="2" direction="horizontal" border>
          <!--          <el-descriptions-item label="用户名">{{ v.row.username }}</el-descriptions-item>-->
          <el-descriptions-item label="密码" :span="2">{{ v.row.password }}</el-descriptions-item>
          <el-descriptions-item label="邮箱">{{ v.row.email }}</el-descriptions-item>
          <el-descriptions-item label="first name">{{ v.row.first_name }}</el-descriptions-item>
          <el-descriptions-item label="last name">{{ v.row.last_name }}</el-descriptions-item>
          <el-descriptions-item label="注册时间">{{ moment(v.row.date_joined).format('YYYY-MM-DD HH:mm:ss') }}</el-descriptions-item>
          <el-descriptions-item label="上次登录时间">{{ moment(v.row.last_login).format('YYYY-MM-DD HH:mm:ss') }}</el-descriptions-item>
          <el-descriptions-item label="超级用户">{{ v.row.is_superuser }}</el-descriptions-item>
          <el-descriptions-item label="管理员">{{ v.row.is_staff }}</el-descriptions-item>
          <el-descriptions-item label="活跃">{{ v.row.is_active }}</el-descriptions-item>
        </el-descriptions>
      </template>
    </el-table-column>
    <el-table-column type="selection" fixed/>
    <el-table-column type="index" fixed sortable/>

    <el-table-column prop="pk" label="id" width="60" sortable/>
    <!--    <el-table-column prop="model" label="model" sortable/>-->

    <!--    <el-table-column label="基本信息">-->
    <el-table-column prop="username" label="用户名" sortable/>
    <el-table-column prop="password" label="密码" sortable>
      <template #default="v">{{v.row.password.substr(0,4)}}...</template>
    </el-table-column>
    <el-table-column prop="email" label="邮箱" sortable/>
    <!--      <el-table-column prop="first_name" label="first_name" sortable/>-->
    <!--      <el-table-column prop="last_name" label="last_name" sortable/>-->
    <!--    </el-table-column>-->

    <!--    <el-table-column label="bool相关">-->
    <el-table-column prop="is_superuser" label="超级用户" sortable
                     :filters="bool_filters" :filter-method="filter_method"
    />
    <el-table-column prop="is_staff" label="管理员" sortable
                     :filters="bool_filters" :filter-method="filter_method"
    />
    <el-table-column prop="is_active" label="活跃状态" sortable
                     :filters="bool_filters" :filter-method="filter_method"
    />
    <!--    </el-table-column>-->

    <!--    <el-table-column label="时间相关">-->
    <el-table-column prop="date_joined" label="注册时间" sortable>
      <template #default="v">{{moment(v.row.date_joined).format('YYYY-MM-DD')}}</template>
    </el-table-column>
    <el-table-column prop="last_login" label="上次登录" sortable>
      <template #default="v">{{moment(v.row.date_joined).format('YYYY-MM-DD')}}</template>
    </el-table-column>


    <el-table-column fixed="right">
      <template #header>
        <el-button type="text" style="width: 100%;border-radius: 30px"
                   @click="()=>{popover.open = true}">add</el-button>
      </template>
      <template #default="v">
        <el-row justify="center">
          <el-button type="primary" style="width: 100%;border-radius: 30px"
                     @click="()=>{dialog.open = true; dialog.data = v.row}">edit</el-button>
          <br/>
          <el-popconfirm title="确定要删除吗？" @confirm="()=>{delete_(`auth_User/${v.row.id}/`).then((res)=>{
                       table.data_base.splice((pagination.cur-1)*pagination.size + v.$index,1)});console.log(123)
                     }" >
            <template #reference><el-button type="danger" style="width: 100%;border-radius: 30px">remove</el-button></template>
          </el-popconfirm>
        </el-row>
      </template>
    </el-table-column>

  </el-table>

  <el-row justify="center">
    <el-pagination :total="pagination.total" v-model:page-size="pagination.size" v-model:current-page="pagination.cur"
                   layout="prev, pager, next, jumper, slot, sizes, total"
                   :page-sizes="[5,10,20,50,100,200,500]" :pager-count="11"
                   @size-change="(size)=>console.log(size)"
                   @current-change="(cur)=>console.log(cur)"
    >
      <template #default>
        <!--        {{pagination.size}}, {{pagination.cur}}-->
      </template>
    </el-pagination>
  </el-row>

  <el-dialog v-model="dialog.open">
    <!--    {{dialog.data}}-->
    <el-form inline>
      <el-form-item label="用户名"><el-input v-model="dialog.data.username"></el-input></el-form-item>
      <el-form-item label="密码"><el-input v-model="dialog.data.password"></el-input></el-form-item>
      <el-form-item label="邮箱"><el-input v-model="dialog.data.email"></el-input></el-form-item>
      <el-form-item label="first name"><el-input v-model="dialog.data.first_name"></el-input></el-form-item>
      <el-form-item label="last name"><el-input v-model="dialog.data.last_name"></el-input></el-form-item>
      <el-form-item label="注册时间"><el-date-picker type="datetime" v-model="dialog.data.date_joined"></el-date-picker></el-form-item>
      <el-form-item label="上次登录时间"><el-date-picker type="datetime" v-model="dialog.data.last_login"></el-date-picker></el-form-item>
      <el-form-item label="超级用户"><el-switch v-model="dialog.data.is_superuser"></el-switch></el-form-item>
      <el-form-item label="管理员"><el-switch v-model="dialog.data.is_staff"></el-switch></el-form-item>
      <el-form-item label="活跃"><el-switch v-model="dialog.data.is_active"></el-switch></el-form-item>

      <el-row justify="center">
        <el-button @click="()=>{put(`auth_User/${dialog.data.id}/`, dialog.data)}">save</el-button>
        <el-button @click="dialog.open=false">cancel</el-button>
      </el-row>
    </el-form>

  </el-dialog>

</template>

<script setup lang="ts">
import {ref,onMounted,reactive,computed} from 'vue'

import {get,put,post,delete_} from '@/components/utils/http'
import {ElTable} from 'element-plus'
import InstanceType from 'element-plus'
import moment from 'moment'

let table = reactive({data: [], data_base: []}), table_ref = ref<InstanceType<typeof ElTable>>()
let pagination = reactive({total: 0, size: 5, cur: 1})
let dialog = reactive({open: false, data: {}}), popover = reactive({open: false, data: {}})
onMounted(async ()=>{

  await get(`auth_User/?time=${new Date()}`).then((res)=>{
    table.data_base = res.data
    console.log(res)
    pagination.total = computed((old)=>{
      return table.data_base.length
    })
    table.data = computed((old)=>{
      return table.data_base.slice((pagination.cur-1)*pagination.size, pagination.cur*pagination.size)
    })
  })

  // console.log(moment().format('x'))
  // post('auth_User/', {username: `${moment().format('x')}`, password: '90'})
})

let bool_filters: {text: string, value: boolean}[] = [{text: 'Y', value: true}, {text: 'N', value: false}]
let filter_method = (value, row, column)=>{
  // return row.fields[prop_name] === value
  return eval(`row.${column.property}`) === value
}


</script>

<style scoped>

</style>\