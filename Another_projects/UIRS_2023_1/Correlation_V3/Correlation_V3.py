import cv2
from pickle import TRUE


import numpy as np
import matplotlib.pyplot as plt
import math

from matplotlib import image



if __name__ == "__main__":

    rgb_image = cv2.imread(r"E:\Programs_VS_2022\Programs_2023\Python_projects\UIRS_2023_1\Correlation\image\ri_v1.png")
    img = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)
    #img_test = cv2.imread(r"E:\Programs_VS_2022\Programs_2023\Python_projects\UIRS_2023_1\Correlation\image\ci_5.png")

    #print(img)
    #print("qqq")
    #print(np_img)
    #print("www")
    #cv2.imshow('Image', np_img)

    #img = img[:,2:8]
    img = img[:,2:3]



    shape_0 = 480
    shape_1 = 640

    img_shape_0 = img.shape[0]
    img_shape_1 = img.shape[1]

    #scale_percent = 80 #calculate the 50 percent of original dimensions 
    # = int(img_shape_1 * scale_percent / 100) 
    #height = int(img_shape_0 * scale_percent / 100) # dsize 
    #dsize = (width, height) # resize image 
    #img = cv2.resize(img, dsize)

    print(img_shape_1)
    cap = cv2.VideoCapture(0)

    K_0 = np.zeros((shape_0 - img_shape_0, shape_1 - img_shape_1), dtype = np.float64)

    K_mda = np.zeros((shape_0 - img_shape_0, shape_1 - img_shape_1), dtype = np.float64)

    ri_mean = img.mean()

    std_img = np.std(img)

    #step = 10
    x = 0
    y = 0
    max_K = 0

    while(True): 
        ret, frame = cap.read()

        img_test = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        scale_percent = 30 #calculate the 50 percent of original dimensions 
        width = int(shape_1 * scale_percent / 100) 
        height = int(shape_0 * scale_percent / 100) # dsize 
        dsize = (width, height) # resize image 
        img_test = cv2.resize(img_test, dsize)


        for di in range(0, img_test.shape[0] - img.shape[0], 2):
            for dj in range(0, img_test.shape[1] - img.shape[1], 2):

                #std_test = np.sqrt(abs(np.var(img_test[di:di+img.shape[0],dj:dj+img.shape[1]])))
                std_test = np.std(img_test[di:di+img.shape[0],dj:dj+img.shape[1]])
                #print("std_test", std_test)
                ci_mean = img_test[di:di+img.shape[0],dj:dj+img.shape[1]].mean()
                for i in range(0, img.shape[0]):
                    for j in range(0, img.shape[1]):

                        ri = img[i,j]
                        ci = img_test[i+di, j+dj]

                        corr = np.abs(ri - ri_mean)*np.abs(ci - ci_mean)

                        corr = corr / (img.shape[0]*img.shape[1])

                        if(std_test != 0):
                            norm_corr = corr/(std_img*std_test)
                        else:
                            norm_corr = 0

                        K_0[di,dj] += norm_corr

                        K_mda[di,dj] += (img[i,j] - img_test[i+di, j+dj])

                if (K_0[di,dj]>max_K):
                            print("K_0", K_0[di,dj])
                            max_K = K_0[di,dj]
                            x = di
                            y = dj
                            print("qw", x, " ",y)

        cv2.rectangle(img_test, (y,x), (y+img_shape_1, x+img_shape_0), (255, 0, 0), 2)

        K_0 = np.round(K_0, 8)


        K_mda /= (img_test.shape[0] - img.shape[0])*(img_test.shape[1] - img.shape[1])

        cv2.imshow('Video', img_test)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        

    cap.release()
    #cv2.destroyAllWindows()

    