# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 21:32:53 2023

@author: ngocanh
"""

from ultralytics import  YOLO
import  cv2

model  = YOLO('./best.pt')
results = model.predict(r'D:/DNU/NghienCuuKhoaHoc/Code/data/fire5.mp4',stream=True,save = True, save_txt = True)
# model.predict()
# print(results[0].tojson())
for r in results:
    print(r.boxes)