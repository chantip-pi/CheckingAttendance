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
IMAGE_PATH ="./Datasets/Test1/"
MODEL_PATH = "model_v1.pkl"

#Read Test dataset
test_dataset = []
for path in glob.iglob(os.path.join(IMAGE_PATH, "**", "*.jpg")):
    path = path.replace("\\","/")
    person = path.split("/")[-2]
    test_dataset.append({"person":person, "path": path})
    
test_dataset = pd.DataFrame(test_dataset)
test_dataset = test_dataset.groupby("person").filter(lambda x: len(x) > 10)
test_dataset.head(10)

# Testing
fr = FaceRecognition()
fr.load(MODEL_PATH)


y_test, y_pred, y_scores = [],[],[]
for idx in tqdm(range(len(test_dataset))):
    path = test_dataset.path.iloc[idx]
    img =  cv2.imread(path)
    result = fr.predict(img)
    for prediction in result["predictions"]:
        y_pred.append(prediction["person"])
        y_scores.append(prediction["confidence"])
        y_test.append(test_dataset.person.iloc[idx])

# Show Summary
print(classification_report(y_test, y_pred))

# Accuracy
print("Accuracy: %f" % accuracy_score(y_test, y_pred))