<script setup lang="ts">
import {Play48Filled,Collections20Filled,Share24Filled,ArrowDownload16Filled,Comment12Filled} from '@vicons/fluent'

import {useRouter,useRoute,useLink} from 'vue-router'
let route = useRoute(), router = useRouter()
import {get,post} from '@/components/utils/http'
import moment from 'moment'

import {watchEffect,ref} from 'vue'
let data = ref([]), data_comment = ref([])
let close_handle = watchEffect(async () => {
  const id = route.query.id
  get(`g-Song/?id=${id}`).then(res => data.value = res)
  get(`g-Comment/?type=song&id=${id}`).then(res => data_comment.value = res)
})

let c_row = 'flex flex-row', c_col = 'flex flex-col'
let c_bg = 'bg-gradient-to-tl from-black via-blue-200 to-black'
let c_center = 'max-w-sm mx-auto max-h-sm my-auto'
let c_hover = 'hover:text-blue-500 hover:cursor-pointer'

let more = ref(false), comment = ref('')
let uid = localStorage.getItem('id'), aid = localStorage.getItem('aid')

import {ElMessage} from 'element-plus'
import {useTest} from '@/components/stores'
let player = useTest()
let on_play = ()=>{
  ElMessage.success('正在播放...')
  player.load_play(data.value)
}
let on_collect = ()=>{
  ElMessage.success('已收藏...')
}
let on_share = ()=>{
  ElMessage.success('已复制到粘贴板')
  navigator.clipboard.writeText(window.location.href)
}
</script>

<template>
  <div :class="[c_row]">
    <div :class="['size-48 flex rounded-full', c_bg]">
      <el-image :src="data.img" :class="['size-36 rounded-full hover:animate-slow-spin', c_center]"/>
    </div>
    <div :class="[c_col, 'ml-5 *:mt-2 basis-3/6']">
      <p class="text-3xl">{{data.title}}</p>
      <p><span class="text-[12px]">歌手:</span>
        <span class="hover:text-blue-500 hover:cursor-pointer" v-if="data.artist"
                        @click="router.push(`/g/Artist?id=${data.artist.id}`)">{{data.artist.stagename}}</span>
      </p>
      <p><span class="text-[12px]">所属专辑:</span>
        <span class="hover:text-blue-500 hover:cursor-pointer" v-if="data.album"
                         @click="router.push(`/g/Album?id=${data.album.id}`)">{{data.album.title}}</span>
      </p>
      <div class="*:ml-2">
        <el-button type="primary" size="small" :icon="Play48Filled" @click="on_play">播放</el-button>
        <el-button type="primary" size="small" :icon="Collections20Filled" @click="on_collect">收藏</el-button>
        <el-button type="primary" size="small" :icon="Share24Filled" @click="on_share">分享</el-button>
        <a :href="`${data.data}`" target="_blank"><el-button type="primary" size="small" :icon="ArrowDownload16Filled">下载</el-button></a>
        <a href="#comment" class="ml-2"><el-button type="primary" size="small" :icon="Comment12Filled">评论</el-button></a>

      </div>
      <el-text v-html="data.lyrics" :line-clamp="more ? 1000 : 8"/>
    </div>
    <el-button type="primary" @click="more=!more" class="hover:cursor-pointer self-start mt-36">{{more?'折叠':'展开'}}</el-button>

  </div>

  <p class="mt-10 text-2xl" id="comment">评论</p>
  <div class="border-2 my-3 border-sky-400"></div>
  <div :class="[c_row, 'h-24 *:ml-2']">
    <img :src="`http://localhost:8001/rest/img-user/?id=${uid}`" class="size-24 rounded-2xl">
    <textarea v-model="comment" placeholder="评论"
              class="grow rounded-xl resize-none p-2"/>
    <el-button class="basis-12 max-h-sm my-auto" type="primary"
               @click="post('SongComment/', {
                 // user: uid,
                 user: 32+Math.ceil(Math.random()*20),
                 song: route.query.id, content: comment,
                 shared_count: Math.ceil(Math.random()*10000), liked_count: Math.ceil(Math.random()*10000)}
               ).then(()=>{
                 comment = ''
                 get(`g-Comment/?type=song&id=${route.query.id}`).then(res => data_comment = res)
               })"
    >评论</el-button>
  </div>
  <div v-if="data_comment.length" v-for="(v) in data_comment" :class="[c_row, 'm-2']">
    <img :src="v.img" class="size-20 rounded-2xl">
    <div class="m-2 grow">
      <el-text :line-clamp="2">{{v.user.nickname}}: {{v.content}}</el-text>
      <div :class="[c_row, 'place-content-between']">
        <p class="text-[10px]">{{moment(v.pub_time).format('YYYY年MM月DD日')}}</p>
        <div :class="[c_row, '*:mx-2']">
          <span @click="v.liked_count++" :class="c_hover">
            <el-icon><ThumbLike16Filled/></el-icon>
            {{v.liked_count}}
          </span>
          <span @click="v.shared_count++" :class="c_hover">
            <el-icon><Share24Filled/></el-icon>
            {{v.shared_count}}
          </span>
        </div>
      </div>
    </div>
  </div>
  <div v-else>
    评论区空空如也...
  </div>

</template>

<style scoped>

</style>