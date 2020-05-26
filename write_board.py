import tkinter as tk

window = tk.Tk() #建立視窗window
window.title('write board')
window.geometry('500x300') #window大小

def do_print():
    print('game name: %s' %(gameString.get))
    print('opponent school: %s' %(oppschoolString.get))
    print('opponent department: %s' %(oppdepString.get))

#Label
gameLabel = tk.Label(window, text='盃賽名稱:')
oppschoolLabel = tk.Label(window, text='對手學校')
oppdepLabel = tk.Label(window, text='對手系名')

gameLabel.grid(column=0, row=0, sticky=tk.W)
oppschoolLabel.grid(column=0, row=1, sticky=tk.W)
oppdepLabel.grid(column=0, row=2, sticky=tk.W)

#Entry輸入
gameString = tk.StringVar()
oppschoolString = tk.StringVar()
oppdepString = tk.StringVar()
gameEntry = tk.Entry(window, show=None, font=('Arial', 14), textvariable=gameString)
oppschoolEntry = tk.Entry(window, show=None, font=('Arial', 14), textvariable=oppschoolString)
oppdepEntry = tk.Entry(window, show=None, font=('Arial', 14), textvariable=oppdepString)

gameEntry.grid(column=1, row=0, padx=10)
oppschoolEntry.grid(column=1, row=1, padx=10)
oppdepEntry.grid(column=1, row=2, padx=10)

#提交Button
pushButton = tk.Button(window, text='提交', command=do_print)

pushButton.grid(column=0, row=3, pady=10, sticky=tk.W)

window.mainloop() #主視窗迴圈顯示