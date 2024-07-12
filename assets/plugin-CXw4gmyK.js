function __vite__mapDeps(indexes) {
  if (!__vite__mapDeps.viteFileDeps) {
    __vite__mapDeps.viteFileDeps = ["assets/LinksPlugin-uMyV7-82.js","assets/index-Cz9OmzVi.js","assets/index-DfsnMPuq.css"]
  }
  return indexes.map((i) => __vite__mapDeps.viteFileDeps[i])
}
import{_ as o}from"./index-Cz9OmzVi.js";async function r(i,n=!0){const{LinksPlugin:t}=await o(()=>import("./LinksPlugin-uMyV7-82.js"),__vite__mapDeps([0,1,2])),a=new t;await i.addPlugin(a,n)}export{r as loadLinksPlugin};
