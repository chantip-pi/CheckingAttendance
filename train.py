from face_recognition import FaceRecognition
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_curve, precision_recall_curve, roc_auc_score, accuracy_score
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
from pprint import pprint

#Settings
ROOT_FOLDER ="./Dataset/Train/"
MODEL_PATH = "model_v1.pkl"

#Read Train dataset
train_dataset = []
for path in glob.iglob(os.path.join(ROOT_FOLDER, "**", "*.jpg")):
    path = path.replace("\\","/")
    person = path.split("/")[-2]
    train_dataset.append({"person":person, "path": path})
    

train_dataset = pd.DataFrame(train_dataset)
train_dataset = train_dataset.groupby("person").filter(lambda x: len(x) > 10)
train_dataset.head(10)

# Training
fr = FaceRecognition()
fr.fit_from_dataframe(train_dataset)
fr.save(MODEL_PATH)

