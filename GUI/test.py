from tkinter import *
from tkinter import ttk

root = Tk()# Tk() の呼び出しでルート要素を作成します。このルート要素はベースとなるウィンドウそのものを表しています。
root.title('My First App') # ルートのウィンドウにタイトルを設定しています。

# ウィジェットの作成
frame1 = ttk.Frame(root, padding=16) # root を親要素にして Frame を作成しています。 Frame は単純な矩形のウィジェットで、 他のコンポーネントを含むコンテナとして使います。
label1 = ttk.Label(frame1, text='Your name')
t = StringVar() # 入力した文字をセット
entry1 = ttk.Entry(frame1, textvariable=t) # エントリーウィジェットを作成
button1 = ttk.Button(
    frame1,
    text='OK',
    command=lambda: print('Hello, %s.' % t.get()))

# レイアウト
frame1.pack()
label1.pack(side=LEFT) #左から右にウィジェットを追加
entry1.pack(side=LEFT)
button1.pack(side=LEFT)

# ウィンドウの表示開始
root.mainloop()