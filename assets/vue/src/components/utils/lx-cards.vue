<script setup>
import {ReadMoreRound} from "@vicons/material";
import {DotCircleRegular} from "@vicons/fa";

import {defineProps,useSlots} from 'vue'
import {IceDrink} from "@element-plus/icons-vue";
let props = defineProps(['title','path','size','tags','data'])
let size,title,path,tags,data,aside
title = props.title ? props.title : 'example_title'
path = props.path ? props.path : '#/example/path'
size = props.size ? props.size : [30,30]   // 卡片的 右间距, 下间距
tags = props.tags ? props.tags : []        // 标题右侧的标签, 如：tags = [{label: 'example label', id: 'tag-name'}]
data = props.data ? props.data : [{title: 'example title', img: 'image-url', id: 'data-id'}]
aside = !!useSlots().aside
// try { title = props.title }catch (e){ title = 'example_title';console.log(1) }
// try { path = props.path }catch (e){ path = '#/example/path';console.log(2) }
// try { size = props.size }catch (e){ size = [50,40];console.log(3) }
// try { tags = props.tags }catch (e){ tags = [] ;console.log(4) }
// try { data = props.data }catch (e){ data = [{title: 'example title', img: 'image-url', id: 'data-id'}];console.log(5) } // 数据项

</script>

<template>
  <el-card shadow="hover">
    <template #header>
      <!--      DotCircleRegular-->
      <el-row align="middle">
        <el-col :span="1">
          <el-icon><DotCircleRegular/></el-icon>
        </el-col>
        <el-col :span="6">
          <el-link :href="path" :underline="false"><h1>{{title}}</h1></el-link>
        </el-col>
        <el-col :span="17">
          <el-space spacer="|" alignment="center">
            <el-link v-for="(v,k,i) in tags" :href="`${path}?tag=${v.id}`"
            >{{v.label}}</el-link>
          </el-space>
        </el-col>
      </el-row>
    </template>
    <el-row>
      <el-col :span="aside ? 20 : 24">
        <el-space :size="size" wrap>
          <el-card v-for="(v,k,i) in data" shadow="hover"
                   style="width: 200px; height: 200px">
            <el-row justify="center">
              <el-link :href="`${path}?search=${v.id}`">
                <img :src="v.img"
                     style="width: 140px; height: 140px; object-fit: cover">
              </el-link>
            </el-row>
            <el-row justify="center">
              <el-link :underline="false" style="text-align: center" :href="`${path}?search=${v.id}`">{{v.title}}</el-link>
            </el-row>
          </el-card>
        </el-space>
      </el-col>
      <el-col :span="aside ? 4 : 0">
<!--        <el-affix offset="60">-->
          <slot name="aside"/>
<!--        </el-affix>-->
      </el-col>
    </el-row>

    <template #footer>
      <el-row justify="end">
        <el-link :underline="false" :href="path">更多<template #icon><el-icon><ReadMoreRound/></el-icon></template></el-link>
      </el-row>
    </template>
  </el-card>
</template>

<style scoped>

</style>