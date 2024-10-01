import time
from tkinter import *
import pygame

#зупиняє

def stop():
    btn_start.pack()
    btn_stop.pack_forget()
    pygame.mixer.music.pause()

#програє звук

def sound():
    btn_start.pack_forget()
    btn_stop.pack()
    pygame.mixer.music.play()

#починає
def start():
    duration = int(seconds.get())
    while duration:
        m, s = divmod(int(duration), 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        count_digit['text'] = min_sec_format
        count_digit.update()
        time.sleep(1)
        duration -= 1
    sound()

#встановлює рамки
root = Tk()
root.title('Таймер')
root.geometry('200x200')
root.resizable(0, 0)

count_digit = Label(root, text='0', font='Arial 15 bold')
count_digit.pack()

seconds = Entry(root, font='Arial 15 bold', width=7)
seconds.pack(pady=10)
#команда старт
btn_start = Button(root, text='КГ одягу', font='Arial 15 bold', command=start)
btn_start.pack()
#команда стоп
btn_stop = Button(root, text='стирка завершина', font='Arial 15 bold', command=stop)

root.mainloop()