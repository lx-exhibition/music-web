function __vite__mapDeps(indexes) {
  if (!__vite__mapDeps.viteFileDeps) {
    __vite__mapDeps.viteFileDeps = []
  }
  return indexes.map((i) => __vite__mapDeps.viteFileDeps[i])
}
import{_ as t}from"./index-D3KaMA3V.js";async function r(a,e=!0){const{LineDrawer:i}=await t(()=>import("./LineDrawer-1OQKWYNc.js"),__vite__mapDeps([]));await a.addShape("line",new i,e)}export{r as loadLineShape};
