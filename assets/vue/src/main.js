// import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'

let app = createApp(App)

// (1) element-plus 配置
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
// import "element-plus/theme-chalk/src/message.scss";
app.use(ElementPlus)

// (2)  vue-router 配置
import {createRouter, createWebHashHistory, createWebHistory} from 'vue-router'

import Settings from './components/Settings.vue'
import NotFound from "./components/results/404.vue";
import Main from './components/Main.vue'
import Search from './components/pages/Search.vue'

import Recommends from './components/pages/explore/Recommends.vue'
import Ranks from './components/pages/explore/Ranks.vue'
import PlayLists from './components/pages/explore/PlayLists.vue'
import DJ from './components/pages/explore/DJ.vue'
import Artists from './components/pages/explore/Artists.vue'
import Albums from './components/pages/explore/Albums.vue'

import my_Artists from './components/pages/my/Artists.vue'
import Videos from './components/pages/my/Videos.vue'
import DJs from './components/pages/my/DJs.vue'
import CreatedSongLists from './components/pages/my/CreatedSongLists.vue'
import CollectedSongLists from './components/pages/my/CollectedSongLists.vue'
import Home from './components/pages/my/Home.vue'
import Messages from './components/pages/my/Messages.vue'
import Degree from './components/pages/my/Degree.vue'
import VIP from './components/pages/my/VIP.vue'
import my_Settings from './components/pages/my/Settings.vue'
import Authorization from './components/pages/my/Authorization.vue'
import Exit from './components/pages/my/Exit.vue'

import Friends from './components/pages/other/Friends.vue'
import Market from './components/pages/other/Market.vue'
import Artist from './components/pages/other/Artist.vue'
import Advanced from './components/pages/other/Advanced.vue'
import Client from './components/pages/other/Client.vue'

import g_Artist from './components/pages/generic/Artist.vue'
import g_Song from './components/pages/generic/Song.vue'
import g_Album from './components/pages/generic/Album.vue'
import g_Video from './components/pages/generic/Video.vue'
import g_PlayList from './components/pages/generic/PlayList.vue'
import g_Message from './components/pages/generic/Message.vue'

const routes = [
    { path: '/', component: Main },
    // { path: '/HelloWorld', component: HelloWorld },
    // { path: '/TheWelcome', component: TheWelcome },
    // { path: '/WelcomeItem', component: WelcomeItem },
    { path: '/search', component: Search },
    { path: '/settings', component: Settings },
    { path: '/explore', children:[
            {path: 'Recommends', component: Recommends},
            {path: 'Ranks', component: Ranks},
            {path: 'PlayLists', component: PlayLists},
            {path: 'DJ', component: DJ},
            {path: 'Artists', component: Artists},
            {path: 'Albums', component: Albums},
        ]},
    { path: '/my', children:[
            {path: 'Artists', component: my_Artists},
            {path: 'Videos', component: Videos},
            {path: 'DJs', component: DJs},
            {path: 'CreatedSongLists', component: CreatedSongLists},
            {path: 'CollectedSongLists', component: CollectedSongLists},
            {path: 'Home', component: Home},
            {path: 'Messages', component: Messages},

            {path: 'Degree', component: Degree},
            {path: 'VIP', component: VIP},
            {path: 'Settings', component: my_Settings},
            {path: 'Authorization', component: Authorization},
            {path: 'Exit', component: Exit},
        ]},
    { path: '/other', children:[
            {path: 'Friends', component: Friends},
            {path: 'Market', component: Market},
            {path: 'Artist', component: Artist},
            {path: 'Advanced', component: Advanced},
            {path: 'Client', component: Client},
        ]},
    { path: '/g', children:[
            {path: 'Artist', component: g_Artist},
            {path: 'Song', component: g_Song},
            {path: 'Album', component: g_Album},
            {path: 'Video', component: g_Video},
            {path: 'PlayList', component: g_PlayList},
            {path: 'Message', component: g_Message},
        ]},
    { path: '/:other(.*)', component: NotFound },
]

app.use(createRouter({
    // history: createWebHashHistory(),
    history: createWebHashHistory(),
    routes: routes,
    sensitive: false,
    strict: false,
}))

// (3) element-plus 图标配置
// import * as ElementPlusIconsVue from '@element-plus/icons-vue'
// for (const [key, component] of Object.entries(ElementPlusIconsVue)){
//     app.component(key, component)
// }

// (4) animate.css
import 'animate.css'

// (5) xicons

// import * as VIcons from '@vicons/ionicons5'
// for (const [key, component] of Object.entries(VIcons)){
//     app.component(key, component)
// }
// import * as VFluent from '@vicons/fluent'
// for (const [key, component] of Object.entries(VFluent)){
//     app.component(key, component)
// }

// (6) naive
import Naive from 'naive-ui'
app.use(Naive)


// (7)

// ... 依赖注入
import {ref,computed} from 'vue'
app.provide('app', app)
// import {construct} from './components/utils/tool.ts'
import {http} from '@/components/utils/http.ts'
// let imgs = []
// await http.get('img/')
//     .then(res => {
//         imgs = res.data
//     })
// console.log(imgs)
app.provide('conf', ref({
    fold: false,
    mode: true,
    search: '周杰伦', res: [],
    vol: 24,
    // imgs: imgs,
}))



// (8) 背景特效
import Particles from "@tsparticles/vue3";
import { loadSlim } from "@tsparticles/slim"; // if you are going to use `loadSlim`, install the "@tsparticles/slim" package too.

app.use(Particles, {
    init: async engine => {
        // await loadFull(engine); // you can load the full tsParticles library from "tsparticles" if you need it
        await loadSlim(engine); // or you can load the slim version from "@tsparticles/slim" if don't need Shapes or Animations
    },
})

// (9) pinia
import {createPinia} from 'pinia'
const pinia = createPinia()
pinia.use((context) => {
    const {store,options} = context
    // console.log(store)
    // console.log(options)
    return {}
})
app.use(pinia)

// (10) @videojs-player/vue, video.js
import VueVideoPlayer from '@videojs-player/vue'
import 'video.js/dist/video-js.css'
app.use(VueVideoPlayer)


app.mount('#app')
