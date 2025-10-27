# 1) Считать картинку с экрана
# 2) По событию выделить эталон
# 3) Получать координаты эталона
import numpy as np
import cv2 as cv
from numba import njit
import matplotlib.pyplot as plt 

ri = np.zeros((10,10),dtype=np.uint8)
use_kor = True

@njit(fastmath=True)
def raznostnaya(ci, ri, ci_k=3, ri_k=2):
        (M, N) = ci.shape
        (i0, j0) = ri.shape

        k1 = np.zeros((M-i0, N-j0), dtype=np.float64)

        for di in range(0, M-i0, ci_k):
            for dj in range(0, N-j0,ci_k):
                for i in range(0, i0, ri_k):
                    for j in range(0, j0, ri_k):
                        k1[di, dj] += np.abs(ri[i, j] - ci[i+di, j+dj])
        k1 /= i0*j0/ri_k/ri_k
        
        return k1

@njit(fastmath=True)
def kor(ci, ri, ci_k=3, ri_k=2):
        ci_k = 2
        ri_k=2
        (M, N) = ci.shape
        (i0, j0) = ri.shape
        ci_m = ci.mean()
        ri_m = ri.mean()
        k1 = np.zeros((M-i0, N-j0), dtype=np.float64)

        for di in range(0, M-i0, ci_k):
            for dj in range(0, N-j0,ci_k):
                for i in range(0, i0, ri_k):
                    for j in range(0, j0, ri_k):
                        k1[di, dj] += (ri[i, j]-ri_m)*(ci[i+di, j+dj]-ci_m)
        k1 /= (i0*j0/ri_k/ri_k*np.sqrt(ri.var()*ci.var()))
        
        return k1


vid = cv.VideoCapture(0) 
#vid.set(cv.CAP_PROP_FRAME_WIDTH, 320)
#vid.set(cv.CAP_PROP_FRAME_HEIGHT, 240)

vid.set(cv.CAP_PROP_FRAME_WIDTH, 480)
vid.set(cv.CAP_PROP_FRAME_HEIGHT, 360)

first_tick = True

def main():
    global first_tick
    global ri
    global use_kor
    Kzvk = 1
    
    while(vid.isOpened()):
        ret, frame = vid.read()
        frame_grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        if first_tick:
            (height, width , chanels) = frame.shape
            #print(width, height)
            ri_width = 40*Kzvk
            ri_height = 40*Kzvk
            ri = frame_grey[int((height-ri_height)/2):int((height+ri_height)/2), int((width-ri_width)/2):int((width+ri_width)/2)]
            if cv.waitKey(1) & 0xFF == ord('r'):
                first_tick = False

        if cv.waitKey(3) & 0xFF == ord('o'):
                first_tick = True

        if cv.waitKey(3) & 0xFF == ord('a'):
                Kzvk +=0.2
                if(Kzvk == 2):
                    Kzvk = 1

        # Место выделения нового эталона
        #frame = cv.rectangle(frame,
        #                        (int((width+ri_width)/2), int((height+ri_height)/2)),
        #                        (int((width-ri_width)/2), int((height-ri_height)/2)),
        #                        (0,0,0),
        #                        1)
        # Приведение к типу для корректной работы
        frame_grey_ = frame_grey.astype(float)
        if (use_kor):
            # Вычисление корреляционной функции
            k = kor(frame_grey_, ri)
            minval, maxval, min_i, max_i = cv.minMaxLoc(k)
            #k = (k-minval)/(maxval-minval)
            
            #Потеря эталона
            if maxval < 0.45:
                frame = cv.putText(frame, "MISS".format(minval), (10, 60), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, 2)## 3  2     
            #else:
            # Прямоугольник найденного эталона
            frame = cv.rectangle(frame,
                                    max_i,
                                    (max_i[0]+ri_height, max_i[1]+ri_width),
                                    (0,50,127),
                                    2)
            # Направление от эталона к центру
            #frame = cv.arrowedLine(frame,
            #                    (int(max_i[0]+ri_height/2), int(max_i[1]+ri_width/2)),
            #                    (int((width+ri_width)/2), int((height+ri_height)/2)),
            #                    (50,50,50),
            #                    2)
            
            frame = cv.putText(frame, "K_max = {:.2f}".format(maxval), (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2, 1)
            cv.imshow("function", np.uint8(k*255.0))

            if cv.waitKey(3) & 0xFF == ord('k'):
                use_kor = False

        else:
            raz = kor(frame_grey_, ri)
            raz[raz == raz.min()] = raz.max()
            # raz = cv.matchTemplate(frame_grey, ri, cv.TM_SQDIFF)

            minval, maxval, min_i, max_i = cv.minMaxLoc(raz)
            if minval > 2:
                frame = cv.putText(frame, "MISS".format(minval), (10, 60), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, 2)     
            raz = (raz-minval)/(maxval-minval)

            # Прямоугольник найденного эталона
            frame = cv.rectangle(frame,
                                    min_i,
                                    (min_i[0]+ri_height, min_i[1]+ri_width),
                                    (0,50,127),
                                    2)
            # Направление от эталона к центру
            #frame = cv.arrowedLine(frame,
            #                    (min_i[0]+ri_height, min_i[1]+ri_width),
            #                    (int((width-ri_width)/2), min_i[1]+ri_width),
            #                    (50,50,50),
            #                    2)
            
            frame = cv.putText(frame, "K_min = {:.2f}".format(minval), (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2, 1)
            cv.imshow(" ", np.uint8(raz*255.0))

            if cv.waitKey(1) & 0xFF == ord('k'):
                use_kor = True
        
        # Вывод на экран
        frame[0:ri_height,width - ri_width:width,0] = ri 
        frame[0:ri_height,width - ri_width:width,1] = ri 
        frame[0:ri_height,width - ri_width:width,2] = ri 
        #print(frame.shape)
        cv.imshow('Video capture', frame)
        #cv.imshow("Kernel",ri)
        
        # Обработчик нажатия на клавишу
        res = cv.waitKey(1)
        if res & 0xFF == ord('q') or res == 27: 
            break
    
    vid.release()
    cv.destroyAllWindows() 

if __name__ == "__main__":
    main()
