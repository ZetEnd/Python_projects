import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

from matplotlib import image

if __name__ == "__main__":

    # C помощью MatPlotLib
    img = image.imread(r"E:\Programs_VS_2022\Programs_2023\Python_projects\UIRS_2023_1\Correlation\image\ri_v1.png")

    img1 = image.imread(r"C:\Users\ptimo\Desktop\8_1.jpg")

    img_test = image.imread(r"E:\Programs_VS_2022\Programs_2023\Python_projects\UIRS_2023_1\Correlation\image\ci_5.png")

	
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2GRAY)
    print(img_test.shape)
    print(img.shape)


    img = np.asarray(img)
    img_test = np.asarray(img_test)
    #img = img[:,2:8]
    K_0 = np.zeros((img_test.shape[0] - img.shape[0], img_test.shape[1] - img.shape[1]), dtype = np.float64)

    K_mda = np.zeros((img_test.shape[0] - img.shape[0], img_test.shape[1] - img.shape[1]), dtype = np.float64)

    print(K_0.shape[0], K_0.shape[1])

    ri_mean = img.mean()
    ci_mean = img_test.mean()


    std_ = np.sqrt(abs(np.var(img)))
    print(" std_" , std_)
    print(" np.std_" , np.std(img))

    #img = img[:,2:4]
    max_K = 0

    plt.imshow(img1)
    plt.show()

    plt.imshow(img)
    print('ssss')
    print(img)
    print(img.shape[0], "there ",img.shape[1])
    print('ssss')

    plt.show()

    step = 1

    qw = []
    q = 0
    w =0
    for di in range(0, img_test.shape[0] - img.shape[0], step):
        for dj in range(0, img_test.shape[1] - img.shape[1], step):

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
                        norm_corr = corr/(std_*std_test)
                    else:
                        norm_corr = 0

                    K_0[di,dj] += norm_corr

                    K_mda[di,dj] += (img[i,j] - img_test[i+di, j+dj])

            if (K_0[di,dj]>max_K):
                        print("K_0", K_0[di,dj])
                        #print("K_0", K_0[di,dj])
                        max_K = K_0[di,dj]
                        #q = di
                        #w = dj
                        print("qw", q, " ",w)
                        qw.append([di, dj])

    K_0 = np.round(K_0, 8)


    K_mda /= (img_test.shape[0] - img.shape[0])*(img_test.shape[1] - img.shape[1])


    #for di in range(0, img_test.shape[0] - img.shape[0]):
    #    print("K0", K_0[di]);
    #    print()

    img_test = cv2.cvtColor(img_test, cv2.COLOR_GRAY2BGR)

    img_test_draw = img_test.copy()
    color = (255, 0, 0)

    stop = False
    K_ = K_0.copy()
    print("K_", K_)

    #q, w = np.unravel_index(np.argmax(K_0), K_0.shape)

    while(K_.any() > 0.9):
        #qw.append([di, dj])
        q = np.argmax(K_)%K_.shape[1] 
        w = np.argmax(K_)//K_.shape[1] 
        qw.append([q, w])

        start_point = (w, q)
        end_point = (w + img.shape[1], q + img.shape[0])

        color = (255, 0, 0)
        #img_test_draw = cv2.rectangle(img_test_draw,start_point, end_point,color, 2)
        cv2.rectangle(img_test_draw,start_point, end_point,color, 2)

        print(q, "wwwwwwwwwwwwwwwwwwwwwwwwwwwww", w)
        print("K_K_",K_[q-img.shape[0]:q+img.shape[0],w-img.shape[1]:w+img.shape[1]])

        K_[q-img.shape[0]:q+img.shape[0],w-img.shape[1]:w+img.shape[1]] = 0
        #K_[q,w] = 0
        K_[w:w+ img.shape[1],q:q + img.shape[0]] = 0
        K_[w- img.shape[1]:w,q - img.shape[0]:q] = 0
        #print("K_[q,w]",K_[q,w])
        print("K_[q,w]",K_[w,q])

        print("max", np.argmax(K_))
        print(K_)


    print("base",K_0[60:70,270:280])
    #q = np.argmax(K_0, axis = 0)
    #w = np.argmax(K_0, axis = 1)
    start_point = (w, q)
    end_point = (w + img.shape[1], q + img.shape[0])

    color = (255, 0, 0)
    #img_test_draw = cv2.rectangle(img_test_draw,start_point, end_point,color, 2)
    cv2.rectangle(img_test_draw,start_point, end_point,color, 2)

    K_linear = K_.reshape(K_.size)
    print("K_linear w",K_linear)

    k_max_ind = np.argmax(K_linear)
    K_max = K_linear[k_max_ind]
    print("K_.argmax()",k_max_ind)

    print("K_max",K_max)
    q = K_max//K_.shape[0]
    w = K_max % K_.shape[0]

    print("q w",q,w)


    #while(stop != True):
    #    q_new, w_new = np.unravel_index(np.argmax(K_), K_.shape)
    #    if (K_[q_new,w_new] not in K_[q+1:q + img.shape[1],w+1:w + img.shape[0]]) and (K_[q_new,w_new] > 0.75):

    #        start_point = (q, w)
    #        end_point = (q + img.shape[1], w + img.shape[0])
    #        color = (255, 0, 0)
    #        img_test_draw = cv2.rectangle(img_test,start_point, end_point,color, 2)

    #        K_[q_new,w_new] = -1

    #        K_linear = K_.reshape(K_.size)
    #        K_max = K_linear[K_.argmax()]

    #        i = K_max//K_.shape[0]
    #        j = K_max % K_.shape[0]
    #        q, w = np.unravel_index(np.argmax(K_), K_0.shape)



    #    K_[q_new,w_new] = -1
    #    q_new, w_new = np.unravel_index(np.argmax(K_), K_.shape)

    #    if (K_[q_new,w_new] < 0.75):
    #        stop = True


    #for i in range(len(qw)):
    #    if K_0[q,w] in K_0[q:q + img.shape[1],w:w + img.shape[0]]:
    #        continue

    #    K_ = K_0[qw[i][0]:qw[i][0] + img.shape[1],qw[i][1]:qw[i][1] + img.shape[0]]
    #    q, w = np.unravel_index(np.argmax(K_), K_0.shape)

    #    print(q,w)
    #    #if ()
    #    #start_point = (qw[i][0], qw[i][1])
    #    #end_point = (qw[i][0] + img.shape[1], qw[i][1] + img.shape[0])

        ####################################################################
    #start_point = (q, w)
    #end_point = (q + img.shape[1], w + img.shape[0])

    #color = (255, 0, 0)
    #img_test_draw = cv2.rectangle(img_test,start_point, end_point,color)
        #####################################################################

    #for i in range(qw):
    #    K_ = K_0[i[0]:i[0] + img.shape[1],i[1]:i[1] + img.shape[0]]
    #    ind = np.unravel_index(np.argmax(K), K_0.shape)

    #    print(ind)
    #    if 
    #    start_point = (qw[i][0], qw[i][1])
    #    end_point = (qw[i][0] + img.shape[1], qw[i][1] + img.shape[0])
    #    color = (255, 0, 0)
    #    img_test_draw = cv2.rectangle(img_test,start_point, end_point,color, 2)


    #img_test_norm = cv2.rectangle(img_test,start_point, end_point,color, 2)
    #plt.imshow(img_test)
    plt.imshow(img_test_draw)
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
