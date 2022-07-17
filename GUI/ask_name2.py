import tkinter as tk
from tkinter import *
from tkinter import ttk


root = Tk()# Tk() の呼び出しでルート要素を作成します。このルート要素はベースとなるウィンドウそのものを表しています。
root.geometry("300x150+550+300") # 位置
root.title('確認') # ルートのウィンドウにタイトルを設定しています。

# def select_combo(event):
#     print(combobox.get())

def close_window():
    root.destroy()

def sub_window():
    sub_win = tk.Toplevel()
    sub_win.geometry("300x150+550+300")
    label_sub = tk.Label(sub_win, text="サブウィンドウ")
    label_sub.pack()

def sub_window():
    root2 = tk.Toplevel() # Tk() の呼び出しでルート要素を作成します。このルート要素はベースとなるウィンドウそのものを表しています。
    root2.geometry("300x150+550+300") # 位置
    root2.title('名前を入力') # ルートのウィンドウにタイトルを設定しています。

    root2.grab_set()
    frame2 = ttk.Frame(root2, padding=16) # root2 を親要素にして Frame を作成しています。 Frame は単純な矩形のウィジェットで、 他のコンポーネントを含むコンテナとして使います。
    label2 = ttk.Label(frame2, text=f"名前を選択してください")

    module = ('orui', 'kusumoto', 'saito', 'nomura')
    v = tk.StringVar()
    combobox = ttk.Combobox(root2, textvariable= v, values=module)
    # combobox.bind('<<ComboboxSelected>>', select_combo(combobox))
    combobox.bind('<<ComboboxSelected>>')

    button3 = ttk.Button(
        frame2,
        text='OK',
        command = close_window)

    ###結果をスプレッドシートに送る###
    print(v.get())

    frame2.pack()
    label2.pack(side=TOP) #左から右にウィジェットを追加
    combobox.pack(pady=10)
    button3.pack(side=BOTTOM) 

    

###　受け取る ###
name = "orui"

# ウィジェットの作成
frame1 = ttk.Frame(root, padding=16) # root を親要素にして Frame を作成しています。 Frame は単純な矩形のウィジェットで、 他のコンポーネントを含むコンテナとして使います。
label1 = ttk.Label(frame1, text=f"{name}さんですか?")
t = StringVar() # 入力した文字をセット

button1 = ttk.Button(
    frame1,
    text='OK',
    command = close_window)

button2 = ttk.Button(
    frame1,
    text='No',
    command=sub_window)
# レイアウト
frame1.pack()
label1.pack(side=TOP) #左から右にウィジェットを追加
button1.pack(side=TOP) 
button2.pack(side=TOP) 


# ウィンドウの表示開始
root.mainloop()



