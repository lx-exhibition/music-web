<template>
<!--  <iframe width=900 height=100 src="https://music.163.com/outchain/player?type=0&id=2967278822&auto=1&height=430"></iframe>-->

  <el-row direction="horizontal" justify="center" align="middle" class="lx">
    <el-space wrap>
      <div>
        <el-button round color="#2a2a2a" size="large" :icon="PlaySkipBackOutline" @click="back_btn_clk"></el-button>
        <el-button round color="#2a2a2a" size="large" v-if="!player_test.audio.paused" :icon="VideoPause" @click="pause_btn_clk"></el-button>
        <el-button round color="#2a2a2a" size="large" v-else :icon="VideoPlay" @click="play_btn_clk"></el-button>
        <el-button round color="#2a2a2a" size="large"  :icon="PlaySkipForwardOutline" @click="forward_btn_clk"></el-button>
      </div>
      <img src="http://localhost:8001/media/uploads/image/MTA5OTUxMTY5MDE0NTcxNjk0.jpg" class="size-8" alt="歌曲封面">
      <el-col>
        <el-row>
          <el-col :span="19">
            <el-link style="font-size: 12px; color: white" :underline="false">とげとげサディスティック (5人 Ver.)</el-link>
          </el-col>
          <el-col :span="5">
            <el-link style="font-size: 10px; color: #aaaaaa" :underline="false">エノルミータ</el-link>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="24">
            <!--          <n-progress type="line" :percentage="percent" indicator-placement="outside" :stroke-width="20" ref="progress" />-->
            <el-progress :percentage="player_test.percentage" :format="()=>(`${player_test.time}/${player_test.total}`)"></el-progress>
          </el-col>
        </el-row>
      </el-col>
      <el-space :size="30">
        <el-space direction="horizontal">
          <el-tooltip content="歌词"><lx-img :images="[DocumentQueueMultiple24Regular,DocumentQueueMultiple24Filled]"
                                             @click="on_lyrics"/></el-tooltip>
          <el-tooltip content="收藏"><lx-img :images="[Collections20Regular,Collections20Filled]"
                                             @click="on_collect"/></el-tooltip>
          <el-tooltip content="分享"><lx-img :images="[Share16Regular,Share16Filled]"
                                             @click="on_share"/></el-tooltip>
        </el-space>
        <el-space direction="horizontal">
          <el-tooltip content="音量">
<!--            <el-link style="color: white" :underline="false" :icon="MdVolumeHigh" :index="0"></el-link>-->
            <el-dropdown :hide-timeout="500" trigger="click">
              <div>
                <el-link v-if="conf.vol<=0" :icon="v1" @mouseleave="v1=VolumeMuteOutline" @mouseenter="v1=VolumeMuteSharp"
                         style="color: white" :underline="false"></el-link>
                <el-link v-else-if="conf.vol<=10" :icon="v2" @mouseleave="v2=VolumeOffOutline" @mouseenter="v2=VolumeOffSharp"
                         style="color: white" :underline="false"></el-link>
                <el-link v-else-if="conf.vol<=40" :icon="v3" @mouseleave="v3=VolumeLowOutline" @mouseenter="v3=VolumeLowSharp"
                         style="color: white" :underline="false"></el-link>
                <el-link v-else-if="conf.vol<=70" :icon="v4" @mouseleave="v4=VolumeMediumOutline" @mouseenter="v4=VolumeMediumSharp"
                         style="color: white" :underline="false"></el-link>
                <el-link v-else :icon="v5" @mouseleave="v5=VolumeHighOutline" @mouseenter="v5=VolumeHighSharp"
                         style="color: white" :underline="false"></el-link>
              </div>
              <template #dropdown>
                <el-col style="height: 200px">
                  <el-slider v-model="conf.vol" show-stops :step="1" :min="0" :max="100" vertical style="height: 85%;margin-top: 12px"></el-slider>
                </el-col>
              </template>
            </el-dropdown>
          </el-tooltip>
          <el-tooltip content="播放模式"><lx-img :images="[ArrowSyncCircle16Regular,ArrowSyncCircle16Filled]"
                                                 @click="on_playmode"/></el-tooltip>
          <el-tooltip content="播放列表"><lx-img :images="[ReceiptPlay20Regular,ReceiptPlay24Filled]"
                                                 @click="on_playlist"/></el-tooltip>
        </el-space>
      </el-space>

    </el-space>
  </el-row>

</template>

<script setup>
import {VideoPause, VideoPlay} from "@element-plus/icons-vue";
import {PlaySkipBackOutline,PlaySkipForwardOutline,
  VolumeMuteOutline,VolumeMuteSharp,VolumeOffOutline,VolumeOffSharp,
  VolumeLowOutline,VolumeLowSharp,VolumeMediumOutline,VolumeMediumSharp,VolumeHighOutline,VolumeHighSharp
} from '@vicons/ionicons5';
import {
  DocumentQueueMultiple24Regular,DocumentQueueMultiple24Filled,Share16Regular,Share16Filled,Collections20Regular,Collections20Filled,
  ArrowSyncCircle16Regular, ArrowSyncCircle16Filled,ReceiptPlay20Regular,ReceiptPlay24Filled
} from '@vicons/fluent'
import LxImg from "@/components/utils/lx-img.vue";

import {useRoute,useRouter} from 'vue-router'
import {inject,ref,shallowRef} from 'vue'
let route = useRoute(), router = useRouter(), conf = inject('conf')

import {useTest} from '@/components/stores'
import {ElMessage} from "element-plus";
let player_test = useTest()

let playing = ref(false)
let pause_btn_clk = ()=>{
  // playing.value = false
  player_test.pause()
}
let play_btn_clk = ()=>{
  // playing.value = true
  player_test.play()
}
let back_btn_clk = ()=>{
  console.log("back")
}
let forward_btn_clk = ()=>{
  console.log("forward")
}

let v1=shallowRef(VolumeMuteOutline),v2=shallowRef(VolumeOffOutline),v3=shallowRef(VolumeLowOutline),
    v4=shallowRef(VolumeMediumOutline),v5=shallowRef(VolumeHighOutline)

let on_lyrics = ()=>{

}
let on_collect = ()=>{
  ElMessage.success('已收藏')

}
let on_share = ()=>{
  ElMessage.success('已复制到粘贴板')
  // navigator.clipboard.writeText(window.location.href)
}
let on_playmode = ()=>{

}
let on_playlist = ()=>{

}

</script>

<style scoped>
.lx-row-full:first-child::content{
  content: '';
  display: block;
  width: 0;
  height: 100%;
  border: solid 1px grey;
}
</style>