import tkinter as tk

window = tk.Tk() #建立主視窗window
window.title('board')
window.geometry('400x300')
window.configure(background='white')

top_frame = tk.Frame(window) #建立top群
top_frame.pack()
bottom_frame = tk.Frame(window) #建立bottom群
bottom_frame.pack(side=tk.BOTTOM)
# 建立事件處理函式
def echo_hello():
    result = "查詢結果等等..."
    result_label.configure(text=result)

left_button = tk.Button(top_frame, text='球員數據', fg='red')
left_button.pack(side=tk.LEFT)

middle_button = tk.Button(top_frame, text='球隊數據', fg='green')
middle_button.pack(side=tk.LEFT)

right_button = tk.Button(top_frame, text='排行查詢', fg='blue')
right_button.pack(side=tk.LEFT)


result_label = tk.Button(bottom_frame, text='', fg='black')
result_label.pack(side=tk.BOTTOM)
bottom_button = tk.Button(bottom_frame, text='查詢', fg='black', command=echo_hello)
bottom_button.pack(side=tk.BOTTOM)

window.mainloop()
