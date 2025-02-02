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
# 2304/16*(970-2)/4

for datanum in range(0,1):
    t=os.listdir("page1/")
    t.sort()
    t=t[datanum*1000:(datanum+1)*1000]
    
    w=len(t)
    u=np.zeros([len(t),475,1152], dtype = np.uint64)#1 Conv [[0.25,0.25],[0.25,0.25]] 2304/2,970/2
    ul=np.zeros([len(t)],dtype = np.uint8)

    for files in range(len(t)):
        r=t[files]
        print(files,r)
        k=np.array(Image.open('page1/'+r).convert('L'))
        
        for y in range(0,k.shape[0],2):
            for x in range(0,k.shape[1],2):
                u[files][y//2][x//2]=int(k[y][x]/4+k[y][x+1]/4+k[y+1][x]/4+k[y+1][x+1]/4)
        for x in range(0,k.shape[1],1):
            u[files][-4][x]=int(u[files][-1][x]/4+u[files][-2][x]/4+u[files][-3][x]/4+u[files][-4][x]/4)
        k=np.zeros([len(t),118,72], dtype = np.uint64)#2 Merge 1152/16 *  472/4
        for y in range(0,472,4):
            for x in range(0,1152,16):

                k[files][y//4][x//16]=add([u[y][x+d] for d in range(16)]+[u[y+1][x+d] for d in range(16)]+[u[y+2][x+d] for d in range(16)]+[u[y+3][x+d] for d in range(16)])#k[y][x+7]

        ul[files]=r[r.index('-')+1:r.index('.')]
    k=(k/(2**64)).astype("float16")
    #np.save('page1Piece'+str(datanum+1)+'.npy', u)#10000
    #np.save('page1_labelsPiece'+str(datanum+1)+'.npy', ul)
    