import tkinter as tk

window = tk.Tk()
window.title('board')
window.geometry('500x300')

l = tk.Label(window, text='    ', bg='blue')
l.pack()

counter = 0
def do_job():
    global counter
    l.config(text='do '+str(counter))
    counter += 1

def clean():
    l.pack_forget()


menubar = tk.Menu(window)
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

window.config(menu=menubar)
window.mainloop()
