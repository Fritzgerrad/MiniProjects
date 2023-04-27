#import the libraries
import tkinter as tk
import fnmatch
import os
from turtle import down
from pygame import mixer
import random
from mutagen.mp3 import MP3
import datetime
import time

songLength = 0
file = ""
roots = []
tracks = dict()
#create a new Tkinter module named canvas and set the title, size and background color
canvas = tk.Tk()
canvas.title("Fritzgerrad's Music Player")
canvas.geometry("600x800")
canvas.config(bg="pink")

#set the directory folder of the songs to choose from
#rootpath = "C:\\Users\DELL\Music\Music\Taylor Swift - Lover (2019) [320]"
rootpath = "/home/fritzgerrad/Music"

#ask the program to only choose files of this type
pattern = "*.mp3"

#initialize the mixer
mixer.init()

#Creating the image Objects
prev_img  = tk.PhotoImage(file = "logos/prev_img.png")
stop_img  = tk.PhotoImage(file = "logos/stop_img.png")
play_img  = tk.PhotoImage(file = "logos/play_img.png")
pause_img  = tk.PhotoImage(file = "logos/pause_img.png")
next_img  = tk.PhotoImage(file = "logos/next_img.png")
shuff_img = tk.PhotoImage(file = "logos/shuff.png")
repeat_img = tk.PhotoImage(file = "logos/repeat.png")
base = tk.PhotoImage(file = "images/girl.png")
album_image = tk.PhotoImage(file = "images/ima.png")
#album_image = tk.PhotoImage("lovercover.png")

#method that selects the song and plays it
def getPaths(songname):
    global tracks
    track = tracks[songname]+"//"+songname
    print(tracks[songname])
    return track
        
# def songbar(pos):
#     global songLength   
#     where = str(datetime.timedelta(seconds = int(pos)))
#     if where[0]=='0':
#         where = where[3:]
#     label0.config(text=where)
#     mixer.music.load(file)
#     mixer.music.play(loops=0, start=int(pos))
#     # while mixer.get_busy() == True:
    #     time.sleep(1)
    #     count+=1
    #     w2.set(count)
    #     print(count)
    #     where = str(datetime.timedelta(seconds = int(count)))
    #     if where[0]=='0':
    #         where = where[3:]
    #     label0.config(text=where)
        
# def select():
#     global file
#     global songLength
#     #Sets the text of label to the selected song so that it displays is
#     theSong = listBox.get("anchor")
#     label.config(text=theSong)
#     #loads the selected song
#     #mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
#     #song = MP3(rootpath + "\\" + listBox.get("anchor"))
#     file = getPaths(theSong)
#     mixer.music.load(file)
#     song = MP3(file)
#     songLength = song.info.length
#     print(songLength)
#     #plays the song
#     mixer.music.play()
#     album_display.config(image = base)
#     #slider()
#     print("status", mixer.get_busy())
#     # count = 0
#     # while count < songLength:
#     #     def set_slider():
#     #         current_pos = mixer.music.get_pos()/1000
#     #         w2.set(current_pos)
#     #         canvas.after(100,set_slider)
        
        
        
        
#         #count = int(mixer.music.get_pos())
#         # w2.set(count)
#         # where = str(datetime.timedelta(seconds = count))
        
#         # if where[0]=='0':
#         #     where = where[3:]
#         # label0.config(text=where)
#         # time.sleep(1)
#         # count+=1
        
    
#     #play_next()

def select():
    global file
    global songLength
    theSong = listBox.get("anchor")
    label.config(text=theSong)
    file = getPaths(theSong)
    mixer.music.load(file)
    song = MP3(file)
    songLength = song.info.length
    mixer.music.play()
    album_display.config(image = base)
    slider()

def stop():
    #stops the music
    mixer.music.stop()
    #clears the selected option from the listbox
    listBox.select_clear('active')
    label1['text'] = '-:--'
    label0['text'] = '-:--'

def play_next():
    global songLength
    #gets the currently selected song
    next_song = listBox.curselection()
    #sets the variable next_song to the song after current song i.e object at the next index
    next_song = next_song[0] + 1
    #gets name of next song which is the song with the index gotten in the line above 
    next_song_name = listBox.get(next_song)
    #sets label to display that song
    label.config(text = next_song_name)
    file = getPaths(next_song_name)
    mixer.music.load(file)
    song = MP3(file)
    songLength = song.info.length
    #plays the song
    mixer.music.play()
    album_display.config(image = album_image)
    #clears the currently selected song
    listBox.select_clear(0, 'end')
    #activates next_song as currently selected song
    listBox.activate(next_song)
    #Sets next_song as the currently selected song
    listBox.select_set(next_song)
    slider()
    #play_next()
    
