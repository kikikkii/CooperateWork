import os
import sys
sys.path.append(".")
import re
import imageCutTest as imgCut
from PIL import Image,ImageQt
import PicturesMatch.PicturesMatch2 as pm

# 遍历文件夹
def walkFile(file):
    ImgList = []
    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        


        # 遍历文件
        for f in files:
            #print(os.path.join(root, f))
            ImgList.append(os.path.join(root, f))
            #print(f)
            #image = Image.open(os.path.join(root, f))
            #imgList = imgCut.cut_image(image)
            #imgCut.save_images(imgList,f)

        # 遍历所有的文件夹
        #for d in dirs:
            #print(os.path.join(root, d))

    return ImgList

# 遍历文件夹进行图形匹配'
def picturesMatch(img1,img2):
    print('依据平均哈希算法计算相似度：{}/{}'.format(ah.calaHashSimilarity(img1, img2), 64))


def MatchFirst(ImgList):
    ImgCutpictures = []
    #ImgGetPictures = []
    ImgCutpictures = walkFile("..\cutPictures")
    
    #ImgGetPictures = walkFile(".\getPictures")
    #print(ImgCutpictures)
    #print(ImgGetPictures)
    print("ImgList=" + str(ImgList))
    MatchFiles = {}
    for i in ImgList:
        #img1 = Image.open(i)
        image1 = pm.make_regalur_image(ImageQt.fromqimage(i.toImage()))
        for j in ImgCutpictures:
            img2 = Image.open(j)
            #print(img2)
            image2 = pm.make_regalur_image(img2)
            if pm.calc_similar(image1, image2) == 1.0:
                print(str(i) + "找到匹配了" + j)
                #找到图片最大匹配的文件夹
                j = j.replace("..\cutPictures\\","")
                print(j)
                if(not MatchFiles.get(j[0:j.index("\\")])):
                    MatchFiles[j[0:j.index("\\")]] = 1
                else:
                    MatchFiles[j[0:j.index("\\")]] += 1

                print(pm.calc_similar(image1, image2))
                break
    print(MatchFiles)
    #print(maxMatch(MatchFiles))
    return maxMatch(MatchFiles)

def matchSecond(files,img):
    #重新再找一遍
    ImgCutpictures = []
    ImgCutpictures = walkFile("..\cutPictures\\" + files)
    image1 = pm.make_regalur_image(ImageQt.fromqimage(img.toImage()))
    for j in ImgCutpictures:
        img2 = Image.open(j)
        #print(img2)
        image2 = pm.make_regalur_image(img2)
        if pm.calc_similar(image1, image2) == 1.0:
            print("-----------------------------------")
            print(str(img) + "找到匹配了" + j)
            #找到图片最大匹配的文件夹
            j = j.replace("..\cutPictures\\","")
            print(j)
            print(pm.calc_similar(image1, image2))
            number = re.search(r'\\\d',j).group()
            return(int(number[1]))
    return 0

def maxMatch(files):
    print("+++++++++++++++++++++")
    print(files)
    print("+++++++++++++++++++++")
    mf = ""
    max = 0
    for key,value in files.items():
        print(key + ":" + str(value))
        if (int)(value) > max:
            max = value
            mf = key
    return mf
#if __name__ == '__main__':
 #   main()
