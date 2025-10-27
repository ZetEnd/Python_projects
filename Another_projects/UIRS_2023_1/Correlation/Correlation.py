import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

from matplotlib import image

if __name__ == "__main__":

    # С помощью библиотеки Open_cv
    #img = cv2.imread(r"E:\Programs_VS_2022\Programs_2023\Python_projects\UIRS_2023_1\Correlation\image\one.jpg")

    #img_test = cv2.imread(r"E:\Programs_VS_2022\Programs_2023\Python_projects\UIRS_2023_1\Correlation\image\test_1.jpg")

    #np_img = np.asarray(img)

    #rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    #print(np_img)
    #cv2.imshow('Image', np_img)
    #cv2.waitKey(0)

    ###################################################################################

    # C помощью MatPlotLib
    #img = image.imread(r"E:\Programs_VS_2022\Programs_2023\Python_projects\UIRS_2023_1\Correlation\image\one.jpg")

    #img_test = image.imread(r"E:\Programs_VS_2022\Programs_2023\Python_projects\UIRS_2023_1\Correlation\image\test_1.jpg")

    img = image.imread(r"E:\Programs_VS_2022\Programs_2023\Python_projects\UIRS_2023_1\Correlation\image\ri_new.png")

    img_test = image.imread(r"E:\Programs_VS_2022\Programs_2023\Python_projects\UIRS_2023_1\Correlation\image\ci_3.png")

	
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2GRAY)
    print(img_test.shape)
    print(img.shape)

    #print(img_test.shape[0])
    #print(img.shape[0])
    #print(img_test.shape[1])
    #print(img.shape[1])

    #print(img)



    #plt.imshow(img_test)
    #plt.show()

    img = np.asarray(img)
    img_test = np.asarray(img_test)

    K_0 = np.zeros((img_test.shape[0] - img.shape[0], img_test.shape[1] - img.shape[1]), dtype = np.float64)

    K_mda = np.zeros((img_test.shape[0] - img.shape[0], img_test.shape[1] - img.shape[1]), dtype = np.float64)

    print(K_0.shape[0], K_0.shape[1])

    q = 50
    w = 50
    ri_mean = img.mean()
    ci_mean = img_test.mean()

    ri_cko = 0
    ci_cko = 0

    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            ri_cko += math.pow((img[i,j]- ri_mean),2) 

    ri_cko = np.sqrt(ri_cko/(img.shape[0]*img.shape[1]))

    std_ = np.sqrt(abs(np.var(img)))
    print(" std_" , std_)
    print(" np.std_" , np.std(img))

    max = 0

    qw = []
    for di in range(0, img_test.shape[0] - img.shape[0]):
        for dj in range(0, img_test.shape[1] - img.shape[1]):

            #std_test = np.sqrt(abs(np.var(img_test[di:di+img.shape[0],dj:dj+img.shape[1]])))
            std_test = np.std(img_test[di:di+img.shape[0],dj:dj+img.shape[1]])
            print(" std_test" , std_test)
            for i in range(0, img.shape[0]):
                for j in range(0, img.shape[1]):

                    ri = img[i,j]
                    ci = img_test[i+di, j+dj]

                    corr = (ri - ri_mean)*(ci - ci_mean)

                    corr = corr / (img.shape[0]*img.shape[1])

                    norm_corr = corr/(std_*std_test)

                    K_0[di,dj] += norm_corr

                    if (K_0[di,dj]>0.75):
                        qw.append([di, dj])

                    K_mda[di,dj] += (img[i,j] - img_test[i+di, j+dj])
            
            ci_cko += math.pow((img_test[di,dj]- ci_mean),2) 

            #K_0[di,dj] /= (img_test.shape[0] - img.shape[0])*(img_test.shape[1] - img.shape[1])
            #K_mda[di,dj] /= (img_test.shape[0] - img.shape[0])*(img_test.shape[1] - img.shape[1])

            if (K_0[di,dj] > max) and (K_0[di,dj] > 0.75):
                max = K_0[di,dj]
                q = di
                w = dj



    #ci_cko = np.sqrt(ci_cko/(img_test.shape[0]*img_test.shape[1]))
    #########ci_cko = np.sqrt(ci_cko/((img_test.shape[0]- img.shape[0])*(img_test.shape[1]- img.shape[1])))

    print('cko', ri_cko, ci_cko)

    img_test_norm = img_test[:img_test.shape[0] - img.shape[0],:img_test.shape[1] - img.shape[1]]

    print("img_test_norm", img_test_norm.shape)
    #K_0 /= (np.std(img,ddof= 1)*np.std(img_test,ddof= 1))

    #K_0 /= np.sqrt(ri_cko*ci_cko)
    ##########K_0 /= ri_cko*ci_cko


    #K_mda /= (np.std(img)*np.std(img_test))
    print(np.std(img))
    print(np.std(img_test))
    #############K_0 = K_0 / ((img_test.shape[0] - img.shape[0])*(img_test.shape[1] - img.shape[1])*img.shape[0]*img.shape[1])

    K_0 = np.round(K_0, 8)


    K_mda /= (img_test.shape[0] - img.shape[0])*(img_test.shape[1] - img.shape[1])
    #plt.imshow(img_test)

    print(q, w)
    for di in range(0, img_test.shape[0] - img.shape[0]):
        print("K0", K_0[di]);
        print()

    img_test = cv2.cvtColor(img_test, cv2.COLOR_GRAY2BGR)
    ######start_point = (w, q)
    ######end_point = (w + img.shape[1], q + img.shape[0])
    color = (255, 0, 0)

    for i in range(len(qw)):
        start_point = (qw[i][0], qw[i][1])
        end_point = (qw[i][0] + img.shape[1], qw[i][1] + img.shape[0])
        color = (255, 0, 0)
        img_test_norm = cv2.rectangle(img_test,start_point, end_point,color, 2)

    #img_test_norm = cv2.rectangle(img_test,start_point, end_point,color, 2)
    #plt.imshow(img_test)
    plt.imshow(img_test_norm)
    fig2 = plt.figure()
    plt.imshow(K_0)
    
    fig = plt.figure()
    ax = fig.add_subplot(projection = "3d")
    Y = np.arange(img_test.shape[0] - img.shape[0])
    X = np.arange(img_test.shape[1] - img.shape[1])
    print(X, Y)
    (x ,y) = np.meshgrid(X,Y)

    surf = ax.plot_surface(x, y, K_0)

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(projection = "3d")
    Y1 = np.arange(img_test.shape[0] - img.shape[0])
    X1 = np.arange(img_test.shape[1] - img.shape[1])
    (x1 ,y1) = np.meshgrid(X1,Y1)

    surf1 = ax1.plot_surface(x1, y1, K_mda)
    plt.show()