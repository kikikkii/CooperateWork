from PIL import Image
import sys
import os

#将图片切为九宫格的函数
def cut_image(image):
    width,height = image.size
    print(width)
    print(height)
    item_width = int(width/3)
    box_list = []
    for i in range(0,3):
        for j in range(0,3):
            box = (j * item_width,i * item_width , (j + 1) * item_width,(i + 1) * item_width)
            print(box)
            box_list.append(box)
    image_list = [image.crop(box) for box in box_list]
    print(image_list)
    return image_list


#保存图片的函数
def save_images(image_list,savePath = ""):
    index = 1
    for image in image_list:
        Path = savePath.replace(".jpg","")
        if(not (os.path.exists("./cutPictures/" + Path))):
            os.mkdir("./cutPictures/" + Path)
        image.save("./cutPictures/" + Path + "/" + str(index) + savePath)
        index += 1
    return


#保存图片的函数2
def save_images2(image_list):
    index = 1
    for image in image_list:
        image.save("./getPictures/" + str(index) + ".jpg")
        index += 1

if __name__ == '__main__':
    file_path = "imgtest.jpg"
    image = Image.open(file_path)
    image_list = cut_image(image)
    print(image_list)
    save_images2(image_list)
