import tkinter as tk
from tkinter import *
from tkinter import ttk

def select_combo(event):
    print(combobox.get())

def close_window():
    root.destroy()

root = tk.Tk()
root.geometry("300x150+550+300") # 位置

frame1 = ttk.Frame(root, padding=16) # root を親要素にして Frame を作成しています。 Frame は単純な矩形のウィジェットで、 他のコンポーネントを含むコンテナとして使います。
label1 = ttk.Label(frame1, text=f"名前を選択してください")

module = ('orui', 'kusumoto', 'saito', 'nomura')

v = tk.StringVar()

combobox = ttk.Combobox(root, textvariable= v, values=module)
combobox.bind('<<ComboboxSelected>>', select_combo)

button1 = ttk.Button(
    frame1,
    text='OK',
    command = close_window)


###結果をスプレッドシートに送る###
print('Hello, %s.' % v.get())

frame1.pack()
label1.pack(side=TOP) #左から右にウィジェットを追加
combobox.pack(pady=10)
button1.pack(side=BOTTOM) 

root.mainloop()