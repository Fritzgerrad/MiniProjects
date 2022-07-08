from tkinter import *
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk


root= Tk()
root.title('reanits.blogspot.com')
#root.iconbitmap('1.png')
root.geometry('300x400')
pygame.mixer.init()
def playtime():
    Currenttime = pygame.mixer.music.get_pos()/1000
    sliderlabel.config(text=f'Slider:{int(myslider.get())} and SongPos:{int(Currenttime)}')
    ConvertCurrentTime = time.strftime('%M:%S',time.gmtime(Currenttime))
    #Currentsong = songbox.curselection()
    song = songbox.get(ACTIVE)
    song = f'D:/Python/Test2/sound/{song}.mp3'
    songmut = MP3(song)
    global SongLength
    SongLength=songmut.info.length
    ConvertSongLength = time.strftime('%M:%S', time.gmtime(SongLength))
    SliderPosition = int(SongLength)
    statusbar.config(text=f'Time Elasped: {ConvertCurrentTime} of {ConvertSongLength} ')
    myslider.config(to=SliderPosition, value=int(Currenttime))
    statusbar.after(1000,playtime)
def deletesongmusic():
    songbox.delete(ANCHOR)
    pygame.mixer.music.stop()
def deletesongsmusics():
    songbox.delete(0,END)
    pygame.mixer.music.stop()
def addsongmusic():
    song = filedialog.askopenfilename(initialdir='sound/', title="Choose File Song", filetypes=(("MP3 file", "*.mp3"),))
    song = song.replace("D:/Python/Test2/sound/","")
    song = song.replace(".mp3", "")
    songbox.insert(END,song)
def addsongsmusic():
    songs = filedialog.askopenfilenames(initialdir='sound/', title="Choose File Song", filetypes=(("MP3 file", "*.mp3"),))
    for song in songs:
        song = song.replace("D:/Python/Test2/sound/", "")
        song = song.replace(".mp3", "")
        songbox.insert(END, song)
def playmusic():
    song = songbox.get(ACTIVE)
    song = song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    playtime()
    #SliderPosition = int(SongLength)
    #myslider.config(to=SliderPosition, value=0)
def stopmusic():
    pygame.mixer.music.stop()
    songbox.select_clear(ACTIVE)
    statusbar.config(text='')
def nextmusic():
    nextone = songbox.curselection()
    nextone = nextone[0]+1
    song = songbox.get(nextone)
    song = f'D:/Python/Test2/sound/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    songbox.select_clear(0,END)
    songbox.activate(nextone)
    songbox.selection_set(nextone, last=None)
def preback():
    nextone = songbox.curselection()
    nextone = nextone[0] - 1
    song = songbox.get(nextone)
    song = f'D:/Python/Test2/sound/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    songbox.select_clear(0, END)
    songbox.activate(nextone)
    songbox.selection_set(nextone, last=None)
    global paused
    paused = False
def pause(is_paused):
    global paused
    paused = is_paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True
def slider(x):
    sliderlabel.config(text=f'{int(myslider.get())} of {int(SongLength)}')
    song = songbox.get(ACTIVE)
    song = f'{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(myslider.get()))
songbox= Listbox(root, bg="black", fg="green", width=80,selectbackground="gray",selectforeground="black")
songbox.pack(pady=20)
# backbtn= PhotoImage(file='image/forward101.png')
# forwardbtn= PhotoImage(file='image/forward101.png')
# playbtn= PhotoImage(file='image/Play101.png')
# pausebtn= PhotoImage(file='image/pause101.png')
# stopbtn= PhotoImage(file='image/Stop101.png')
controlframe= Frame(root)
controlframe.pack()
backbutton= Button(controlframe, borderwidth=0, command=preback)
frowardbutton= Button(controlframe, borderwidth=0,command=nextmusic)
playbutton= Button(controlframe, borderwidth=0, command=playmusic)
pausebutton= Button(controlframe, borderwidth=0, command=lambda: pause(paused))
stopbutton= Button(controlframe, borderwidth=0, command=stopmusic)
backbutton.grid(row=0, column=1, padx=10)
frowardbutton.grid(row=0, column=2, padx=20)
playbutton.grid(row=0, column=3, padx=20)
pausebutton.grid(row=0, column=4, padx=20)
stopbutton.grid(row=0, column=5, padx=20)
#create Menu
mymenu = Menu(root)
root.config(menu=mymenu)
addsong = Menu(mymenu)
mymenu.add_cascade(label="file", menu=addsong)
addsong.add_command(label="Open Song or Playlist",command=addsongmusic)
addsong.add_command(label="Open Many Songs or Playlist",command=addsongsmusic)
deletesong = Menu(mymenu)
mymenu.add_cascade(label="Delete", menu=deletesong)
deletesong.add_command(label="Delete Song or Playlist",command=deletesongmusic)
deletesong.add_command(label="Delete All Songs or Playlist",command=deletesongsmusics)
statusbar= Label(root, text='',bd=1, relief=GROOVE, anchor=E)
statusbar.pack(fill=X,side=BOTTOM, ipady=2)
myslider = ttk.Scale(root,from_=0, to=100, orient=HORIZONTAL, value=0, command=slider, length=500)
myslider.pack(pady=30)
sliderlabel = Label(root, text="0")
sliderlabel.pack(pady=10)

root.mainloop()