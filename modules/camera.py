from face_recognition import FaceRecognition
from modules.sheet_generator import SheetGenerator
import numpy as np
import cv2
import base64

def open_camera(sheet: SheetGenerator):
    MODEL_PATH = "model_v1.pkl"
    fr = FaceRecognition()
    fr.load(MODEL_PATH)

    capture = cv2.VideoCapture(0)
    while True:    
        ret, frame = capture.read()
        result = fr.predict(frame, threshold=0.65)
        file_bytes = np.fromstring(base64.b64decode(result["frame"]), np.uint8)
        frame = cv2.imdecode(file_bytes,1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
        try:
            id = result["predictions"][0]["person"]
            if (id != 'UNKNOWN'):
                print(id)
                sheet.check(id)
        except:
            pass
        cv2.imshow("frame",frame)
        if cv2.waitKey(25) & 0xff == ord('q'): 
            break