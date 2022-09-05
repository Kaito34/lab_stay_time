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

def ask_name_terminal (rec_result, confirmed_name, e_flag):
    if type(rec_result) is str :
        print(f"Are you {rec_result}?")
        while True:
            val = input("press y if ok / n if not / q if you quit: ")
            # 認識結果があっている
            if val == "y":
                # 名前の確定
                confirmed_name = rec_result
                while True: 
                    # 入室か退室かを聞く    
                    val1 = input("press e if you enter lab / x if you exit lab / q if you quit: ")
                    # やめる
                    if val1 == "q":
                        confirmed_name = None # 名前の確定を取り消す
                        break
                    # 入室
                    elif val1 == "e":
                        e_flag = True
                        print("The access results were processed successfully")
                        break
                    # 退室
                    elif val1 == "x":
                        e_flag = False
                        print("The access results were processed successfully")
                        break                        
                    # 入力が正常にされてない
                    else:
                        print("press y or n")
                break                
            # 認識結果が違っている
            elif val == "n": 
                while True: 
                    val2 = input("type your name / q if you quit ex) orui, julia \n :")
                    # やめる
                    if val2 == "q":
                        break
                    # 入力された名前がない
                    elif val2 not in ['orui','kusumoto','wu','nishimura','hiramatsu','ishii','saito','chonabayashi','igarashi','ishizuka','imano','nomura','fujii','julia', 'macarena', 'valentin']:
                        print ("type your name correctly")                        
                    else:
                        # 名前の確定
                        confirmed_name = val2
                        while True:
                            # 入室か退室かを聞く
                            val3 = input("press e if you enter lab / x if you exit lab / q if you quit: ")
                            # やめる
                            if val3 == "q":
                                confirmed_name = None # 名前の確定を取り消す
                                break
                            # 入室
                            elif val3 == "e":
                                e_flag = True
                                print("The access results were processed successfully")
                                break
                            # 退室
                            elif val3 == "x":
                                e_flag = False
                                print("The access results were processed successfully")
                                break                                
                            # 入力が正常にされてない
                            else:
                                print("press e or x")
                        break
                break 
            # やめる
            elif val == "q": 
                break   
            # 入力が正常にされてない
            else:
                print("press y or n or q")

    return confirmed_name, e_flag                

def main():
    timer = False # タイマーをセットしたか否か
    results = [] # 1フレームごとの認証結果を一定時間格納
    name = None # １フレームごとの認証結果
    rec_result = None # 最終的な認証結果
    confirmed_name = None # 利用者により確定された結果
    e_flag = True # True → 入室 / False → 退室
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
        # if os.path.splitext(cls)[1] != ".png":
        #     continue
        if os.path.splitext(cls)[1] not in [".png", ".jpg"]:
            continue

        current_img = cv2.imread(f'{path}/{cls}')
        images.append(current_img)
        classNames.append(os.path.splitext(cls)[0])
    print(classNames)

    encode_list_known = find_encodings(images)
    print(len(encode_list_known))

    cap = cv2.VideoCapture(1)
    count = 0 # ループのカウンタ
    while True: # 大体34ループ回る
        count += 1

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

        ### 認識結果があるときだけリストに追加 ###
        if name is not None:
            #### 初めて認識されたら、タイマーをセット ###
            if timer == False: 
                start_time = time.time()
                timer = True

            results.append(name)
        
        ### 3s経過したら、個人の判別 & タイマーのリセット ###
        if timer == True:
            # 現時刻を毎回測り、waiting time経過しているかどうかを判別
            now_time = time.time() 

            # waiting time経過後
            if  now_time - start_time >= waiting_time: 

                # 2回ループのうち1回以上は認識できている時だけ結果を出す
                if len(results) >= count//2: 
                    rec_result = collections.Counter(results)
                    rec_result = rec_result.most_common(1)[0][0]

                # 結果、タイマー、ループのカウンタのリセット
                results.clear()
                timer = False
                count = 0
        
                # print("rec_result", rec_result, type(rec_result))

        # ### 認識結果を利用者に確認する (tkinter) ###
        # if rec_result is not None:
            # ask_name.main(rec_result)
        #     root = tk.Tk()
        #     root.geometry("300x150+550+300") 
        #     root.title('confirmation') 

        #     frame1 = ttk.Frame(root, padding=16) 
        #     label1 = ttk.Label(frame1, text=f"Are you {name}?")

        #     frame1.pack()
        #     label1.pack(side=TOP) 

        #     root.mainloop()

        #     # confirmed_name = ask_name.main(rec_result)
        #     rec_result = None
        
        # ### なぜかこれを書かないとエラーが出る ###
        # else:
        #     continue
        #     root = tk.Tk()
        #     root.geometry("300x150+550+300") 
        #     root.title('confirmation') 

        #     frame1 = ttk.Frame(root, padding=16) 
        #     label1 = ttk.Label(frame1, text=f"Are you {name}?")

        #     frame1.pack()
        #     label1.pack(side=TOP) 

        #     root.mainloop()

        #     # confirmed_name = ask_name.main(rec_result)
        #     rec_result = None
            


        ### 認識結果を利用者に確認する (ターミナル) ###
        if type(rec_result) is str :
            confirmed_name, e_flag = ask_name_terminal (rec_result, confirmed_name, e_flag)            
            rec_result = None
                    
        # print("confirmed_name", confirmed_name)
        # print("e_flag", e_flag)
        # print("end")
        # print("rec_result", rec_result)
        # print("timer", timer)


            
        
        
        ### 判別結果をデータベースに送る ###
        if confirmed_name is not None: 
            # 先頭を大文字にする!
            confirmed_name = confirmed_name.capitalize()
            if e_flag == True:
                print("entrance: name", confirmed_name)

                # database.entrance_stamp(confirmed_name)
            else:
                pass
                print("exit: name", confirmed_name)
                # database.exit_stamp(confirmed_name)

            confirmed_name = None

            # 連続して認識しないようにするため
            # time.sleep (3)
        
        ### 1フレームごとの認識結果をリセット ###
        name = None

        cv2.imshow('WebCam', img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()