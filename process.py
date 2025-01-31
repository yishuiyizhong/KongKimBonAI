from PIL import Image
import numpy as np
import sys
from tensorflow.keras.models import load_model
import requests
import io
import json

def httpget(url, **kwargs):
    #try:
    response = requests.get(url, **kwargs)
    
    if response.status_code == 200:
        response.encoding='utf8'
        return response.text
def t(url):
    #try{
    t0=httpget(url)
    r=json.loads(t0[t0.index("var imgs")+11:t0.index("var tmpl")-4]);
    #u0=json.loads(t0[t0.index("var tmpl")+11:t0.index("var score")-4]);
    #y=json.loads(t0[t0.index("var score")+12:t0.index("var font1")-4])
    return r[0]['url']

H={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Upgrade-Insecure-Requests": "1",
            "Priority": "u=0, i",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache"
        }

model=load_model("EngTextAll0.4364.keras")
if sys.argv[-1].startswith("https://yunyj.linyi.net/wechat/imgs?"):
    res =requests.get(t(sys.argv[-1]),headers=H)
    img = Image.open(io.BytesIO(res.content)).convert('L').crop((1290,165+150,2395,1598))
else:
    img = Image.open(sys.argv[-1]).crop((1290,165+150,2395,1598))

def trans(p):
    if(p>=123):
        return 0
    else:
        return 1
def add(arr):
    yp=0
    for it in range(len(arr)):
        yp+=trans(arr[it])<<(len(arr)-it-1)
    return yp

u=np.zeros([1,320,69], dtype = np.uint64)


k=np.array(img.convert('L'))
for y in range(0,k.shape[0]-3,4):
    for x in range(0,k.shape[1]-1,16):
        u[0][y//4][x//16]=add([k[y][x+d] for d in range(16)]+[k[y+1][x+d] for d in range(16)]+[k[y+2][x+d] for d in range(16)]+[k[y+3][x+d] for d in range(16)])#k[y][x+7]
u=(u/(2**64)).astype("float16")
h=model.predict(u)
print('Predict point:'+str(np.argmax(h)/2))
#(1105-1)*(1283-3)