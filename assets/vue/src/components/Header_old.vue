<template>
  <el-row direction="horizontal" justify="center" align="middle" style="height: 100%">
    <el-space>


      <el-link style="font-family: 'Tangerine', serif;font-size: 25px;"
               href="#/" :underline='false'>
        <div>
          <el-avatar src="https://pic3.zhimg.com/80/v2-92d475f7a6938a51f5024fb1114e652a_qhd.jpg" alt="logo" size="large"></el-avatar>
        </div>
        <span>网抑云音乐</span>
      </el-link>

<!--      发现音乐 的下拉菜单-->
      <el-dropdown @command="(cmd) => router.push(`/explore/${cmd}`)" :hide-timeout="50">
        <el-button>发现音乐<el-icon><arrow-down/></el-icon></el-button>
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item v-for="(v,k,i) in [['Recommends','推荐'], ['Ranks','排行榜'], ['SongLists','歌单'], ['DJ','主播电台'],
            ['Artists','歌手'], ['NewAlbum','新碟上架']]" :command="v[0]">
                {{v[1]}}
            </el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>

<!--      我的音乐 的下拉菜单-->
      <el-dropdown @command="(cmd) => router.push(`/my/${cmd}`)" :hide-timeout="50">
        <el-button>我的音乐<el-icon><arrow-down/></el-icon></el-button>
        <template #dropdown>
          <el-dropdown-menu>

            <el-dropdown-item v-for="(v,k,i) in [['Artists','我的歌手'], ['Videos','我的视频'],
             ['DJs','我的电台'], ['CreatedSongLists','创建的歌单'], ['CollectedSongLists','收藏的歌单']]" :command="v[0]">
              {{v[1]}}
            </el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>


<!--     关注, 商城, 音乐人, 云推歌, 下载客户端  -->
      <el-button v-for="(v,k,i) in [['Friends','关注'], ['Market','商城'],
             ['Artist','音乐人'], ['Advanced','云推歌'], ['Client','下载客户端']]" @click="router.push(`/other/${v[0]}`)">
        <span>{{v[1]}}</span>
      </el-button>

<!--      搜索框-->
      <el-autocomplete ref="search" v-model="public_obj.search" placeholder="音乐/视频/电台/用户" :debounce="300"
                       :fetch-suggestions="(str, cb)=>cb(data.filter(createFilter(str)))" value-key="link"
                       :trigger-on-focus="false" highlight-first-item
                       @select="console.log(public_obj.search)"
      >
        <template #prefix><el-icon><Search/></el-icon></template>
      </el-autocomplete>

<!--      头像，及其下拉框-->
      <el-link href="#/HelloWorld" style="margin-left: 20px" :underline="false">
        <el-dropdown>
          <el-avatar src="http://p3.music.126.net/E0hOSpWP4XBov9hsO5KJBA==/109951165422241301.jpg" alt="头像">
          </el-avatar>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item v-for="(v,k,i) in {
                1:['我的主页',InprivateAccount16Regular],2:['我的消息',EmailOutlined],3:['我的等级',Medal],
                4:['vip会员',Smoking],5:['个人设置',Settings48Regular],6:['实名认证',OfficeBuilding],7:['退出',DoorExit]}">
                <el-link :icon="v[1]" :underline="false">
                  {{v[0]}}
                </el-link>
              </el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </el-link>


    </el-space>
  </el-row>
</template>

<script setup>
import {ArrowDown,Medal,Smoking,OfficeBuilding} from "@element-plus/icons-vue";
import {InprivateAccount16Regular,Settings48Regular,} from '@vicons/fluent'
import {EmailOutlined} from '@vicons/material'
import {DoorExit} from '@vicons/tabler'

import {defineModel, ref} from 'vue'
import {useRouter} from 'vue-router'

let router = useRouter()


let public_obj = defineModel()

let search = ref(), search_model = ref()
const createFilter = (str) => {return (item)=>{return item.value.toLowerCase().indexOf(str.toLowerCase()) === 0}}
const data = [
  { value: 'vue', link: 'https://github.com/vuejs/vue' },
  { value: 'element', link: 'https://github.com/ElemeFE/element' },
  { value: 'cooking', link: 'https://github.com/ElemeFE/cooking' },
  { value: 'mint-ui', link: 'https://github.com/ElemeFE/mint-ui' },
  { value: 'vuex', link: 'https://github.com/vuejs/vuex' },
  { value: 'vue-router', link: 'https://github.com/vuejs/vue-router' },
  { value: 'babel', link: 'https://github.com/babel/babel' },
]
// addEventListener()
</script>

<style scoped>

</style>