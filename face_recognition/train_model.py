import base64
from tqdm import tqdm
from face_recognition import FaceRecognition
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_curve, precision_recall_curve, roc_auc_score, accuracy_score
import matplotlib.pyplot as plt
import os
import glob
import pandas as pd
import numpy as np
import cv2
import base64
from tqdm import tqdm
from pprint import pprint
import shutil

def train():
    #Settings
    ROOT_FOLDER ="./dataset/train/"
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
    
    
def validate():
    #Settings
    IMAGE_PATH ="./dataset/val/"
    MODEL_PATH = "model_v1.pkl"

    SAVE_PATH = "Result"
    if not os.path.exists(SAVE_PATH):
        os.mkdir(SAVE_PATH)
    else:    
        shutil.rmtree(SAVE_PATH)
        os.mkdir(SAVE_PATH)
    SAVE_PATH = os.path.join(os.getcwd(), SAVE_PATH)

    # Testing
    fr = FaceRecognition()
    fr.load(MODEL_PATH)

    file_names = [fn for fn in os.listdir(IMAGE_PATH) if any(fn.endswith(ext) for ext in ['jpg','jpeg', 'bmp', 'png', 'gif'])]

    for file in file_names:
        img =  cv2.imread(os.path.join(IMAGE_PATH,file))

        result = fr.predict(img, threshold=0.3)
        file_bytes = np.fromstring(base64.b64decode(result["frame"]), np.uint8)
        output = cv2.imdecode(file_bytes,1)

        plt.imshow(output)
        if len(result['predictions'])>0:
            plt.title("%s (%f)" % (result["predictions"][0]["person"], result["predictions"][0]["confidence"]))
        plt.tight_layout()
        plt.show(block=False)
        plt.pause(0.5)
        plt.savefig(os.path.join(SAVE_PATH,'Output_'+file))
        plt.close()
        pprint(result["predictions"])

    
def test():
    #Settings
    IMAGE_PATH ="./dataset/test/"
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
        result = fr.predict(img,threshold=0.5)
        for prediction in result["predictions"]:
            y_pred.append(prediction["person"])
            y_scores.append(prediction["confidence"])
            y_test.append(test_dataset.person.iloc[idx])

    # Show Summary
    print(classification_report(y_test, y_pred))

    # Accuracy
    print("Accuracy: %f" % accuracy_score(y_test, y_pred))