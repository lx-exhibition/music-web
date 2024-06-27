function __vite__mapDeps(indexes) {
  if (!__vite__mapDeps.viteFileDeps) {
    __vite__mapDeps.viteFileDeps = ["assets/index-DYJcW-bn.js","assets/index-D3KaMA3V.js","assets/index-DfsnMPuq.css","assets/index-CfUfnqk9.js","assets/index-CBoZSA8E.js","assets/index-BzEVeoYc.js","assets/index-6iakGaHm.js","assets/index-DNeNeaL7.js"]
  }
  return indexes.map((i) => __vite__mapDeps.viteFileDeps[i])
}
import{_ as t}from"./index-D3KaMA3V.js";async function s(a,_=!0){const{loadBaseMover:o}=await t(()=>import("./index-DYJcW-bn.js"),__vite__mapDeps([0,1,2])),{loadCircleShape:i}=await t(()=>import("./index-CfUfnqk9.js"),__vite__mapDeps([3,1,2])),{loadColorUpdater:r}=await t(()=>import("./index-CBoZSA8E.js"),__vite__mapDeps([4,1,2])),{loadOpacityUpdater:d}=await t(()=>import("./index-BzEVeoYc.js"),__vite__mapDeps([5,1,2])),{loadOutModesUpdater:e}=await t(()=>import("./index-6iakGaHm.js"),__vite__mapDeps([6,1,2])),{loadSizeUpdater:l}=await t(()=>import("./index-DNeNeaL7.js"),__vite__mapDeps([7,1,2]));await o(a,!1),await i(a,!1),await r(a,!1),await d(a,!1),await e(a,!1),await l(a,!1),await a.refresh(_)}export{s as loadBasic};
