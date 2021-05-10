import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import datetime


def edge_detection(image_path):
    image = cv2.imdecode(image_path, cv2.IMREAD_UNCHANGED)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 200, 100)
    
    
    
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(APP_ROOT, 'images/')
    random_generate1 = str(datetime.datetime.now()).replace(':', '') + '_1.png'
    random_generate2 = str(datetime.datetime.now()).replace(':', '') + '_2.png'
    random_generate3 = str(datetime.datetime.now()).replace(':', '') + '_3.png'
    
    im_path1 = target + random_generate1
    im_path2 = target + random_generate2
    im_path3 = target + random_generate3
    
    cv2.imwrite(im_path1, image)
    cv2.imwrite(im_path2, gray)
    cv2.imwrite(im_path3, edges)
    
    return random_generate1, random_generate2, random_generate3