def play_prev():
    global songLength
    #gets the currently selected song
    prev_song = listBox.curselection()
    #sets the variable prev_song to the song before current song i.e object at the prev index
    prev_song = prev_song[0] - 1
    #gets name of prev song which is the song with the index gotten in the line above 
    prev_song_name = listBox.get(prev_song)
    #sets label to display that song
    label.config(text = prev_song_name)
    file = getPaths(prev_song_name)
    mixer.music.load(file)
    song = MP3(file)
    songLength = song.info.length
    mixer.music.play()
    album_display.config(image = album_image)
    #clears the currently selected song
    listBox.select_clear(0, 'end')
    #activates prev_song as currently selected song
    listBox.activate(prev_song)
    #Sets prev_song as the currently selected song
    listBox.select_set(prev_song)
    #play_next()
    slider()
    
def pause_song():
    #checks if the text of the pause button is pause.
    
    if pauseButton["text"] == "Pause":
        #if it is pause, it pauses the music
        mixer.music.pause()
        #sets the text to play
        pauseButton['text'] = "Play"
        
    else:
        #if it's not pause i.e it's play, it unpauses the music
        mixer.music.unpause()
        #sets the text of the pause button to play
        pauseButton['text'] = "Pause"

def shuffle():
    global songLength
    #gets the currently selected song
    next_song = listBox.curselection()
    #sets the variable next_song to the song after current song i.e object at the next index
    x = random.randint(0,listBox.size())
    #next_song = next_song[0] + 1
    #gets name of next song which is the song with the index gotten in the line above 
    next_song_name = listBox.get(x)
    #sets label to display that song
    label.config(text = next_song_name)
    #loads the song
    file = getPaths(next_song_name)
    mixer.music.load(file)
    song = MP3(file)
    songLength = song.info.length
    #plays the song
    #plays the song
    mixer.music.play()
    album_display.config(image = album_image)
    #clears the currently selected song
    listBox.select_clear(0, 'end')
    #activates next_song as currently selected song
    listBox.activate(x)
    #Sets next_song as the currently selected song
    listBox.select_set(x)
    slider()
    shuffle()

def play_all():
    global songLength
    end = listBox.size()
    x = 0
    while x < listBox.size():
        song_name = listBox.get(x)
        #sets label to display that song
        label.config(text = song_name)
        #loads the song
        file = getPaths(song_name)
        mixer.music.load(file)
        song = MP3(file)
        songLength = song.info.length
        #plays the song
        mixer.music.play()
        album_display.config(image = album_image)
        #clears the currently selected song
        listBox.select_clear(0, 'end')
        #activates next_song as currently selected song
        listBox.activate(x)
        #Sets next_song as the currently selected song
        listBox.select_set(x)
        x += 1

def repeat(): 
    global songLength
    #Sets the text of label to the selected song so that it displays is
    theSong = listBox.get("anchor")
    label.config(text= theSong)
    #loads the selected song
    file = getPaths(theSong)
    mixer.music.load(file)
    song = MP3(file)
    songLength = song.info.length
    #plays the song
    #plays the song
    mixer.music.play()
    slider()
    canvas.after(int(songLength)*1000,repeat)
    
def setVolume(vol):
    if mixer.music.get_busy():
        vol = int(vol)
        vol = 1 - vol/10
        mixer.music.set_volume(vol)

# def slider():
#     global songLength
#     last = int(songLength+1) 
#     w2['to'] = last
#     lent = str(datetime.timedelta(seconds = last))
#     if lent[0]=='0':
#         lent = lent[3:]
   
#     label1['text'] = lent
#     label0['text'] = '0:00'
#Create a listBox where the songs to choose from would be displayed
def slider():
    count = 0
    while count < songLength:
        current_pos = mixer.music.get_pos()/1000
        w2.set(current_pos)
        canvas.after(1000)
        count += 1
        
listBox = tk.Listbox(canvas,fg = "brown", bg = "LightSkyBlue", width = 75, height = 7,font = ("Giddyup Std",9))
listBox.pack(padx = 15, pady = 15)

scroll = tk.Scrollbar(canvas,orient = "vertical",command = listBox.yview)
#scroll.grid(column=1,row=0,sticky='ns')
listBox['yscrollcommand'] = scroll
very = tk.Frame(canvas, bg = 'pink')
very.pack(padx = 10, pady =5,anchor = 'center')

down = tk.Frame(canvas, bg = 'pink')
down.pack(padx = 10, pady =5,in_ = very, side = "left")

album_display = tk.Label(canvas, text = '',bg = 'pink',fg = 'black',image = base, font = ('poppins',18))
album_display.pack(padx = 15, pady = 15,in_ = very, side = "left")

