import {defineStore} from 'pinia'
import {ref,computed} from 'vue'

export const use_counter = defineStore('counter',()=>{
    const my_ref = ref(0)
    const my_computed = computed(()=>my_ref)
    function my_method (){}
    return {my_ref, my_computed, my_method}
},{my_opt1: 'hello', my_opt2: 'world'})

// import { defineStore } from 'pinia'
// export const use_counter = defineStore('counter',{
//     // data
//     state: ()=>{
//         return {count: 0}
//     },
//     // rel-data
//     getters: {
//         doubled: (state)=>state.count*2,
//     },
//     // method
//     actions: {
//         add(){this.count++},
//     }
// })