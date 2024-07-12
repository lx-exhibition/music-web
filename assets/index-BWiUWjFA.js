function __vite__mapDeps(indexes) {
  if (!__vite__mapDeps.viteFileDeps) {
    __vite__mapDeps.viteFileDeps = ["assets/CircleDrawer-yNp7YHQ9.js","assets/index-Cz9OmzVi.js","assets/index-DfsnMPuq.css"]
  }
  return indexes.map((i) => __vite__mapDeps.viteFileDeps[i])
}
import{_ as i}from"./index-Cz9OmzVi.js";async function o(a,e=!0){const{CircleDrawer:r}=await i(()=>import("./CircleDrawer-yNp7YHQ9.js"),__vite__mapDeps([0,1,2]));await a.addShape("circle",new r,e)}export{o as loadCircleShape};
