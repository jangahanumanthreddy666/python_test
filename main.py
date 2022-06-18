from cv2 import add
import numpy as np
import cv2 as cv
import os

#Read the files from the directory
path = "workspace"
dir_list = os.listdir(path)
x=len(dir_list)

x=len(dir_list)

 

for i in range(x):
    path1='workspace/'
    x1=str(dir_list[i])
    x2=path1+x1
    
    cap = cv.VideoCapture(x2)        
    # Define the codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    
    p1='workspace_output/'
    p2=str(i)
    p3='output_'
    p4=p1+p3+p2
    out = cv.VideoWriter(p4, fourcc, 20.0, (300,  180))
    while cap.isOpened():
        ret, frame = cap.read()
        ret, img=cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        
        angle270 = 90
        scale = 1.0
        h = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        w = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        center = (w / 2, h/ 2)
        M = cv.getRotationMatrix2D(center, angle270, scale)
        
        img2 = cv.warpAffine(img, M, (w, h))
        gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
        frame = cv.flip(frame, -90)
        # write the flipped frame
        out.write(frame)
        gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
        # cv.imshow('frame', frame)
        # cv.imshow('rotated video',img2)
        cv.imshow("GrayColor", gray)
        if cv.waitKey(1) == ord('q'):
            break
        k=cv.waitKey(1) & 0xff
        #once you inter Esc capturing will stop
        if k==27:
            break
    # Release everything if job is finished
    cap.release()
    out.release()
    cv.destroyAllWindows()