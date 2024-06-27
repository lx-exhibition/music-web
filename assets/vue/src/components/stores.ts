import {defineStore} from 'pinia'
import {ElMessage} from 'element-plus'

import {computed,ref,reactive,watchEffect} from 'vue'
import moment from 'moment'
// export const useTest = defineStore('test player', ()=>{
//     let audio = reactive(new Audio())
//     let percentage = ref(0)
//     let time = ref('00:00'), total = ref('--:--')
//     let playing = ref()
//     audio.volume = 1
//     audio.playbackRate = 2
//
//     audio.oncanplay = ()=>{
//         audio.ontimeupdate = ()=>{
//             percentage.value = audio.currentTime/audio.duration*100
//             time.value = moment(audio.currentTime*1000).format('mm:ss')
//             total.value = moment(audio.duration*1000).format('mm:ss')
//             console.log(audio.volume,audio.playbackRate,audio.paused)
//         }
//     }
//     function load(src){
//         audio.pause()
//         audio.src = src
//     }
//     function play(){ audio.play(); playing.value = true }
//     function pause(){ audio.pause(); playing.value = false }
//     function flip(){ audio.paused ? play() : pause() }
//     function load_play(src){ load(src); play() }
//
//     return {
//         audio,percentage,time,total,playing,
//         load,play,pause,flip,load_play,
//     }
// })

export const useTest = defineStore('test player', ()=>{
    let song = ref({img: 'http://localhost:8001/rest/img/?id=141'})
    watchEffect(()=>console.log(song.value))

    let audio = new Audio()
    let percentage = ref(0)
    let time = ref('00:00')
    let total = ref('--:--')
    let playing = ref(false)
    let c_circle = computed(()=>playing.value ? 'animate-slow-spin' : '')
    let vol = ref(100)
    watchEffect(()=> audio.volume = vol.value/100 )
    let rate = ref(1)
    watchEffect(()=> audio.playbackRate = rate.value )


    audio.oncanplay = ()=>{
        total.value = moment(audio.duration*1000).format('mm:ss')
        audio.ontimeupdate = ()=>{
            percentage.value = audio.currentTime/audio.duration*100
            time.value = moment(audio.currentTime*1000).format('mm:ss')

            // console.log(audio.volume,audio.playbackRate,audio.paused)
        }
        audio.onplay = ()=>{ playing.value = true }
        audio.onpause = ()=>{ playing.value = false }
    }
    function load(song_){
        audio.pause()
        song.value = song_
        audio.src = song_.data
    }
    function play(){
        audio.play()
    }
    function pause(){ audio.pause() }
    function flip(){ audio.paused ? play() : pause() }
    function load_play(song_){ load(song_); play() }

    return {
        audio,percentage,time,total,playing,song,vol,rate,
        c_circle,
        load,play,pause,flip,load_play,
    }
})

export const useTheme = defineStore('theme', {
    state: ()=>({light: false, flod: false, vol: 23}),
    getters: {
        text: (s)=>s.light ? '#ffffff' : '#000000',
        bg: (s)=>s.light ? '#000000' : '#ffffff',
        c_theme: (s)=>!s.light ? 'bg-white text-black' : 'bg-black text-white',
    }
})

