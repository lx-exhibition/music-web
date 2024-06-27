
<template>
  <el-color-picker v-model="color" color-format="hex" show-alpha
                   :predefine="['#1e1f22','#656697','#39926b','#51a7de','#c22329']"
  />
  {{color}}

  <el-date-picker v-model="datetime" type="month" placeholder="select date and time"
                  :default-time="new Date()" :shortcuts="shortcuts"
  />
  {{datetime}}

  <el-time-picker v-model="time" arrow-control/>

  <el-radio-group v-model="radio">
    <el-radio-button value="tr">歌姬</el-radio-button>
    <el-radio value="geji" size="default" disabled border>智障</el-radio>
    <el-radio value="gejsi" size="large">歌姬</el-radio>
  </el-radio-group>
  {{radio}}

  <el-row>
    <el-rate v-model="rate" :colors="c" allow-half :texts="['垃圾','还可以','还行','还不错','针布戳']" show-text
             :icons="[Search,School,Scissor]"  show-score score-template="才 {value} 分，垃圾"
             :max="10" :low-threshold="4" :high-threshold="8"
    />
    <el-color-picker v-model="c[0]"/>
    <el-color-picker v-model="c[1]"/>
    <el-color-picker v-model="c[2]"/>
  </el-row>

  <el-select v-model="select1" multiple filterable :max-collapse-tags="3" collapse-tags collapse-tags-tooltip
             style="width: 300px; float:right;" :multiple-limit="3">
    <!--    <el-option-group v-for="(v,i) in select_opts" :label="`group-${i}`">-->
    <!--      <el-option v-for="(w,j) in v" :value="`value-${w}`" :key="j">-->
    <!--        <span style="float: left">label-{{w}}</span>-->
    <!--        <span style="float: right; font-size: 10px; color: #909399">value-{{w}}</span>-->
    <!--      </el-option>-->
    <!--    </el-option-group>-->
    <template #header>
      <el-switch v-model="switch_" active-text="添加选项" inactive-text="关闭添加" inline-prompt
                 style="float: right"
      />
      <div v-if="switch_">
        <el-button @click="()=>{num=Math.min(++num,20)}" style="float: left ">添加</el-button>
        <el-button @click="()=>{num=Math.max(--num,0)}" style="float: left ">减少</el-button>
      </div>
      <br/>
      <br/>
    </template>
  </el-select>
  {{select1}}

  <el-select v-model="select2.model" multiple reserve-keyword filterable remote :remote-method="on_remote"
             :loading="select2.loading" loading-text="正在加载">
    <el-option v-for="(v) in select2.options" :label="`label-${v}`" :value="`value-${v}`"/>
  </el-select>
  {{select2}}


  <el-checkbox-group v-model="checkboxs.model">
    <el-checkbox value="ojpoi" border/>
    <el-checkbox value="ojpi" border/>
    <el-checkbox value="ojpi12" checked/>
    <el-checkbox value="ojpi122" indeterminate/>
    <el-checkbox-button value="btn" label="button"/>
  </el-checkbox-group>
  <br/>{{checkboxs.model}}

  <el-transfer v-model="tranfer.model" :data="tranfer.data"></el-transfer>
  {{tranfer.model}}

  <el-select-v2 v-model="select_v2.model" :options="select_v2.options" value-key="key" multiple filterable/>
  {{select_v2.model}}

  <div>
    <el-time-select v-model="time_sel.model1" start="00:00" end="23:59" :max-time="time_sel.model2"
                    style="width: 50%; float: left"/>
    <el-time-select v-model="time_sel.model2" start="00:00" end="23:59" :min-time="time_sel.model1"
                    style="width: 50%; float: right"/>
    {{time_sel}}
  </div>


</template>

<script setup lang="ts">
import {Setting,Search,School,Scissor} from '@element-plus/icons-vue'

import {ref,onMounted} from 'vue'
let color = ref(''), datetime = ref(), time = ref(), radio = ref(), rate = ref(2.3)
let c=ref(['#99a9bf','#f7ba2a','#ff9900'])
import moment from 'moment'


let t = [
  moment(),
  moment().subtract(1,'d'),
  moment().subtract(1,'w'),
  moment().subtract(1,'M'),
  moment().subtract(1,'y')
]
let shortcuts = ref([
  {text: 'today', value: ()=>moment()},
  {text: 'yesterday', value: ()=>moment().subtract(1,'d')},
  {text: 'last week', value: ()=>moment().subtract(1,'w')},
  {text: 'last month', value: ()=>moment().subtract(1,'m')},
  {text: 'last year', value: ()=>moment().subtract(1,'y')},
])
onMounted(()=>{
  setInterval(()=>{
    for (let i = 0; i < 5; i++) {
      t[i] = t[i].add(1,'s')
    }
  },1000)
})

let select1 = ref({}), num = ref(10)
let switch_ = ref()
import {paginate} from '@/components/utils/tool'
let make_opts = (num)=>{
  let opts = []
  for (let i = 0; i < num; i++) {
    opts.push(i+1)
  }
  return paginate(opts, 3)
}
let select_opts = make_opts(10)


let select2 = ref({model: '', options: 0, loading: false})
let on_remote = (query)=>{
  select2.value.loading = true
  setTimeout(()=>{
    select2.value.loading = false
    select2.value.options = Math.floor(Math.random()*10)+2
  },Math.floor(Math.random()*800))
}

let checkboxs = ref({model: []})

let tranfer = ref({model: [], data: []})
let _ = Math.floor(Math.random()*100)
for (let i = 0; i < _; i++) {
  tranfer.value.data.push({key: `key-${i}`, label: `label-${i}`, disabled: Math.random()>0.8})
}

let select_v2 = ref({model: [], options: []})
_ = Math.floor(Math.random()*15)+5
for (let i = 1; i <= _; i++) {
  let __ = Math.floor(Math.random()*15)+5, opts = []
  for (let j = 1; j <= __; j++) {
    opts.push({value: `value-${j}`, label: `label-${j}`, disabled: Math.random()>0.7})
  }
  select_v2.value.options.push({value: `g-value-${i}`, label: `g-label-${i}`, disabled: Math.random()>0.8,
    options: opts
  })
}


let time_sel = ref({model1: '', model2: ''})

</script>

<style scoped>

</style>