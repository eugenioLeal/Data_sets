import os
import glob
import random
import numpy as np
import cv2

os.chdir('Images')
fileList = glob.glob('*')
random.shuffle(fileList)
# print(fileList)
# print(len(fileList))


for i in range(len(fileList)):
    os.mkdir()
    os.chdir(fileList[i])
    imageFilesList = glob.glob('*')
    random.shuffle(imageFilesList)
    # print(imageFilesList)
    length = len(imageFilesList)
    print(os.system("pwd"))
    # Preprocessing
    # for im_name in imageFilesList:
    #     image = cv2.imread(im_name, 0)
    #     equalized_image = cv2.equalizeHist(image)
    #     cv2.imwrite(im_name, equalized_image)

    # Split into test and training
    percent = (20 * length) / 100
    percent = int(percent)
    test_list = imageFilesList[:percent]
    train_list = imageFilesList[percent]

    print(f"length {length} percent: {percent} \n train_list: {train_list} test_list: {test_list}")

    os.chdir("..")
