import tkinter as tk
from tkinter import *
from tkinter import ttk


root = Tk()# Tk() の呼び出しでルート要素を作成します。このルート要素はベースとなるウィンドウそのものを表しています。
root.geometry("300x150+550+300") # 位置
root.title('確認') # ルートのウィンドウにタイトルを設定しています。

# def select_combo(event):
#     print(combobox.get())

class Ask_Name():
    def __init__(self, name):
        super().__init__()
        self.name = name        
        self.flag = True

    def close_window(self):
        root.destroy()

    def sub_window(self):
        sub_win = tk.Toplevel()
        sub_win.geometry("300x150+550+300")
        label_sub = tk.Label(sub_win, text="サブウィンドウ")
        label_sub.pack()

    def sub_window(self):
        root2 = tk.Toplevel() # Tk() の呼び出しでルート要素を作成します。このルート要素はベースとなるウィンドウそのものを表しています。
        root2.geometry("300x150+550+300") # 位置
        root2.title('名前を入力') # ルートのウィンドウにタイトルを設定しています。

        root2.grab_set()
        frame2 = ttk.Frame(root2, padding=16) # root2 を親要素にして Frame を作成しています。 Frame は単純な矩形のウィジェットで、 他のコンポーネントを含むコンテナとして使います。
        label2 = ttk.Label(frame2, text=f"名前を選択してください")

        module = ('orui', 'kusumoto', 'saito', 'nomura')
        self.v = tk.StringVar()
        combobox = ttk.Combobox(root2, textvariable= self.v, values=module)
        # combobox.bind('<<ComboboxSelected>>', select_combo(combobox))
        combobox.bind('<<ComboboxSelected>>')

        button3 = ttk.Button(
            frame2,
            text='OK',
            command = self.close_window)


        frame2.pack()
        label2.pack(side=TOP) #左から右にウィジェットを追加
        combobox.pack(pady=10)
        button3.pack(side=BOTTOM) 

        self.flag = False

    def main(self):
        

        # ウィジェットの作成
        frame1 = ttk.Frame(root, padding=16) # root を親要素にして Frame を作成しています。 Frame は単純な矩形のウィジェットで、 他のコンポーネントを含むコンテナとして使います。
        label1 = ttk.Label(frame1, text=f"{self.name}さんですか?")
        t = StringVar() # 入力した文字をセット

        button1 = ttk.Button(
            frame1,
            text='OK',
            command = self.close_window)

        button2 = ttk.Button(
            frame1,
            text='No',
            command=self.sub_window)
        # レイアウト
        frame1.pack()
        label1.pack(side=TOP) #左から右にウィジェットを追加
        button1.pack(side=TOP) 
        button2.pack(side=TOP) 


        # ウィンドウの表示開始
        root.mainloop()

        ###結果をスプレッドシートに送る###

        if self.flag == True:
            return self.name     

        else:
            return self.v.get() 


if __name__ == '__main__':
    ###　受け取る ###
    name = "orui"   
    ask_name = Ask_Name(name)
    return_name = ask_name.main()
    print (return_name)

