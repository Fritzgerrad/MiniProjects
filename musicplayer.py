#import the libraries
import tkinter as tk
import fnmatch
import os
from turtle import down
from pygame import mixer

#create a new Tkinter module named canvas and set the title, size and background color
canvas = tk.Tk()
canvas.title("Fritzgerrad's Music Player")
canvas.geometry("600x800")
canvas.config(bg="black")

#set the directory folder of the songs to choose from
rootpath = "C:\\Users\DELL\Music\Music\Taylor Swift - Lover (2019) [320]"
#ask the program to only choose files of this type
pattern = "*.mp3"

#initialize the mixer
mixer.init()

#Creating the image Objects
prev_img  = tk.PhotoImage(file = "prev_img.png")
stop_img  = tk.PhotoImage(file = "stop_img.png")
play_img  = tk.PhotoImage(file = "play_img.png")
pause_img  = tk.PhotoImage(file = "pause_img.png")
next_img  = tk.PhotoImage(file = "next_img.png")

#method that selects the song and plays it
def select():
    #Sets the text of label to the selected song so that it displays is
    label.config(text=listBox.get("anchor"))
    #loads the selected song
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    #plays the song
    mixer.music.play()
    canva.config(image = album_image )

def stop():
    #stops the music
    mixer.music.stop()
    #clears the selected option from the listbox
    listBox.select_clear('active')

def play_next():
    #gets the currently selected song
    next_song = listBox.curselection()
    #sets the variable next_song to the song after current song i.e object at the next index
    next_song = next_song[0] + 1
    #gets name of next song which is the song with the index gotten in the line above 
    next_song_name = listBox.get(next_song)
    #sets label to display that song
    label.config(text = next_song_name)
    #loads the song
    mixer.music.load(rootpath + "\\" + next_song_name)
    #plays the song
    mixer.music.play()
    #clears the currently selected song
    listBox.select_clear(0, 'end')
    #activates next_song as currently selected song
    listBox.activate(next_song)
    #Sets next_song as the currently selected song
    listBox.select_set(next_song)
    
def play_prev():
    #gets the currently selected song
    prev_song = listBox.curselection()
    #sets the variable prev_song to the song before current song i.e object at the prev index
    prev_song = prev_song[0] - 1
    #gets name of prev song which is the song with the index gotten in the line above 
    prev_song_name = listBox.get(prev_song)
    #sets label to display that song
    label.config(text = prev_song_name)
    #loads the song
    mixer.music.load(rootpath + "\\" + prev_song_name)
    #plays the song
    mixer.music.play()
    #clears the currently selected song
    listBox.select_clear(0, 'end')
    #activates prev_song as currently selected song
    listBox.activate(prev_song)
    #Sets prev_song as the currently selected song
    listBox.select_set(prev_song)
    
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


#Create a listBox where the songs to choose from would be displayed
listBox = tk.Listbox(canvas,fg = "cyan", bg = "black", width = 100,font = ("poppins",14))
listBox.pack(padx = 15, pady = 15)

#Add label that displays the name of the selected song when select() is called
label = tk.Label(canvas, text = '',bg = 'black',fg = 'yellow', font = ('poppins',18))
label.pack(pady = 15)

#Put a frame which is used to arrange the widgets
top = tk.Frame(canvas, bg = 'black')
top.pack(padx = 10, pady =5,anchor = 'center')

#Adding the prev button
prevButton = tk.Button(canvas,text = 'Prev',image = prev_img,bg='black',borderwidth = 0,command = play_prev)
#The in_ parameter is used to specify that the prevButton is to be placed in the frame top at the left side
prevButton.pack(pady = 15,in_ = top, side = 'left')

#Adding the Stop Button
stopButton = tk.Button(canvas,text = 'Stop',image=stop_img, bg='black',borderwidth = 0,command=stop)
#The in_ parameter is used to specify that the stopButton is to be placed in the frame top at the left side
stopButton.pack(pady = 15, in_ = top, side = 'left')

#Adding the play Button
playButton = tk.Button(canvas,text = 'Play',image = play_img,bg='black',borderwidth = 0,command=select)
#The in_ parameter is used to specify that the playButton is to be placed in the frame top at the left side
playButton.pack(pady = 15, in_ = top, side = 'left')
album_image = tk.PhotoImage("lover.png")
canva = tk.Canvas(canvas,width = 200, height = 110 )
canva.pack(in_ = top, side = 'bottom')

#Adding the pause Button
    
    
pauseButton = tk.Button(canvas,text = 'Pause',image= pause_img, bg='black',borderwidth = 0,command = pause_song)
#The in_ parameter is used to specify that the pauseButton is to be placed in the frame top at the left side
pauseButton.pack(pady = 15, in_ = top, side = 'left')

#Adding the Next Button
nextButton = tk.Button(canvas,text = 'Next',image= next_img, bg='black',borderwidth = 0,command = play_next)
#The in_ parameter is used to specify that the nextButton is to be placed in the frame top at the left side
nextButton.pack(pady = 15, in_ = top, side = 'left')


#insert data(songs) into the listbox
#loops over all directies, files in the path specified
for root,dirs,files in os.walk(rootpath):
    #loops over all files that match the pattern specified
    for filename in fnmatch.filter(files,pattern):
        #adds the file to the listBox
        listBox.insert('end',filename)


canvas.mainloop()
