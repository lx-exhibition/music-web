<script setup>
import {DotCircleRegular,DotCircle} from '@vicons/fa'
import {ReadMoreRound} from '@vicons/material'

import {ref,inject} from 'vue'
import {useRouter,useRoute,useLink} from 'vue-router'
import LxCards from "@/components/utils/lx-cards.vue";
import LxItem from "@/components/utils/lx-item.vue";
import LxItems from "@/components/utils/lx-items.vue";
import LxCarousel from "@/components/utils/lx-carousel.vue";
let route = useRoute()

let data1 = [], tags1 = [], _ = ['华语','流行','摇滚','民谣','电子']
for (let i = 0; i < 12; i++) {
  data1.push({title: '[一周原创发现] GALI带你在音乐里作画', img: 'http://p1.music.126.net/JgyxyMzPCVifu_ke2Ub6Kw==/109951169454601351.jpg',
    id: 'data-id'})
}
for (let i = 0; i <6; i++) {
  tags1.push({label: _[i], id: _[i]})
}
let data2 = []
for (let i = 0; i < 10; i++) {
  data2.push({title: '星穹铁道～知更鸟～使一颗心免于哀伤', img: 'http://p1.music.126.net/8uH-heC-hJ18QKyQODhOmg==/109951169265478360.jpg',
    id: 'data-id'})
}

let pri_objs = [], sub_objs = [], imgs = []
for (let i = 0; i < 8; i++) {
  pri_objs.push({title: `葡萄成熟时${i}`, path: '#/song', id: i})
  sub_objs.push({title: `陈奕迅${i}`, path: `#/explore/Artists`, id: i})
  imgs.push('http://p1.music.126.net/xuFy0k8O_xKuAqbbjC24Ig==/109951166497586944.jpg')
}
console.log(imgs)
// http://p1.music.126.net/xuFy0k8O_xKuAqbbjC24Ig==/109951166497586944.jpg

</script>

<template>
<!--  {{route.fullPath}}-->
  <div>
    <el-scrollbar>
      <el-carousel height="300px" arrow="always" direction="horizontal" type="card">
        <el-carousel-item v-for="(v) in ['cIF0zVh9LdoKYMGHGChD2g==/109951169457307033.jpg','RJclxzQoZ4PqAoF8VdkKRg==/109951169457307633.jpg',
  'ahTmwbFHsTrXvkpDZhT5yQ==/109951169456971307.jpg','iArWYllwWXYm6GWPkaVSaw==/109951169457543712.jpg','OyYaLj9JBivdUYsPT9DELA==/109951169456989019.jpg',
  '2JSQ0um8RMTDk1qzkhH-vA==/109951169456987218.jpg','6X8kP26YkneLIqn4wmwj3Q==/109951169456993616.jpg']">
          <img :src="`http://p1.music.126.net/${v}?imageView&quality=89`" style="height: 100%"/>
        </el-carousel-item>
      </el-carousel>

      <!--  <el-divider content-position="left" border-style="solid"/>-->
      <lx-cards title="热门推荐" path="#/explore/SongLists" :data="data1" :tags="tags1">
        <template #aside>
          <lx-items :pri-objs="pri_objs" :sub-objs="sub_objs" :imgs="imgs"/>
          <!--        <lx-items :pri-objs="pri_objs" :sub-objs="sub_objs" :imgs="imgs"/>-->
        </template>
      </lx-cards>

      <lx-cards title="新碟上架" path="#/explore/NewAlbum" :data="data2"/>

      <lx-carousel :pri-objs="pri_objs" :sub-objs="sub_objs" :imgs="imgs"/>

    </el-scrollbar>
  </div>


</template>

<style scoped>

</style>