from face_recognition import FaceRecognition
import matplotlib.pyplot as plt
import os
import glob
import pandas as pd
import random
import numpy as np
import cv2
import base64
from tqdm import tqdm
import requests
import shutil

MODEL_PATH = "model_v1.pkl"
fr = FaceRecognition()
fr.load(MODEL_PATH)

capture = cv2.VideoCapture(0)
while True:    
    ret, frame = capture.read()
    result = fr.predict(frame, threshold=0.5)
    file_bytes = np.fromstring(base64.b64decode(result["frame"]), np.uint8)
    frame = cv2.imdecode(file_bytes,1)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
    cv2.imshow("frame",frame)
    if cv2.waitKey(25) & 0xff == ord('q'): 
        break