first = tk.Frame(canvas, bg = 'pink')
first.pack(padx = 10, pady =5,anchor = 'center')
#Add label that displays the name of the selected song when select() is called
w2 = tk.Scale(canvas, from_=0, to=200, length = 350, command = slider,showvalue=0,sliderlength= 4,highlightbackground="pink",orient="horizontal",troughcolor = "black",borderwidth=1,width=3, bd = 1, bg ="pink")
w2.pack(in_=first,side = "top")
label0 = tk.Label(canvas, text = '-:--',bg = 'pink',fg = 'black', font = ('poppins',10))
label1 = tk.Label(canvas, text = "-:--",bg = 'pink',fg = 'black', font = ('poppins',10))
label1.pack(pady = 1,in_=first, side ="right")
label0.pack(pady = 1,in_= first, side = "left")
#tk.Button(canvas, text='Show', command="show_values").pack()

label = tk.Label(canvas, text = '',bg = 'pink',fg = 'black', font = ('poppins',10))
label.pack(pady = 15)

#Put a frame which is used to arrange the widgets
top = tk.Frame(canvas, bg = 'pink')
top.pack(padx = 10, pady =5,anchor = 'center')

#Adding the prev button
prevButton = tk.Button(canvas,text = 'Prev',image = prev_img,bg='pink',borderwidth = 0,command = play_prev)
#The in_ parameter is used to specify that the prevButton is to be placed in the frame top at the left side
prevButton.pack(pady = 15,in_ = top, side = 'left')

#Adding the Stop Button
stopButton = tk.Button(canvas,text = 'Stop',image=stop_img, bg='pink',borderwidth = 0,command=stop)
#The in_ parameter is used to specify that the stopButton is to be placed in the frame top at the left side
stopButton.pack(pady = 15, in_ = top, side = 'left')

#Adding the play Button
playButton = tk.Button(canvas,text = 'Play',image = play_img,bg='pink',borderwidth = 0,command=select)
#The in_ parameter is used to specify that the playButton is to be placed in the frame top at the left side
playButton.pack(pady = 15, in_ = top, side = 'left')

pauseButton = tk.Button(canvas,text = 'Pause',image= pause_img, bg='pink',borderwidth = 0,command = pause_song)
#The in_ parameter is used to specify that the pauseButton is to be placed in the frame top at the left side
pauseButton.pack(pady = 15, in_ = top, side = 'left')

#Adding the Next Button
nextButton = tk.Button(canvas,text = 'Next',image= next_img, bg='pink',borderwidth = 0,command = play_next)
#The in_ parameter is used to specify that the nextButton is to be placed in the frame top at the left side
nextButton.pack(pady = 15, in_ = top, side = 'left')

shuffleButton = tk.Button(canvas,text = 'Shuffle',image = shuff_img,bg='white',borderwidth = 0,command=shuffle)
#The in_ parameter is used to specify that the playButton is to be placed in the frame top at the left side
shuffleButton.pack(pady = 15, in_ = down, side = 'top')

playallButton = tk.Button(canvas,text = 'PlayAll',bg='white',borderwidth = 0,command=play_all)
#The in_ parameter is used to specify that the playButton is to be placed in the frame top at the left side
playallButton.pack(pady = 15, in_ = down, side = 'top')

repeatButton = tk.Button(canvas,text = 'Repeat',bg='white',borderwidth = 0,image = repeat_img, command=repeat)
#The in_ parameter is used to specify that the playButton is to be placed in the frame top at the left side
repeatButton.pack(pady = 15, in_ = down, side = 'top')

volume = tk.Scale(canvas, from_=0, to=10,tickinterval=0.1, relief = "flat",troughcolor = "black", orient="vertical",command=setVolume,borderwidth=1,width=3,sliderlength = 10, sliderrelief="ridge",background = "pink",bd = 10, bg ="pink",border = 1,highlightbackground="pink",showvalue = 0,length=170)
volume.set(7)
volume.pack(pady = 10,in_ = very,side =  "right")

tk.Label(canvas, text='Volume',font=('poppins',5)).pack(in_ = very,side =  "right")

#Adding the pause Button
    


#insert data(songs) into the listbox
#loops over all directies, files in the path specified
for root,dirs,files in os.walk(rootpath):
    roots .append(root)

for root,dirs,files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        #adds the file to the listBox
        for s in roots:
            song = s+"//"+filename
            if  os.path.exists(song):
                tracks[filename]=s
                
#tracks = sorted(tracks)
#print(tracks)

for key in tracks:
    listBox.insert('end',key)

canvas.mainloop()
