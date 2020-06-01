import tkinter as tk

class RecordBoard(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('600x400')
        self.title("記分板板")
        menu_frame = tk.Frame(self)
        menu_frame.pack(side=tk.TOP)
        object_frame = tk.Frame(self)
        object_frame.pack()

        def page_playerdata():
            tk.Label(object_frame,text="球員數據頁面", font=('Arial', 18, "bold")).pack(side="top", fill="x", pady=5)

        def page_teamdata():
            tk.Label(object_frame,text="球隊數據頁面", font=('Arial', 18, "bold")).pack(side="top", fill="x", pady=5)

        def page_recoardtable():
            tk.Label(object_frame,text="歷屆紀錄表", font=('Arial', 18, "bold")).pack(side="top", fill="x", pady=5)

        def page_getrank():
            tk.Label(object_frame,text="得分排行", font=('Arial', 18, "bold")).pack(side="top", fill="x", pady=5)

        def page_basketrank():
            tk.Label(object_frame,text="籃板排行", font=('Arial', 18, "bold")).pack(side="top", fill="x", pady=5)
        
        def page_soporank():
            tk.Label(object_frame,text="助攻排行", font=('Arial', 18, "bold")).pack(side="top", fill="x", pady=5)
        
        def page_blockrank():
            tk.Label(object_frame,text="阻攻排行", font=('Arial', 18, "bold")).pack(side="top", fill="x", pady=5)

        def page_catchrank():
            tk.Label(object_frame,text="抄截排行", font=('Arial', 18, "bold")).pack(side="top", fill="x", pady=5)

        def page_thirdgraderank():
            tk.Label(object_frame,text="三分球排行", font=('Arial', 18, "bold")).pack(side="top", fill="x", pady=5)

        def page_throwrank():
            tk.Label(object_frame,text="投籃排行", font=('Arial', 18, "bold")).pack(side="top", fill="x", pady=5)

        def page_punishrank():
            tk.Label(object_frame,text="罰球排行", font=('Arial', 18, "bold")).pack(side="top", fill="x", pady=5)

        def page_newplayer():
            tk.Label(object_frame,text="新增球員", font=('Arial', 18, "bold")).pack(side="top", fill="x", pady=5)

        def page_changedata():
                    tk.Label(object_frame,text="修改資料", font=('Arial', 18, "bold")).pack(side="top", fill="x", pady=5)

        def page_board():
                    tk.Label(object_frame,text="記分板版", font=('Arial', 18, "bold")).pack(side="top", fill="x", pady=5)

        #清空object_frame裡面的東西
        def clean_frame():
            for widget in object_frame.winfo_children():
                widget.destroy()

        menubar = tk.Menu(menu_frame) #宣告一個Menu的frame裡面有: 模式 設定 查詢 排行
        funcmenu = tk.Menu(menubar, tearoff=0) 
        menubar.add_cascade(label='模式', menu=funcmenu)
        setmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='設定', menu=setmenu)
        querymenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='查詢', menu=querymenu)
        rankmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='排行', menu=rankmenu)
        #查詢選項的下拉式選單
        querymenu.add_command(label='球員數據', command=lambda: [clean_frame(), page_playerdata()])
        querymenu.add_command(label='球隊數據', command=lambda: [clean_frame(), page_teamdata()])
        querymenu.add_separator() #分隔線
        querymenu.add_command(label='歷屆紀錄表', command=lambda: [clean_frame(), page_recoardtable()])
        #排行選項的下拉式選單
        rankmenu.add_command(label='得分', command=lambda: [clean_frame(), page_getrank()])
        rankmenu.add_command(label='籃板', command=lambda: [clean_frame(), page_basketrank()])
        rankmenu.add_command(label='助攻', command=lambda: [clean_frame(), page_soporank()])
        rankmenu.add_command(label='阻攻', command=lambda: [clean_frame(), page_blockrank()])
        rankmenu.add_command(label='抄截', command=lambda: [clean_frame(), page_catchrank()])
        rankmenu.add_separator() #分隔線
        rankmenu.add_command(label='三分球%', command=lambda: [clean_frame(), page_thirdgraderank()])
        rankmenu.add_command(label='投籃%', command=lambda: [clean_frame(), page_throwrank()])
        rankmenu.add_command(label='罰球%', command=lambda: [clean_frame(), page_punishrank()])
        #設定選項的下拉式選單
        setmenu.add_command(label='新增球員', command=lambda: [clean_frame(), page_newplayer()])
        setmenu.add_command(label='修改球員資料', command=lambda: [clean_frame(), page_changedata()])
        #模式選項的下拉式選單
        funcmenu.add_command(label='記分板版', command=lambda: [clean_frame(), page_board()])

        self.config(menu=menubar)
    
if __name__ == "__main__":
    window = RecordBoard()
    window.iconbitmap('./board.ico')
    window.mainloop()
