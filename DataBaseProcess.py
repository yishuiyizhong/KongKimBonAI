from PIL import Image
import numpy as np
import os
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

for datanum in range(1):
    t=os.listdir("sharp/")
    t.sort()
    t=t[30000:]
    w=len(t)
    u=np.zeros([len(t),320,69], dtype = np.uint64)#(1105-1)/16=69,,(1283-3)/4=320
    ul=np.zeros([len(t)],dtype = np.uint8)

    # 打开图像文件
    for files in range(len(t)):
        r=t[files]
        print(files,r)
        k=np.array(Image.open('sharp/'+r).convert('L'))
        for y in range(0,k.shape[0]-3,4):
            for x in range(0,k.shape[1]-1,16):

                u[files][y//4][x//16]=add([k[y][x+d] for d in range(16)]+[k[y+1][x+d] for d in range(16)]+[k[y+2][x+d] for d in range(16)]+[k[y+3][x+d] for d in range(16)])#k[y][x+7]

        ul[files]=r[r.index('-')+1:r.index('.')]
    u=(u/(2**64)).astype("float16")
    np.save('sharpPiece'+str(datanum+1)+'.npy', u)#10000
    np.save('sharp_labelsPiece'+str(datanum+1)+'.npy', ul)
    #(1105-1)*(1283-3)