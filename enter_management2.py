import cv2
import numpy as np
import face_recognition
import os

import tkinter as tk
from tkinter import *
from tkinter import ttk

def find_encodings(images):
    encode_list = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encode_list.append(encode)
    return encode_list
            

if __name__ == "__main__":
    name = None 

    path = 'data/raw'
    images = []
    classNames = []
    myList = os.listdir(path)

    for cls in myList:
        if os.path.splitext(cls)[1] != ".png":
            continue

        current_img = cv2.imread(f'{path}/{cls}')
        images.append(current_img)
        classNames.append(os.path.splitext(cls)[0])

    encode_list_known = find_encodings(images)

    cap = cv2.VideoCapture(1)
    while True:
        success, img = cap.read()
        img_resize = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        img_resize = cv2.cvtColor(img_resize, cv2.COLOR_BGR2RGB)

        face_frame = face_recognition.face_locations(img_resize)
        encode_frame = face_recognition.face_encodings(img_resize, face_frame)

        for encode_face, face_loc in zip(encode_frame, face_frame):
            matches = face_recognition.compare_faces(encode_list_known, encode_face)
            face_dis = face_recognition.face_distance(encode_list_known, encode_face)
            match_idx = np.argmin(face_dis)
        
            if matches[match_idx]:
                name = classNames[match_idx].upper()
                y1, x2, y2, x1 = face_loc
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2-35), (x2, y2), (0,255,0),cv2.FILLED)
                cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

        
        # if name is not None:

        #     root = tk.Tk()
        #     root.geometry("300x150+550+300") 
        #     root.title('confirmation') 

        #     frame1 = ttk.Frame(root, padding=16) 
        #     label1 = ttk.Label(frame1, text=f"Are you {name}?")

        #     frame1.pack()
        #     label1.pack(side=TOP) 

        #     root.mainloop()

        # else:
        #     print("aaa")
        #     continue
        #     root = tk.Tk()
        #     root.geometry("300x150+550+300") 
        #     root.title('confirmation') 

        #     frame1 = ttk.Frame(root, padding=16) 
        #     label1 = ttk.Label(frame1, text=f"Are you {name}?")

        #     frame1.pack()
        #     label1.pack(side=TOP) 

        #     root.mainloop()

        cv2.imshow('WebCam', img)
        cv2.waitKey(1)


