"""
Partly inspired by and some code borrowed from Intel's project on the matter


"""

import os
import cv2
import numpy as np
import time
import playsound
from datetime import datetime

sdThresh=10
font=cv2.FONT_HERSHEY_SIMPLEX
initialized=False
SavePath=
maxFolderSize=300

def get_size(start_path = '.'):
    """Returns the folder size of start_path in gb"""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)

    total_size=total_size/(1e+9)
    return total_size

def getFileList(path):
    """Returns a list of files in the given path, sorted from oldest to newest"""
    List=[]
    for file in os.listdir(path):
        List.append(file)
    return List

def size_check(start_path="-", max_folder_size=300):
    """Checks whether or not the folder is larger than 300 gb, if True then
    it will delete the oldest file"""
    checkvalue=get_size(start_path)
    if checkvalue>max_folder_size:
        print("Folder cluttered, deleting old file")
        List=getFlieList(start_path)
        os.remove(str(start_path)+List[-1])
    else:
        print("Folder has", str(int(max_folder_size-checkvalue))+" gb left.")

def getDistanceBetweenFrames(frame1, frame2):
    """Pythagorean distance between two frames"""
    frame1_32 = np.float32(frame1)
    frame2_32 = np.float32(frame2)

    diff = frame1_32 - frame2_32

    norm32 = np.sqrt(diff[:,:,0]**2 + diff[:,:,1]**2 + diff[:,:,2]**2)/np.sqrt(255**2 + 255**2 + 255**2)

    dist = np.uint8(norm32*255)
    return dist


cv2.namedWindow('Raw')
cv2.namedWindow('Distance')

#capture video. 0 refers to first camera (typically built-in webcam). 1 referes to second camera, etc.

capture = cv2.Videocaptureture(0, cv2.capture_DSHOW)
frame_height=int(capture.get(4))
frame_width=int(capture.get(3))
_, frame1 = capture.read()
_, frame2 = capture.read()

framelist=[]
while (True):
    if initialized==False:
        stDate=str(datetime.today())
        stDate=stDate.split(".")[0]
        stDate=stDate.replace(":", ",")
        out=cv2.VideoWriter(str(SavePath)+stDate+".avi", cv2.VideoWriter_fourcc(*"DIVX"), 30, (frame_width,frame_height))
        initialized=True
    _, frame3 = capture.read()

    rows, cols, _ = np.shape(frame3)
    dist=getDistanceBetweenFrames(frame1, frame3)
    frame1 = frame2
    frame2 = frame3
    mod=cv2.GaussianBlur(dist, (9,9), 0)
    _, thresh = cv2.threshold(mod, 100, 255, 0)
    _, stDev = cv2.meanStdDev(mod)
    cv2.imshow('dist', mod)
    cv2.putText(frame2, "Standard Deviation - {}".format(round(stDev[0][0],0)), (70, 70), font, 1, (255, 0, 255), 1, cv2.LINE_AA)
    cv2.putText(frame2, "Date / Time - {}".format(str(datetime.today())), (30, 30), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
    if stDev > sdThresh:
        print("writing frames")
        framelist.append(frame1)
        framelist.append(frame2)
    if len(framelist)>1000:
        #Serves to save the video in sizable bites to the save path
        print("finishing up")
        size_check(SavePath, maxFolderSize)
        for f in framelist:
            out.write(f)
        framelist=[]
        initialized=False

    cv2.imshow("frame", frame2)
    if cv2.waitKey(1) & 0xFF == 27:
        for f in framelist:
            out.write(f)
        break



print("len", len(framelist))
capture.release()
cv2.destroyAllWindows()
out.release()
