import tkinter as tk

def get_player():
    player = [['one',1],['two',2],['three',3],['four',4],['five',5],['six',6]]
    return player

class RecordBoard(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.geometry('500x300')
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):

        def do_print():
            print('%s' %(dateString.get()))
            print('%s' %(gameString.get()))
            print('%s' %(oppschoolString.get()))
            print('%s' %(oppdepString.get()))

        tk.Frame.__init__(self, master)
        tk.Label(self, text="開始記錄", font=('Arial', 18, "bold")).grid(column=0, row=0, sticky=tk.W)
        #Label-文字標籤
        dateLabel = tk.Label(self, text='日期:')
        gameLabel = tk.Label(self, text='盃賽名稱:')
        oppschoolLabel = tk.Label(self, text='對手學校')
        oppdepLabel = tk.Label(self, text='對手系名')

        dateLabel.grid(column=0, row=1, sticky=tk.W)
        gameLabel.grid(column=0, row=2, sticky=tk.W)
        oppschoolLabel.grid(column=0, row=3, sticky=tk.W)
        oppdepLabel.grid(column=0, row=4, sticky=tk.W)
        #定義文字輸入框裡的文字物件
        dateString = tk.StringVar()
        gameString = tk.StringVar()
        oppschoolString = tk.StringVar()
        oppdepString = tk.StringVar()
        dateEntry = tk.Entry(self, show=None, font=('Arial', 14), textvariable=dateString)
        gameEntry = tk.Entry(self, show=None, font=('Arial', 14), textvariable=gameString)
        oppschoolEntry = tk.Entry(self, show=None, font=('Arial', 14), textvariable=oppschoolString)
        oppdepEntry = tk.Entry(self, show=None, font=('Arial', 14), textvariable=oppdepString)

        dateEntry.grid(column=1, row=1, padx=10)
        gameEntry.grid(column=1, row=2, padx=10)
        oppschoolEntry.grid(column=1, row=3, padx=10)
        oppdepEntry.grid(column=1, row=4, padx=10)

        tk.Button(self, text='確定', command=lambda: [master.switch_frame(Page_ChoosePlayer), do_print()]).grid(column=0, row=5, sticky=tk.W)

class Page_ChoosePlayer(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='red')
        tk.Label(self, text="選擇5個上場球員", font=('Arial', 18, "bold")).pack(side="top", fill="x", pady=5)
        player = get_player()
        tk.Button(self, text="Go back to start page", command=lambda: master.switch_frame(StartPage)).pack()

if __name__ == "__main__":
    window = RecordBoard()
    window.mainloop()