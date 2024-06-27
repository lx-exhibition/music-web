<script setup lang="ts">
import {useRoute,useRouter} from 'vue-router'
import {inject} from 'vue'
let route = useRoute(), router = useRouter(), conf = inject('conf')

import {get} from '@/components/utils/http'
import moment from 'moment'

let fetch_art = async (search)=>{
  await get(`artist/desc?id=${search}`)
      .then(res => {
        conf.value.artist = res
      })
}
let fetcher = async (search) => {
  let ret = []
  await get(`search?keywords=${search}`)
      .then(res => {
        ret = res.data.result.songs
        ret.forEach((v,i)=>{
          let artist = ''
          v.artists.forEach(art=>{
            artist = `${artist}, ${art.name}`
            console.log(art)
            console.log(art.name)
          })
          ret[i].artists = artist.substring(2)

          ret[i].album = v.album.name

          ret[i].duration = moment.format('mm:ss')
        })

        conf.value.res = ret
        // console.log(conf.value)
      })
  return ret
}

let tab_id = 0

</script>

<template>

<!--  {{conf.value.search}}-->
<!--    {{conf.value.res}}-->

  <div>
    <el-card>
      <el-row justify="center">
        <el-autocomplete v-model="conf.search" :fetch-suggestions="(search,ret)=>ret([{name:search}])" value-key="name"
          :trigger-on-focus="false" :highlight-first-item="true" @select="fetcher"
        >
        </el-autocomplete>
      </el-row>
      <el-row justify="center">
        <el-tabs v-model="tab_id">
          <el-tab-pane v-for="(v,i) in ['单曲','歌手','专辑','视频','歌词','歌单','声音主播','用户']"
            :name="i" :label="v">
            <el-table :data="conf.res">
<!--              <el-table-column prop="id" label="id"/>-->
              <el-table-column prop="name" label="歌曲"/>
              <el-table-column prop="artists" label="歌手"/>
              <el-table-column prop="album" label="专辑"/>
              <el-table-column prop="duration" label="时长"/>
            </el-table>
          </el-tab-pane>
        </el-tabs>
      </el-row>
    </el-card>
  </div>

</template>

<style scoped>

</style>