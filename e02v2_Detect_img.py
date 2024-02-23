from ultralytics import  YOLO
import yaml
import  cv2
model  = YOLO('model_v3.pt')
model.predict(r'https://previews.123rf.com/images/leungchopan/leungchopan1312/leungchopan131200967/24554544-warehouse-at-outdoor.jpg',save = True,show=True)    