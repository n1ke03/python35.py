/*! (c) Andrea Giammarchi - ISC */
const{isArray:e}=Array,{parse:r}=JSON,s=(e,{s:r})=>e.replace(/"s(\d+)"/g,((e,s)=>r[s])),t=(e,s)=>r(e.replace(/(\S+?)\s*=/g,'"$1":'),((e,r)=>"string"==typeof r?s[r[0]][r.slice(1)]:r)),p=(r,t,p,l)=>{for(let n=0,{length:a}=r,c=a-1;n<a;n++){const a=s(r[n],t);p=p[a]||(p[a]=l&&n===c?[]:{}),e(p)&&(n!==c&&p.length||p.push({}),p=p.at(-1))}return p},l=e=>{const[r,l]=((e,r,s)=>[e.replace(/(["'])(?:(?=(\\?))\2.)*?\1/g,(e=>`"s${r.push(e.slice(1,-1))-1}"`)).replace(/\d{2,}([:-]\d{2}){2}([ T:-][\dZ:-]+)?/g,(e=>`"d${s.push(new Date(e))-1}"`)).replace(/,\s*[\r\n]+/g,", ").replace(/\[\s*[\r\n]+/g,"[").replace(/[\r\n]+\s*]/g,"]"),{s:r,d:s}])(e,[],[]),n={};let a=n;for(let e of r.split(/[\r\n]+/))if((e=e.trim())&&!e.startsWith("#"))if(/^(\[+)(.*?)\]+/.test(e))a=p(RegExp.$2.trim().split("."),l,n,"["!==RegExp.$1);else if(/^(\S+?)\s*=([^#]+)/.test(e)){const{$1:e,$2:r}=RegExp;a[s(e,l)]=t(r.trim(),l)}return n};export{l as parse};
//# sourceMappingURL=toml-DiUM0_qs.js.map
