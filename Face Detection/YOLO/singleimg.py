import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt
import tensorflow as tf
option = {
    'model':'cfg/tiny-yolo-voc.cfg',
    'load':'bin/tiny-yolo-voc.weights',
    'threshold': 0.3,
    'gpu': 1.0
}
config = tf.ConfigProto()
#config.gpu_options.allow_growth = True
config.gpu_options.per_process_gpu_memory_fraction = 0.8
session = tf.Session(config=config)

tfnet = TFNet(option)

img = cv2.imread('neel.jpg')
img = cv2.resize(img,(0,0),fx=0.3,fy=0.3)
#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow('img',gray)
result = tfnet.return_predict(img)
print(result)
#tl = (result[0]['topleft']['x'],result[0]['topleft']['y'])
#br = (result[0]['bottomright']['x'],result[0]['bottomright']['y'])

for x in result :
    tl = (x['topleft']['x'],x['topleft']['y'])
    br=  (x['bottomright']['x'],x['bottomright']['y'])
    label = x['label']
    img = cv2.rectangle(img,tl,br,(0,255,0),7)
    img = cv2.putText(img,label,tl,cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)
    
#img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow('Result',img)
