import numpy as np
import cv2
import random

random.seed(0)


def adjust(img, alpha=1.0, beta=0.0):
    # 積和演算を行う。
    dst = alpha * img + beta
    # [0, 255] でクリップし、uint8 型にする。
    return np.clip(dst, 0, 255).astype(np.uint8)

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
            # alphaの値を決める
            alpha = random.uniform(0.2, 2.0)
            # print(alpha)

            # 明るさを変更する。
            img1 = adjust(img, alpha)

            cv2.imwrite(f"processed_data/{human_name[n]}_{data_index}_bl_{i}.jpg", img1)
            np.savetxt(f"processed_data/{human_name[n]}_{data_index}_bl_{i}.txt", [list], fmt=["%.0f", "%.6f", "%.6f", "%.6f", "%.6f"])

        data_index += 1
# ### ボックスの変化 ###
# #読み込む
# list = np.loadtxt("data_1/kusumoto.txt")
# #コピーして名前変える
# for i in range(num):
#     np.savetxt(f"data_1/kusumoto_bl_{i}.txt", [list], fmt=["%.0f", "%.6f", "%.6f", "%.6f", "%.6f"])

    
