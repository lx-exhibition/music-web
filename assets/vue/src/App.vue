<template>
  <div id="root" class="h-full">
<!--    <vue-particles id="tsparticles" @particles-loaded="async (container) => {-->
<!--      console.log('Particles container loaded', container);-->
<!--      }" url="http://foo.bar/particles.json" />-->

<!--    粒子特效-->
    <vue-particles id="tsparticles" :options="conf_effect" @particles-loaded="async (container) => {console.log(container)}"/>

    <el-container :class="theme.c_theme">
      <el-header class="px-0">
        <div id="header">
        <Header/>
        </div>
      </el-header>
      <el-main style="padding: 0">
        <el-container>
          <el-aside style="height: 100%" width="collapse">
            <div id="aside">
            <Aside/>
            </div>
          </el-aside>
          <el-container style="height: 100%">
            <el-header height="20px">
              <el-page-header title="返回" @back="on_back">
                <template #content>
                  <el-breadcrumb separator="/">
                    <el-breadcrumb-item :to="{path: '/'}">index</el-breadcrumb-item>
                    <el-breadcrumb-item v-for="(v) in sections" :to="{path: `/${v}`}">{{v}}</el-breadcrumb-item>
                  </el-breadcrumb>
                </template>
              </el-page-header>
            </el-header>
            <el-main>
              <el-scrollbar height="500px">
                <div id="main">
                <router-view/>
                </div>
              </el-scrollbar>
            </el-main>
          </el-container>
        </el-container>
      </el-main>
      <el-footer class="px-0">
        <div id="footer" class="h-full">
        <Footer/>
        </div>
      </el-footer>
    </el-container>
  </div>
</template>

<script setup lang="ts">
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
import Aside from './components/Aside.vue'
import {conf_effect} from './components/utils/confs.js'

import {useRoute,useRouter} from 'vue-router'
import {inject,ref,onMounted} from 'vue'
let route = useRoute(), router = useRouter(), conf = inject('conf')

const header = ref(), main = ref(), footer = ref()
const footer_class = ref({})

onMounted(()=>{
  // header.value.x = 1
  // header.value.style.height = `${80}px`
  // main.value.style.marginTop = `${85}px`
  // footer.value.style.height = `${50}px`
  // footer.value.style.height = `${50}px`
  // footer.value.style.marginTop = `${window.innerHeight-60}px`
  // footer.value.style.marginTop = `${window.innerHeight-60}px`
  // footer_class.tasks = []

})
window.addEventListener('resize', () => {
  // let t = footer.value.style.height
  // let num = t.substring(0,t.length-2)
  // main.value.style.marginTop = `${85}px`
  // footer.value.style.marginTop = `${window.innerHeight-60}px`
  // footer.value.style.width = `${window.innerWidth}px`

})


let into_footer = ()=>{
  return
  for (let x of footer_class.tasks) {
    x && clearTimeout(x)
  }
  console.log("开播")
  footer_class.value['animate__heartBeat'] = true
  footer_class.value['animate__bounce'] = true
  footer_class.value['animate__animated'] = true
  footer_class.value['animate__infinite'] = true
}
let out_footer = ()=>{
  footer_class.value['animate__infinite'] = false
  footer_class.tasks.push(
      footer.value.addEventListener("webkitAnimationEnd", ()=>{
        delete footer_class.value['animate__heartBeat']
        delete footer_class.value['animate__bounce']
        delete footer_class.value['animate__animated']
        // footer_class.value = {}
        console.log('停播')
      })
  )
}

import {watchEffect} from 'vue'
let sections = ref([])
watchEffect(()=>{
  sections.value = route.path.split('/').filter(v => v!=='')
})
let on_back = () => history.back()


import {useTheme} from '@/components/stores.js'
let theme = useTheme()
</script>

<style scoped>
#root{
  font-family: 'Tangerine', serif;
  /* background-image: linear-gradient(#0158c9, #f8f7fc);  渐变色 */
  /* background-image: linear-gradient(#F00E30, #d4118f, #0c4cf3, #0ae993); */
  /* background-image: url("https://sex.nyan.xyz/api/v2/img?r18=true&author_uuid=66371932&author_uuid=70395770&author_uuid=17516104&author_uuid=14496985&author_uuid=13835102&author_uuid=1642433&author_uuid=23040640"); */
  /* background-position-x: right; */
  /* background-position-y: bottom; */

  background-position: center;
  background-size: auto 100%;
  background-repeat: no-repeat;
  background-attachment: fixed;
  //background-color: #A1DDC6;
  //background-color: white;
}
#header,#aside,#main,#footer{
  /* box-shadow: var(--el-box-shadow-dark); */
  //border-radius: var(--el-border-radius-circle);
  //background-color: #c9cad1;

  /* opacity: 0.8; */
}
#header{
  /* height: 80px; */
  /* border-radius: var(--el-border-radius-round); */
}
#aside{
   /*height: 630px;*/
  /* background-color: #2a2a2a; */
  /* color: white; */
}
#main{
  /* border-radius: var(--el-border-radius-base); */
  /* z-index: 2; */

}
#footer{
  //background-color: #2a2a2a;
  color: white;
}
</style>
