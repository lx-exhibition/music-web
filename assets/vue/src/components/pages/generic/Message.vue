<script setup>
import {useRouter,useRoute,useLink} from 'vue-router'
let route = useRoute(), router = useRouter()
import {get,post} from '@/components/utils/http'
import moment from 'moment'

import {watchEffect,ref} from 'vue'
let data = ref([])
const id1 = route.query.id1 ? route.query.id1 : localStorage.getItem('id')
const id2 = route.query.id2
let close_handle = watchEffect(async () => {
  get(`g-Message/?id1=${id1}&id2=${id2}`).then(res => data.value = res)
})

let c_row = 'flex flex-row', c_col = 'flex flex-col'

let message = ref('')
</script>

<template>
<!--  {{id1}},{{id2}},-->
  <div v-for="(v) in data" class="mt-2">
    <div v-if="v.send_user.id == id1">
      <span :class="[c_row, 'justify-center', 'text-[10px] text-gray-50']">
        {{moment(v.send_time).format('YYYY-MM-DD hh:mm:ss')}}
      </span>
      <span :class="[c_row, '*:rounded-2xl justify-end *:mx-1 ']">
        <p class="bg-cyan-500 my-auto h-12 content-center px-2">{{v.content}}</p>
        <img :src="v.send_user.avatar" class="size-16 "/>
      </span>
    </div>
    <div v-else>
      <span :class="[c_row, 'justify-center', 'text-[10px] text-gray-50']">
        {{moment(v.send_time).format('YYYY-MM-DD hh:mm:ss')}}
      </span>
      <span :class="[c_row, '*:rounded-2xl *:mx-1 ']">
        <img :src="v.send_user.avatar" class="size-16 "/>
        <p class="bg-cyan-500 my-auto h-12 content-center px-2">{{v.content}}</p>
      </span>
    </div>
  </div>
  <div :class="[c_row, 'h-24 *:ml-2 ']">
    <img :src="`http://localhost:8001/rest/img-user/?id=${id1}`" class="size-24 rounded-2xl">
    <textarea v-model="message" placeholder="聊天"
              class="grow rounded-xl resize-none p-2"/>
    <el-button class="basis-12 max-h-sm my-auto" type="primary"
               @click="post('Message/', {
                 send_user: id1, receive_user: id2,
                 content: message
               }).then(()=>{
                 message = ''
                 get(`g-Message/?id1=${id1}&id2=${id2}`).then(res => data = res)
               })"
    >发送</el-button>
  </div>
</template>

<style scoped>

</style>