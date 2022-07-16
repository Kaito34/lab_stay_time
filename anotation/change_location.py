'''
画像 (1080*720) とtxtファイル (ラベル、位置) が読み込まれる
→位置を変える
→ラベルの位置を変える
→保存
'''
import numpy as np
import cv2
import random

random.seed(0)
ratio = 0.9
num = 10 #一枚あたり何枚

human_name = ["kusumoto", "orui", "saitou", "nomura"]

for n in range (len(human_name)):
    data_index = 1
    
    while True:
        # 画像読み込み
        file_name = f"data/{human_name[n]}_{data_index}.jpg"
        img = cv2.imread(file_name)
        # print(type(img))
        if(type(img) is not np.ndarray):
            break
        # print(data_index)
        # 画像の情報
        height = img.shape[0]
        width = img.shape[1]
        cr_height = int(height * ratio)
        cr_width = int(width * ratio)
        sp_height = height - cr_height
        sp_width = width - cr_width

        # ラベルの情報
        #読み込む オブジェクトの中心X座標 オブジェクトの中心Y座標 オブジェクトの幅 オブジェクトの高さ
        txt_list = np.loadtxt(f"data/{human_name[n]}_{data_index}.txt")

        # print(txt_list)
        center_x = width * txt_list[1]
        center_y = height * txt_list[2]
        ob_width = width * txt_list[3]
        ob_height = height * txt_list[4]

        
        for i in range(num):
            start_height = random.randrange(0, sp_height)
            start_width = random.randrange(0, sp_width)
            
            img1 = img[start_height : start_height + cr_height, start_width : start_width + cr_width]
            cv2.imwrite(f"processed_data/{human_name[n]}_{data_index}_loc_{i}.jpg", img1)

            # 中心座標を出す→割合を出す
            center_x1 = center_x - start_width
            center_y1 = center_y - start_height
            center_x1_ratio = round(center_x1 / cr_width, 6)
            center_y1_ratio = round(center_y1 / cr_height, 6)

            txt_list[1] = center_x1_ratio
            txt_list[2] = center_y1_ratio
            # print(txt_list.shape)
            np.savetxt(f"processed_data/{human_name[n]}_{data_index}_loc_{i}.txt", [txt_list], fmt=["%.0f", "%.6f", "%.6f", "%.6f", "%.6f"])
        
        data_index += 1
    
