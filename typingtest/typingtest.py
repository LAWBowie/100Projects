import tkinter as tk
import time

def check_entry():
    end_time = time.time()
    text_entered = entry.get()
    words = text_entered.split()
    words_count = len(words)
    total_time = end_time - start_time
    words_per_minute = int(words_count / (total_time / 60))
    result_label.config(text=f'Your typing speed is: {words_per_minute} WPM')

def start_test():
    global start_time
    start_time = time.time()
    check_button.config(state='normal')

root = tk.Tk()

label = tk.Label(root, text='Start typing the moment you see this text...')
label.pack()

entry = tk.Entry(root)
entry.pack()

check_button = tk.Button(root, text='Check Speed', state='disabled', command=check_entry)
check_button.pack()

start_button = tk.Button(root, text='Start Test', command=start_test)
start_button.pack()

result_label = tk.Label(root, text='')
result_label.pack()

root.mainloop()
