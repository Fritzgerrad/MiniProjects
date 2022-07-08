import tkinter as tk
from turtle import down
from pygame import mixer
from mutagen.mp3 import MP3
canvas = tk.Tk()
canvas.title("Fritzgerrad's Music Player")
canvas.geometry("600x800")
canvas.config(bg="pink")
volume = tk.Scale(canvas, from_=0, to=10,tickinterval=0.1, orient="vertical",width=1, bg = "pink",highlightbackground="pink")
volume.set(10)
volume.pack(pady = 10)

canvas.mainloop()