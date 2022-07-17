from tkinter import *
from tkinter import ttk
import numpy as np

class Tell_Score():
    def __init__(self, record):
        super().__init__()

        self.record = record

    def close_window(self):
        self.root.destroy()

    def main(self):

        self.root = Tk()# Tk() の呼び出しでルート要素を作成します。このルート要素はベースとなるウィンドウそのものを表しています。
        self.root.geometry("300x150+550+300") # 位置
        self.root.title('確認') # ルートのウィンドウにタイトルを設定しています。

        # ウィジェットの作成
        frame1 = ttk.Frame(self.root, padding=16) # root を親要素にして Frame を作成しています。 Frame は単純な矩形のウィジェットで、 他のコンポーネントを含むコンテナとして使います。
        
        label1 = ttk.Label(frame1, text=f"あなたの履歴は{self.record}です・")
        
        # label2 = ttk.Label(frame1, text=f"あなたは今月{hour}時間滞在しました")
        t = StringVar() # 入力した文字をセット

        button1 = ttk.Button(
            frame1,
            text='OK',
            command = self.close_window)

        # レイアウト
        frame1.pack()
        label1.pack(side=TOP) #左から右にウィジェットを追加
        # label2.pack(side=TOP) #左から右にウィジェットを追加
        button1.pack(side=TOP) 


        # ウィンドウの表示開始
        self.root.mainloop()


if __name__ == '__main__':
    ###　受け取る ###
    name = np.zeros(4)   
    tell_score = Tell_Score(name)
    tell_score.main()