const sharp = require('sharp');

async function down(url,path,slice){
    var img=await fetch(url, {
        "credentials": "omit",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Upgrade-Insecure-Requests": "1",
            "Priority": "u=0, i",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache"
        },
        "method": "GET",
        "mode": "cors"
    }).then(e=>e.arrayBuffer())//.then(r=>fs.writeFileSync(path,Buffer.from(r)));
    sharp(img).extract(slice).toColorspace('b-w').toFile(path)//(1295,167) to (2364,1594)
}

topc=[]

var t0;
var r;
var u0;
var y;
async function t(id){
    try{
        t0=await fetch("https://yunyj.linyi.net/wechat/imgs?eg=90361&sid="+id+"&eid=903610003").then(e=>e.text());
        r=JSON.parse(t0.slice(t0.indexOf("var imgs")+11,t0.indexOf("var tmpl")-4));
        u0=JSON.parse(t0.slice(t0.indexOf("var tmpl")+11,t0.indexOf("var score")-4));
        y=JSON.parse(t0.slice(t0.indexOf("var score")+12,t0.indexOf("var font1")-4))
        return [r,y,u0]
    }catch(err){
        console.log("An err")
        return ["err"]
    }
}
[
    2010, 2020, 2030, 2080,
    2090, 2220, 2230, 2231,
    2240 , 2290, 2300,
    2301, 2310, 2320, 2330,
    2510, 2520, 2580
  ]
var errr=[]
const Page0={width:2400-1295,height:1600-167-150,left:1290,top:165+150}
const Page1={width:2371-67,height:1262-292,left:67,top:292}//(67,292)=>(2371,1262)
var errnum=0;
async function main(){
    var i=1;
    const yu="22402"
    while(errnum<=10){console.log(i)
        try{
            var f=await t(yu+String(i).padStart(4,'0'));
            if(!f[1]){errnum++;errr.push(yu+String(i).padStart(4,'0'));i++;continue;}
            errnum--;
            errnum=errnum<0?0:errnum;
            //await down(f[0][0].url,'topc/'+f[1].schoolname+'-'+f[1].name+'-'+f[1].code+'-0.jpg');
            if(f[1].itemdetail[1].score!=0&&f[1].itemdetail[2].score!=0){
                down(f[0][0].url,`sharp2/${f[1].code}-${f[1].itemdetail[1].score*2}.jpg`,Page0)
                down(f[0][1].url,`page1/${f[1].code}-${f[1].itemdetail[2].score*2}.jpg`,Page1)
            }
            
            /*image=await loadImage(f[0][1].url);
            canvas = createCanvas(image.width,image.height)
            ctx = canvas.getContext('2d');
            ctx.drawImage(image, 0, 0);
            drawScore(2,ctx,f[2],f[1]);
            canvas.createJPEGStream().pipe(fs.createWriteStream('j/'+f[1].schoolname+'-'+f[1].name+'-'+f[1].code+'-1.jpg'))*/
            //await down(f[0][1].url,'topc/'+f[1].schoolname+'-'+f[1].name+'-'+f[1].code+'-1.jpg');
        }catch(err){
            errnum++;errr.push(yu+String(i).padStart(4,'0'))
        }
        i++
    }
    console.log(JSON.stringify(errr))
}
main()