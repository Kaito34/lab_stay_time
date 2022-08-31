import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import time
import sys
from DBtools import DataBaseConnection
from GUI.ask_name import Ask_Name 
from GUI.tell_score import Tell_Score
import collections
import matplotlib
matplotlib.use('tkagg')

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

# def mark_attendance(name):
#     with open('attend.csv', 'r+') as f:
#         my_data_list = f.readlines()
#         name_list = []
#         for line in my_data_list:
#             entry = line.split(',')
#             name_list.append(entry[0])
#         if name not in name_list:
#             now = datetime.now()
#             time = now.strftime('%H:%M:%S')
#             f.writelines(f'\n{name},{time}')
            
def main():
    timer = False # タイマーをセットしたか否か
    results = [] # 1フレームごとの認証結果を一定時間格納
    name = None # １フレームごとの認証結果
    rec_result = None # 最終的な認証結果
    waiting_time = 3

    path = 'data/raw'
    images = []
    classNames = []
    myList = os.listdir(path)
    database = DataBaseConnection('dev')
    ask_name = Ask_Name()

    for cls in myList:
        # if cls == ".DS_Store":
        #     continue

        # .DS_Storeとか.gitkeepとか余分なものが混ざっていることがあるので除く
        if os.path.splitext(cls)[1] != ".png":
            continue

        current_img = cv2.imread(f'{path}/{cls}')
        images.append(current_img)
        classNames.append(os.path.splitext(cls)[0])
    print(classNames)

    encode_list_known = find_encodings(images)
    print(len(encode_list_known))

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
                # print(name)

        ### 認識結果があるとき ###
        if name is not None:
            #### 初めて認識されたら、タイマーをセット ###
            if timer == False: 
                start_time = time.time()
                timer = True

            results.append(name)
            
        ### 3s経過したら、個人の判別 & タイマーのリセット ###
        if timer == True:
            now_time = time.time()
            if  now_time - start_time >= waiting_time:
                rec_result = collections.Counter(results)
                rec_result = rec_result.most_common(1)[0][0]

                # 結果、タイマーのリセット
                results.clear()
                timer = False
        
                print("rec_result", rec_result, type(rec_result))

        # ## 認識結果を利用者に確認する ###
        if type(rec_result) is str :
        # a = True
        # if a == True:
            confirmed_name = ask_name.main(rec_result)
            rec_result = None
    
        
        ### 判別結果をデータベースに送る ###
        # 先頭を大文字にする処理を以下に書く!
         
        # database.entrance_stamp(confirmed_name)
        
        ### 1フレームごとの認識結果をリセット ###
        name = None

        cv2.imshow('WebCam', img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()