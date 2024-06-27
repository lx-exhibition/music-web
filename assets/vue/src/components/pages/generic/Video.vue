<script setup lang="ts">
import {useRouter,useRoute,useLink} from 'vue-router'
let route = useRoute(), router = useRouter()
import {get,post} from '@/components/utils/http'
import moment from 'moment'

import {watchEffect,ref} from 'vue'
import {Share24Filled} from "@vicons/fluent";
import {VideoPlayer} from "@videojs-player/vue";
let data = ref([]), data_comment = ref([])
watchEffect(async () => {
  const id = route.query.id
  get(`g-Video/?id=${id}`).then(res => data.value = res)
  get(`g-Comment/?type=video&id=${id}`).then(res => data_comment.value = res)
})
let c_row = 'flex flex-row', c_col = 'flex flex-col'
let c_hover = 'hover:text-blue-500 hover:cursor-pointer'

let comment = ref('')
let uid = localStorage.getItem('id'), aid = localStorage.getItem('aid')

</script>

<template>
  <div class="flex">
    <video-player :src="data.data" :poster="data.img" class="mx-auto" :width="600" controls/>
  </div>

  <p class="mt-10 text-2xl" id="comment">评论</p>
  <div class="border-2 my-3 border-sky-400"></div>
  <div :class="[c_row, 'h-24 *:ml-2']">
    <img :src="`http://localhost:8001/rest/img-user/?id=${uid}`" class="size-24 rounded-2xl">
    <textarea v-model="comment" placeholder="评论"
              class="grow rounded-xl resize-none p-2"/>
    <el-button class="basis-12 max-h-sm my-auto" type="primary"
               @click="post('VideoComment/', {
                 // user: uid,
                 user: 32+Math.ceil(Math.random()*20),
                 video: route.query.id, content: comment,
                 shared_count: Math.ceil(Math.random()*10000), liked_count: Math.ceil(Math.random()*10000)}
               ).then(()=>{
                 comment = ''
                 get(`g-Comment/?type=video&id=${route.query.id}`).then(res => data_comment = res)
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
          <span @click="v.liked_count++" :class="c_hover"><el-icon><ThumbLike16Filled/></el-icon>{{v.liked_count}}</span>
          <span @click="v.shared_count++" :class="c_hover"><el-icon><Share24Filled/></el-icon>{{v.shared_count}}</span>
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