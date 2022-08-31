import os
from PIL import Image
import math
os.system("adb connect 127.0.0.1:62025")
os.system("adb remount")
u=0
while(u==0):
    os.system("adb shell /system/bin/screencap -p /sdcard/screenshot.png")
    os.system("adb pull /sdcard/screenshot.png screenshot.png")

    img=Image.open("screenshot.png")
    img_array=img.load()
    by=[[0 for x in range(2)]for y in range(1000)]

    x=0
    count=0
    for i in range(700):
        ori=img_array[0,300+i]
        for j in range(1079):
            if(img_array[j,300+i]!=ori):
               # print(j,300+i)
                by[count][0]=j
                by[count][1]=300+i
               # print(by[count][0], ",",by[count][1])
                count=count+1
                #绘制
                if(x==0):
                    x=1
#                   for k in range(1079):
#                       img_array[k,300+i]=(255,0,0,0)
#                   for k in range(1919):
#                       img_array[j,k]=(255,0,0,0)
                break

    i=0
    for i in range(count):
        #print("i=",i,"  ",by[1][0], ",",by[1][1])
        img_array[by[i][0],by[i][1]]=(255,0,0,0)
        if(by[i][0]==by[i-1][0]):
            break
        if((by[i][0]-by[i-1][0])>=8 and i>20):
            break
    #for k in range(1079):
    #    img_array[k,by[i-1][1]]=(255,0,0,0)
    #for k in range(1919):
    #    img_array[by[i-1][0],k]=(255,0,0,0)


    for k in range(1079):
        img_array[k,by[i-1][1]]=(255,0,0,0)
    for k in range(1919):
        img_array[by[0][0],k]=(255,0,0,0)
    jieguo1=(by[0][0],by[i-1][1])
    print("jieguo1=",jieguo1[0],",",jieguo1[1])
    i=0
    j=0

    for i in range(1300):
        for j in range(1079):
            if(img_array[j,300+i]==(52,52,59,255)):
                for k in range(1079):
                    img_array[k,300+i+190]=(255,0,0,0)
                for k in range(1919):
                    img_array[j,k]=(255,0,0,0)
                jieguo2=(j,300+i+190)
                x=100
                print("jieguo2=",jieguo2[0],",",jieguo2[1])
                break
        if(x==100):
            break
    juli=math.sqrt(abs(jieguo1[0]-jieguo2[0])**2+abs(jieguo1[1]-jieguo2[1])**2)
    shijian=int(juli/1000*1345)
    print('juli=',juli,'   shijian=',shijian)
    img.show()
    os.system('adb shell input swipe 250 250 251 251 '+str(shijian))
    
    u=int(input("u="))
    