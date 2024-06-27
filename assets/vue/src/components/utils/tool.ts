import {ref} from 'vue'
export class Lx_Context{
    _: object
    constructor(val) {
        this._ = val
    }
    set value(val){
        this._ = val
    }
    get value(){
        return this._
    }
}
export function construct(val){
    return ref(new Lx_Context(val))
}


export function paginate(data: any[], page_size: number = 5){
    let total = data.length
    let page_num = Math.ceil(total/page_size)
    let pag = []
    for (let i = 0; i < page_num; i++) {
        let now = []
        for (let j = 0; i * page_size + j<total && j < page_size; j++) {
            now.push(data[i * page_size + j])
            // console.log(`${i} ${j}`)
        }
        pag.push(now)
    }
    return pag
}
