import http from "node:http";
import fs from "node:fs";
import path from "node:path";
const root=process.cwd();
const types={".html":"text/html; charset=utf-8",".js":"text/javascript; charset=utf-8",".css":"text/css; charset=utf-8",".svg":"image/svg+xml"};
http.createServer((req,res)=>{
  const pathname=decodeURIComponent(new URL(req.url,"http://127.0.0.1").pathname);
  const relative=pathname==="/"?"/index.html":pathname;
  const file=path.resolve(root,"."+relative);
  if(!file.startsWith(root)){res.writeHead(403);res.end("Forbidden");return}
  fs.readFile(file,(error,data)=>{
    if(error){res.writeHead(404);res.end("Not found");return}
    res.writeHead(200,{"Content-Type":types[path.extname(file)]||"application/octet-stream"});
    res.end(data);
  });
}).listen(8765,"127.0.0.1");
