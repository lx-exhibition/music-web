import axios, {InternalAxiosRequestConfig,AxiosResponse} from 'axios';
import {toRaw} from 'vue'
import {ElMessage} from 'element-plus'

let http_ = axios.create({
    baseURL: 'http://localhost:8001/rest', // 设置基础 URL
    headers: {
        'Content-Type': 'application/json',
        // 'Accept': 'application/json',
    },
    timeout: 3000,
    withCredentials: true,
    withXSRFToken: true,
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'X-CSRFToken',
});
// http_.interceptors.request.use((config: InternalAxiosRequestConfig)=>{
//     // 请求前的操作
//     return config
// },(error)=>{
//     // 请求出错的操作
//     return Promise.reject(error)
// })
http_.interceptors.response.use((res: AxiosResponse)=>{
    // code <= 299 的操作
    // console.log(res)
    let {config, data, status, headers} = res
    console.log(`success(${res.config.method}):`, data)
    if (config.method.toUpperCase() !== 'GET'){
        ElMessage.success(`success(${config.method.toUpperCase()} ${config.baseURL} ${status})`)
    }

    return res.data
},(error)=>{
    // code >= 300 的操作\
    let {config,response} = error
    let msg = `error(${config.method.toUpperCase()} ${config.baseURL} ${error.status ? error.status : 400})`
    let server_msg = JSON.stringify(response.data)
    ElMessage.error(`${msg}: ${server_msg}`)
    console.log(server_msg)

    let msg1 = JSON.stringify(error.data)
    // console.log(res.status)
    switch (error.status){
        case 404:
            ElMessage.error(`404: 找不到页面 => ${msg1}`)
            console.log(`404: 找不到页面 => ${msg1}`)
            break
        case 401:
            ElMessage.error(`401: 用户未认证 => ${msg1}`)
            console.log(`401: 用户未认证 => ${msg1}`)
            // window.location.href = '#/login'
            break
        case 400:
            ElMessage.error(`400 => ${msg1}`)
            console.log(`400 => ${msg1}`)
            break
        case undefined:
            // ElMessage.error('status undefined')
            console.log('status undefined')
    }
    return Promise.reject(error)
})
export const http = http_


// type METHOD = 'post' | 'get' | 'put' | 'delete'
type CONTENT_TYPE = string | 'application/x-www-form-urlencoded' | 'multipart/form-data' | 'application/json'

import moment from 'moment'
export const post = async (path: string, data={})=>{
    // data = toRaw(data)
    return await http.post(path, data, {})
}
export const post_f = async (path: string, data={})=>{
    // data = toRaw(data)
    return await http.post(path, data, {headers: {'Content-Type': 'multipart/form-data'}})
}
export const get = async (path: string, params={})=>{
    params = Object.assign(params, {time: moment().format('x')})
    return  await http.get(path, {params: params})
}
export const put = async (path: string, data={})=>{
    return await http.put(path, data, {})
}
export const delete_ = async (path: string)=>{
    return  await http.delete(path, {})
}

export const check = (obj, label)=>{
    obj === undefined ? console.warn(`${label} is not defined`) : 0
}
