from datetime import datetime
from typing import List, Dict
import os
import pandas as pd

class SheetGenerator:
    fileName: str
    df: pd.DataFrame
    destination: str
    attendanceList: List[Dict]
    
    def __init__(self, name, destination) -> None:
        self.destination = os.path.join(os.getcwd(), destination)
        os.makedirs(self.destination, exist_ok=True)
        self.fileName = name + "_" + self.__getTimeNow__()
        self.attendanceList = []
        
    def __getTimeNow__(self) -> str:
        dt = datetime.now()
        df = pd.DataFrame()
        return dt.strftime("%d-%m-%Y_%H:%M:%S")
    

    def check(self, id, image) -> None:
        newStd = {
            'id': id,
            'image': image,
            'timestamp': self.__getTimeNow__()
        }
        
        idList = [
            std['id'] for std in self.attendanceList
        ]

        if (id not in idList):
            self.attendanceList.append(newStd)
            print(f"ID:{id} has been added")
    
    def close(self):
        self.df = pd.DataFrame(self.attendanceList)
        self.df.to_csv(os.path.join(self.destination, f"{self.fileName}.csv"), index=False)
        print("File has been saved")

