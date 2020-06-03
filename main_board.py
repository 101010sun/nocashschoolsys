import tkinter as tk
from tkinter import ttk
import server

wordfont= ('Arial', 12)

class RecordBoard(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('600x400')
        self.title("記分板板")
        menu_frame = tk.Frame(self)
        menu_frame.pack(side=tk.TOP)
        object_frame = tk.Frame(self)
        object_frame.pack()

        def page_playerdata(): #球員數據頁面
            def clean_smallframe():
                for widget in playerinfo_frame1.winfo_children():
                    widget.destroy()
                for widget in playerinfo_frame2.winfo_children():
                    widget.destroy()
                for widget in playerinfo_frame3.winfo_children():
                    widget.destroy()

            def callbackFunc(event): #處理下拉式選單資訊
                infomat=combo.get()
                infomat = infomat.split(' ') #擷取學號
                data1 = server.player_info()
                tk.Label(playerinfo_frame1,text="姓名", font=wordfont).grid(row=0,column=0)
                tk.Label(playerinfo_frame1,text="背號", font=wordfont).grid(row=0,column=1)
                tk.Label(playerinfo_frame1,text="入隊學年", font=wordfont).grid(row=0,column=2)
                tk.Label(playerinfo_frame1,text="退隊學年", font=wordfont).grid(row=0,column=3)
                tk.Label(playerinfo_frame1,text="隊長", font=wordfont).grid(row=0,column=4)
                tk.Label(playerinfo_frame1,text="上場次數", font=wordfont).grid(row=0,column=5)

                tk.Label(playerinfo_frame1,text=data1[0][1], font=wordfont).grid(row=1,column=0)
                tk.Label(playerinfo_frame1,text=data1[0][2], font=wordfont).grid(row=1,column=1)
                tk.Label(playerinfo_frame1,text=data1[0][3], font=wordfont).grid(row=1,column=2)
                tk.Label(playerinfo_frame1,text=data1[0][4], font=wordfont).grid(row=1,column=3)
                tk.Label(playerinfo_frame1,text=data1[0][5], font=wordfont).grid(row=1,column=4)

                data2 = server.player_data_average()
                tk.Label(playerinfo_frame2,text="得分率", font=wordfont).grid(row=0,column=0)
                tk.Label(playerinfo_frame2,text="進攻籃板率", font=wordfont).grid(row=0,column=1)
                tk.Label(playerinfo_frame2,text="防守籃板率", font=wordfont).grid(row=0,column=2)
                tk.Label(playerinfo_frame2,text="助攻率", font=wordfont).grid(row=0,column=3)
                tk.Label(playerinfo_frame2,text="阻攻率", font=wordfont).grid(row=0,column=4)
                tk.Label(playerinfo_frame2,text="抄截率", font=wordfont).grid(row=0,column=5)
                tk.Label(playerinfo_frame2,text="犯規率", font=wordfont).grid(row=0,column=6)
                tk.Label(playerinfo_frame2,text="失誤率", font=wordfont).grid(row=0,column=7)

                tk.Label(playerinfo_frame2,text=data2[3][1], font=wordfont).grid(row=1,column=0)
                tk.Label(playerinfo_frame2,text=data2[3][2], font=wordfont).grid(row=1,column=1)
                tk.Label(playerinfo_frame2,text=data2[3][3], font=wordfont).grid(row=1,column=2)
                tk.Label(playerinfo_frame2,text=data2[3][4], font=wordfont).grid(row=1,column=3)
                tk.Label(playerinfo_frame2,text=data2[3][5], font=wordfont).grid(row=1,column=4)
                tk.Label(playerinfo_frame2,text=data2[3][6], font=wordfont).grid(row=1,column=5)
                tk.Label(playerinfo_frame2,text=data2[3][7], font=wordfont).grid(row=1,column=6)
                tk.Label(playerinfo_frame2,text=data2[3][8], font=wordfont).grid(row=1,column=7)

                data3 = server.player_hit_rate()
                tk.Label(playerinfo_frame3,text="三分球命中率", font=wordfont).grid(row=0,column=0)
                tk.Label(playerinfo_frame3,text="投籃命中率", font=wordfont).grid(row=0,column=1)
                tk.Label(playerinfo_frame3,text="罰球命中率", font=wordfont).grid(row=0,column=2)
                for i in range(1,4):
                    if (data3[3][i] == None):
                        tk.Label(playerinfo_frame3,text="目前還沒有表現", font=wordfont).grid(row=1,column=i-1)
                    else:
                        tk.Label(playerinfo_frame3,text=data3[3][i], font=wordfont).grid(row=1,column=i-1)

            tk.Label(object_frame,text="球員數據", font=('Arial', 18, "bold")).grid(row=0, column=1)
            tk.Label(object_frame,text="                        ", font=(18)).grid(row=0, column=2) #排版用的
            tk.Label(object_frame,text="選擇要查詢的球員學號和姓名").grid(row=1,column=0)
            combo = ttk.Combobox(object_frame, values=server.online_player(), state="readonly") # 先放現有球員之後要改
            combo.grid(row=1,column=1)
            playerinfo_frame1 = tk.Frame(self)
            playerinfo_frame1.pack()
            playerinfo_frame2 = tk.Frame(self)
            playerinfo_frame2.pack()
            playerinfo_frame3 = tk.Frame(self)
            playerinfo_frame3.pack()
            combo.bind("<<ComboboxSelected>>", callbackFunc, clean_smallframe()) #選取之後顯示球員資料

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

        def page_startboard():
            tk.Button(object_frame, text='開始記錄', width=20, height=10, command=lambda: [clean_frame(), page_boardgetgameinfo()]).pack()

        def page_boardgetgameinfo():
            def do_print():
                print('%s' %(dateString.get()))
                print('%s' %(gameString.get()))
                print('%s' %(oppschoolString.get()))
                print('%s' %(oppdepString.get()))
                
            tk.Label(object_frame, text="開始記錄", font=('Arial', 18, "bold")).grid(column=0, row=0, sticky=tk.W)
            #Label-文字標籤
            dateLabel = tk.Label(object_frame, text='日期:')
            gameLabel = tk.Label(object_frame, text='盃賽名稱:')
            oppschoolLabel = tk.Label(object_frame, text='對手學校')
            oppdepLabel = tk.Label(object_frame, text='對手系名')

            dateLabel.grid(column=0, row=1, sticky=tk.W)
            gameLabel.grid(column=0, row=2, sticky=tk.W)
            oppschoolLabel.grid(column=0, row=3, sticky=tk.W)
            oppdepLabel.grid(column=0, row=4, sticky=tk.W)
            #定義文字輸入框裡的文字物件
            dateString = tk.StringVar()
            gameString = tk.StringVar()
            oppschoolString = tk.StringVar()
            oppdepString = tk.StringVar()
            dateEntry = tk.Entry(object_frame, show=None, font=('Arial', 14), textvariable=dateString)
            gameEntry = tk.Entry(object_frame, show=None, font=('Arial', 14), textvariable=gameString)
            oppschoolEntry = tk.Entry(object_frame, show=None, font=('Arial', 14), textvariable=oppschoolString)
            oppdepEntry = tk.Entry(object_frame, show=None, font=('Arial', 14), textvariable=oppdepString)

            dateEntry.grid(column=1, row=1, padx=10)
            gameEntry.grid(column=1, row=2, padx=10)
            oppschoolEntry.grid(column=1, row=3, padx=10)
            oppdepEntry.grid(column=1, row=4, padx=10)

            tk.Button(object_frame, text='確定', command=lambda: [clean_frame(), do_print(), page_boardchoosplayer()]).grid(column=1, row=5, sticky=tk.N)
    
        def page_boardchoosplayer():
            data = server.online_player()
            #print(data)

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
        funcmenu.add_command(label='記分板版', command=lambda: [clean_frame(), page_startboard()])

        self.config(menu=menubar)
    
if __name__ == "__main__":
    window = RecordBoard()
    window.iconbitmap('./board.ico')
    # window.configure(bg='Tan')
    window.mainloop()
