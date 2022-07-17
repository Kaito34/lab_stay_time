import numpy as np
import cv2
import random

random.seed(0)

# 画像を読み込む。
img = cv2.imread("data_1/kusumoto.jpg")
num = 10

human_name = ["kusumoto", "orui", "saitou", "nomura"]

for n in range (len(human_name)):
    data_index = 1

    while True:
        # 画像を読み込む。
        img = cv2.imread(f"data/{human_name[n]}_{data_index}.jpg")
        if(type(img) is not np.ndarray):
            break
        list = np.loadtxt(f"data/{human_name[n]}_{data_index}.txt")

        for i in range(num):
            ratio = random.uniform(0.1, 1.0)
            img1 = cv2.resize(img, dsize=None, fx=ratio, fy=ratio)

            # print(f"{img.shape} -> {img1.shape}")

            cv2.imwrite(f"processed_data/{human_name[n]}_{data_index}_size_{i}.jpg", img1)
            np.savetxt(f"processed_data/{human_name[n]}_{data_index}_size_{i}.txt", [list], fmt=["%.0f", "%.6f", "%.6f", "%.6f", "%.6f"])

        data_index += 1
# ### ボックスの変化 ###
# # 比率を表しているから、変えなくていいはず
# #読み込む
# list = np.loadtxt("data_1/kusumoto.txt")
# #コピーして名前変える
# for i in range(num):
#     np.savetxt(f"data_1/kusumoto_si_{i}.txt", [list], fmt=["%.0f", "%.6f", "%.6f", "%.6f", "%.6f"])
