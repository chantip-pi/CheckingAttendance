#capture video to image
import cv2
import numpy as np
import os
import glob as gl
import matplotlib.pyplot as plt
import shutil

#get folder path that contains video, get folder name to save the extracted image
def video_to_image(video_folder,image_folder): 
    
    # delete dir if exist
    if os.path.exists(image_folder):
        shutil.rmtree(image_folder, ignore_errors=False, onerror=None)
    
    #make folder that save the extracted image
    os.mkdir(image_folder)
    
    #get video from video folder
    for filename in os.listdir(video_folder):
        
        #Opens the video.
        cap = cv2.VideoCapture(os.path.join(video_folder,filename)) 
        
        #count extracted image
        i = 1
        #set frequency of frame how frequent you want to extract
        target = 2

        counter = 0
        
        #make directory folder
        os.mkdir(os.path.join(image_folder,filename[:-4]))
        
        while(cap.isOpened()):
            #Extract image every 2 frame
            if counter==target: 
                
                ret, frame = cap.read()
                
                #Resize image to (576,720)
                dim = (576,720)
                frame=cv2.resize(frame,dim,fx=0,fy=0,interpolation = cv2.INTER_NEAREST)
                
                #Save image to image folder 
                cv2.imwrite(os.path.join(image_folder,filename[:-4],filename[:-4]+'_'+str(i)+'.jpg'),frame)
                
                counter = 0 
                i += 1
                
            else: 
                ret = cap.grab() 
                counter += 1
            #if reach the end of video, stop
            if ret == False: 
                break
            #if have 60 extracted image, stop
            if i == 61: 
                break
            
            
    cv2.destroyAllWindows()
video_to_image("videos","Train")