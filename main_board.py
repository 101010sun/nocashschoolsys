import tkinter as tk

counter = 0

class RecordBoard(tk.Tk):
    def switch_frame(object_frame, frame_class):
        new_frame = frame_class(object_frame)
        if object_frame is not None:
            object_frame.destroy()
        object_frame = new_frame
        object_frame.pack()

    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x300')
        menu_frame = tk.Frame(self)
        menu_frame.pack(side=tk.TOP)
        object_frame = tk.Frame(self)
        object_frame.pack()

        l = tk.Label(object_frame, text='    ', bg='blue')
        l.pack()

        def do_job():
            global counter
            l.config(text='do '+str(counter))
            counter += 1

        menubar = tk.Menu(menu_frame) #宣告一個Menu的frame
        funcmenu = tk.Menu(menubar, tearoff=0) 
        menubar.add_cascade(label='模式', menu=funcmenu)
        setmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='設定', menu=setmenu)
        querymenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='查詢', menu=querymenu)
        rankmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='排行', menu=rankmenu)

        querymenu.add_command(label='球員數據', command=lambda: switch_frame(Page_PlayerData))
        querymenu.add_command(label='球隊數據', command=do_job)
        querymenu.add_separator() #分隔線
        querymenu.add_command(label='歷屆紀錄表', command=do_job)

        rankmenu.add_command(label='得分', command=do_job)
        rankmenu.add_command(label='籃板', command=do_job)
        rankmenu.add_command(label='助攻', command=do_job)
        rankmenu.add_command(label='阻攻', command=do_job)
        rankmenu.add_command(label='抄截', command=do_job)
        rankmenu.add_separator() #分隔線
        rankmenu.add_command(label='三分球%', command=do_job)
        rankmenu.add_command(label='投籃%', command=do_job)
        rankmenu.add_command(label='罰球%', command=do_job)

        setmenu.add_command(label='新增球員', command=do_job)
        setmenu.add_command(label='修改球員資料', command=do_job)

        funcmenu.add_command(label='記分板版', command=do_job)

        self.config(menu=menubar)
    
class Page_PlayerData(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="球員數據頁面", font=('Arial', 18, "bold")).pack(side="top", fill="x", pady=5)
        

if __name__ == "__main__":
    window = RecordBoard()
    window.mainloop()
