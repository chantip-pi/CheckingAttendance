#capture video to image
import cv2
import numpy as np
import os
import shutil

#get folder path that contains video, get folder name to save the extracted image
def video_to_image(video_folder,image_folder): 
    """
    Image:
        sample01:
            sample01_1.jpg
            sample01_2.jpg
            ...
        sample02:
            sample01_1.jpg
            sample01_2.jpg
            ...
    """
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

        #make directory folder
        os.mkdir(os.path.join(image_folder,filename[:-4]))
        
        while(cap.isOpened()):
        
            ret, frame = cap.read()
                
            #Resize image to (576,720)
            dim = (576,720)
            frame=cv2.resize(frame,dim,fx=0,fy=0,interpolation = cv2.INTER_NEAREST)
                
            #Save image to image folder 
            cv2.imwrite(os.path.join(image_folder,filename[:-4],filename[:-4]+'_'+str(i)+'.jpg'),frame)
                
            
            i += 1
                
            #if reach the end of video, stop
            if ret == False: 
                break
            #if have 150 extracted image, stop
            if i == 151: 
                break
            
            
    cv2.destroyAllWindows()

#Create a folder with shuffled data and splitting to train data and test data
def make_shuffle_dataset(foldername):
    """
    Dataset:
        Train:
            sample01:
                sample01_5.jpg
                sample01_17.jpg
                ...
            sample02:
                sample01_11.jpg
                sample01_22.jpg
                ...
        Test:
            sample01:
                sample01_15.jpg
                sample01_27.jpg
                ...
            sample02:
                sample01_18.jpg
                sample01_32.jpg
                ...
        Val:
            sample01:
                sample01_51.jpg
                sample01_54.jpg
                ...
            sample02:
                sample01_10.jpg
                sample01_42.jpg
                ...
    """
     # delete dir if exist
    if os.path.exists("dataset"):
        shutil.rmtree("dataset", ignore_errors=False, onerror=None)
    
    #make new dataset folder that contain all the data
    os.mkdir("dataset")
    os.mkdir(os.path.join("dataset", "train"))
    os.mkdir(os.path.join("dataset", "test"))
    os.mkdir(os.path.join("dataset", "val"))

    #make new label folder in Train,Test,Val folder of dataset   
    for label in os.listdir(foldername):
        os.mkdir(os.path.join("dataset", "train", label))
    for label in os.listdir(foldername):
        os.mkdir(os.path.join("dataset", "test", label))
    for label in os.listdir(foldername):
        os.mkdir(os.path.join("dataset", "val", label))

    #Go through each label folder
    for label in os.listdir(foldername):
        #contain paths of shuffled data
        train_path = []
        test_path = []
        val_path = []

        #contain path of file in label folder
        paths = []
        
        #Go through file in label folder
        for file in os.listdir( os.path.join(foldername,label) ):
            paths.append( (os.path.join(foldername,label,file) ))
                
        np.random.shuffle(paths)
        
        #split the shuffle path into 3 section, each one contain 0.33 percent of the path 
        shuffle_split = np.array_split(paths, 6)
        
        #combine 2 section of the split data to train and 1 section to test 
        #add path to train and test
        #resulting a split of train = 0.50 test = 0.33 val = 0.17
        for i in range(0,3):
            for j in shuffle_split[i]:
                train_path.append(j)

        for i in range(3,5):
            for j in shuffle_split[i]:
                val_path.append(j)
            
        for j in shuffle_split[5]:
            test_path.append(j)

    #copy image file to new dataset folder by train_path, test_path,val_path to folder Train ,Test and Val
        for image in train_path: 
            src = image
            dst = os.path.join("dataset", "train", label,os.path.basename(image))
            shutil.copyfile(src, dst)
   
        for image in test_path: 
            src = image
            dst = os.path.join("dataset", "test", label,os.path.basename(image))
            shutil.copyfile(src, dst)

        for image in val_path: 
            src = image
            dst = os.path.join("dataset", "val", label,os.path.basename(image))
            shutil.copyfile(src, dst)
        
    if os.path.exists('images'):
        shutil.rmtree('images', ignore_errors=False, onerror=None)
