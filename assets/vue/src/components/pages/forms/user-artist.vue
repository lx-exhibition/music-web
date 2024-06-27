<script setup lang="ts">
import {ref} from "vue";
import {get} from "@/components/utils/http";

let form = ref({})

let is_sended = ref(false)
</script>

<template>
  <el-form class="flex flex-col" inline>
    <el-form-item label="艺名"><el-input v-model="form.stagename"></el-input></el-form-item>
    <el-form-item label="描述"><el-input v-model="form.description"></el-input></el-form-item>
    <el-form-item><el-upload v-model:file-list="form.bg" :auto-upload="false" list-type="picture-card">上传背景图</el-upload></el-form-item>
    <el-button>入驻歌手</el-button>
  </el-form>

</template>

<style scoped>

</style>