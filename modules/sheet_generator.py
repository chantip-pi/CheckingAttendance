from datetime import datetime
from typing import List, Dict
import os
import pandas as pd

class SheetGenerator:
    fileName: str
    df: pd.DataFrame
    destination: str
    attendanceList: List[Dict]
    
    def __init__(self, name: str, destination: str) -> None:
        self.destination = os.path.join(os.getcwd(), destination)
        os.makedirs(self.destination, exist_ok=True)
        self.fileName = name + "_" + self.__getTimeNow__()
        self.attendanceList = []
        
    def __getTimeNow__(self) -> str:
        dt = datetime.now()
        return dt.strftime("%d-%m-%Y_%H:%M:%S")
    

    def check(self, id: str) -> None:
        newStd = {
            'id': id,
            'timestamp': self.__getTimeNow__()
        }
        
        idList = [
            std['id'] for std in self.attendanceList
        ]

        if (id not in idList):
            self.attendanceList.append(newStd)
            print(f"ID:{id} has been added")
    
    def close(self) -> None:
        self.df = pd.DataFrame(self.attendanceList, columns=['id', 'timestamp'])
        self.df.to_csv(os.path.join(self.destination, f"{self.fileName}.csv".replace(':', '-')), index=False)
        print("File has been saved")
