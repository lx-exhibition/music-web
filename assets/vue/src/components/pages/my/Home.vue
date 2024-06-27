<script setup>
import {get} from '@/components/utils/http'
import {watchEffect, ref} from 'vue'
import {useRoute} from 'vue-router'

let route = useRoute()

let data = ref({origin_user: 'sd', location: ' '})


let close_handle = watchEffect(async () => {
  const url = route.query.id ? route.query.id : localStorage.getItem('id')
  get(`User/${url}/d/`).then(res => data.value = res)
})

</script>

<template>
  <el-descriptions :column="2">
    <el-descriptions-item :span="2"><img :src="data.avatar" style="width: 100px" class="rounded-3xl"/></el-descriptions-item>
    <el-descriptions-item><h1>{{ data.nickname }}</h1></el-descriptions-item>
    <el-descriptions-item label="性别">{{ data.gender }}</el-descriptions-item>
    <el-descriptions-item label="生日">{{ data.birthday }}</el-descriptions-item>
    <el-descriptions-item label="电话">{{ data.cellphone }}</el-descriptions-item>
    <el-descriptions-item label="qq">{{ data.qq }}</el-descriptions-item>
    <el-descriptions-item label="github">
      <el-link :href="data.github" target="_blank">{{ data.github }}</el-link>
    </el-descriptions-item>
    <el-descriptions-item label="经验值">{{ data.experience }}</el-descriptions-item>
    <el-descriptions-item label="邮箱">{{ data.origin_user.email }}</el-descriptions-item>
    <el-descriptions-item label="位置">{{ data.location.location }}</el-descriptions-item>
  </el-descriptions>
</template>

<style scoped>


</style>