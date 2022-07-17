from tkinter import *
from tkinter import ttk

root = Tk()# Tk() の呼び出しでルート要素を作成します。このルート要素はベースとなるウィンドウそのものを表しています。
root.geometry("300x150+550+300") # 位置
root.title('確認') # ルートのウィンドウにタイトルを設定しています。

def close_window():
    root.destroy()
###　受け取る ###
date = "10"
hour = "10"

# ウィジェットの作成
frame1 = ttk.Frame(root, padding=16) # root を親要素にして Frame を作成しています。 Frame は単純な矩形のウィジェットで、 他のコンポーネントを含むコンテナとして使います。
label1 = ttk.Label(frame1, text=f"あなたは今月{date}日登校しました")
label2 = ttk.Label(frame1, text=f"あなたは今月{hour}時間滞在しました")
t = StringVar() # 入力した文字をセット

button1 = ttk.Button(
    frame1,
    text='OK',
    command = close_window)

# レイアウト
frame1.pack()
label1.pack(side=TOP) #左から右にウィジェットを追加
label2.pack(side=TOP) #左から右にウィジェットを追加
button1.pack(side=TOP) 


# ウィンドウの表示開始
root.mainloop()