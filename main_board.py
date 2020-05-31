import tkinter as tk

class RecordBoard(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x300')
        menu_frame = tk.Frame(self)
        menu_frame.pack(side=tk.TOP)
        object_frame = tk.Frame(self)
        object_frame.pack()

        l = tk.Label(object_frame, text='    ', bg='blue')
        l.pack()

        counter = 0
        def do_job():
            global counter
            l.config(text='do '+str(counter))
            counter += 1

        def clean():
            for widget in object_frame.winfo_children():
                widget.destroy()

        menubar = tk.Menu(menu_frame)
        funcmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='功能', menu=funcmenu)
        querymenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='查詢', menu=querymenu)
        rankmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='排行', menu=rankmenu)
        cleanmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='清空', menu=cleanmenu)

        querymenu.add_command(label='球員數據', command=do_job) #缺command
        querymenu.add_command(label='球隊數據', command=do_job) #缺command
        querymenu.add_separator()
        querymenu.add_command(label='歷屆紀錄表', command=do_job) #缺command

        rankmenu.add_command(label='得分', command=do_job)
        rankmenu.add_command(label='籃板', command=do_job)
        rankmenu.add_command(label='助攻', command=do_job)
        rankmenu.add_command(label='阻攻', command=do_job)
        rankmenu.add_command(label='抄截', command=do_job)
        rankmenu.add_separator()
        rankmenu.add_command(label='三分球%', command=do_job)
        rankmenu.add_command(label='投籃%', command=do_job)
        rankmenu.add_command(label='罰球%', command=do_job)

        cleanmenu.add_command(label='清空', command=clean)

        funcmenu.add_command(label='記分板版', command=do_job)

        self.config(menu=menubar)

    def switch_frame(self.object_frame, frame_class):
        new_frame = frame_class(self)
        if self.object_frame is not None:
            self.object_frame.destroy()
        self.object_frame = new_frame
        self.object_frame.pack()

class MenuFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        

if __name__ == "__main__":
    window = RecordBoard()
    window.mainloop()
