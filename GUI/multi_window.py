# sample.py
# tkinterのインポート
import tkinter as tk
import tkinter.ttk as ttk

def sub_window():
    sub_win = tk.Toplevel()
    sub_win.geometry("300x100")
    label_sub = tk.Label(sub_win, text="サブウィンドウ")
    label_sub.pack()

# rootメインウィンドウの設定
root = tk.Tk()
root.title("tkinter:Toplevel")
root.geometry("300x100")

# メインフレームの作成と設置
frame = tk.Frame(root)
frame.pack(fill = tk.BOTH, padx=5, pady=10)

# 各種ウィジェットの作成
button = ttk.Button(frame, text="サブウィンドウ生成", command=sub_window)

# 各種ウィジェットの設置
button.pack()

root.mainloop()