import requests
from PIL import Image
import io
import json
H={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Upgrade-Insecure-Requests": "1",
            "Priority": "u=0, i",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache"
        }
def down(url, path, slice):
    response = requests.get(url,headers=H)
    if response.status_code == 200:
        img = Image.open(io.BytesIO(response.content)).convert('L').crop(slice)

        img.save(path)
    else:
        print('Failed')

        #"headers": 

def httpget(url, **kwargs):
    #try:
    response = requests.get(url, **kwargs)
    
    if response.status_code == 200:
        response.encoding='utf8'
        return response.text
    #except requests.exceptions.RequestException as e:
    #    print(f"An error occurred: {e}")
    #    return None
def t(id):
    #try{
    t0=httpget("https://yunyj.linyi.net/wechat/imgs?eg=90361&sid="+id+"&eid=903610003")
    r=json.loads(t0[t0.index("var imgs")+11:t0.index("var tmpl")-4]);
    u0=json.loads(t0[t0.index("var tmpl")+11:t0.index("var score")-4]);
    y=json.loads(t0[t0.index("var score")+12:t0.index("var font1")-4])
    return [r,y,u0]
    #}catch(err){
    #    console.log("An err")
    #    return ["err"]
    #}

rlist=[
    2010, 2020, 2030, 2080,
    2090, 2220, 2230, 2231,
    2300,
    2301, 2310, 2320, 2330,
    2510, #TrainTest 2520, :2580
  ]
errr=[]
Page0=(1290,165+150,2395,1598)
Page1=(67,292,2371,1262)
errnum=0

#MAIN
i=1
for school in rlist:
    for ischool in range(4):
        yu=str(school)+'0'+str(ischool)
        while errnum<=20:
            print(i)
            try:
                f=t(yu+str(i).zfill(4));
                if not f[1]:
                    errnum+=1
                    errr.append(yu+str(i).zfill(4))
                else:
                    errnum-=1
                    if errnum<0:
                        errnum=0
                    if f[1]['itemdetail'][1]['score']!=0 and f[1]['itemdetail'][2]['score']!=0:
                        down(f[0][0]['url'],f"sharp/{f[1]['code']}-{int(f[1]['itemdetail'][1]['score']*2)}.jpg",Page0)
                        down(f[0][1]['url'],f"page1/{f[1]['code']}-{int(f[1]['itemdetail'][2]['score']*2)}.jpg",Page1)

            except Exception as e:
                errnum+=1
                errr.append(yu+str(i).zfill(4))
            #}
            i+=1
        print(errr)
